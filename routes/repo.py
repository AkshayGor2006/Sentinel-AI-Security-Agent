from fastapi import APIRouter
from pydantic import BaseModel
from services.code_analyzer import analyze_repository

from services.github_service import clone_repository


router = APIRouter()


class RepoRequest(BaseModel):
    url: str


@router.post("/analyze-repo")
def analyze_repo(request: RepoRequest):


    repo_path = clone_repository(
        request.url
    )


    result = analyze_repository(
        repo_path
    )


    return {

        "repo_path": repo_path,

        "analysis": result

    }