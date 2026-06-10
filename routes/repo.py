from fastapi import APIRouter
from pydantic import BaseModel
from services.code_analyzer import analyze_repository

from services.github_service import clone_repository
from services.dependency_graph import build_dependency_graph


router = APIRouter()


class RepoRequest(BaseModel):
    url: str


@router.post("/analyze-repo")
def analyze_repo(request: RepoRequest):


    repo_path = clone_repository(
        request.url
    )


    code_analysis = analyze_repository(
        repo_path
    )


    dependency_graph = build_dependency_graph(
        repo_path
    )


    return {

        "repo_path": repo_path,

        "code_analysis": code_analysis,

        "dependency_graph": dependency_graph

    }