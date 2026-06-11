from fastapi import APIRouter
from pydantic import BaseModel
from services.code_analyzer import analyze_repository

from services.github_service import clone_repository
from services.dependency_graph import build_dependency_graph

from services.context_engine import select_relevant_files


router = APIRouter()


class RepoRequest(BaseModel):

    url:str

    query:str


@router.post("/analyze-repo")
def analyze_repo(request:RepoRequest):


    repo_path = clone_repository(
        request.url
    )

    if repo_path is None:

         return {
             "error":
             "Repository not found or invalid GitHub URL"
            }


    analysis = analyze_repository(
        repo_path
    )


    important_files = (
        select_relevant_files(
            analysis,
            request.query
        )
    )


    return {

        "important_files":
        important_files,

        "analysis":
        analysis

    }