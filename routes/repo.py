from fastapi import APIRouter
from pydantic import BaseModel
from services.code_analyzer import analyze_repository

from services.github_service import clone_repository
from services.dependency_graph import build_dependency_graph

from services.context_engine import select_relevant_files
from agents.manager_agent import manager_agent
from agents.code_explainer_agent import explain_codebase
from agents.security_agent import scan_security
from services.report_generator import generate_security_report

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

    selected_agent = manager_agent(request.query)

    agent_result = None


    if selected_agent["agent"] == "code_explainer_agent":

        agent_result = explain_codebase(
            analysis
        )

    if selected_agent["agent"] == "security_agent":


        findings = scan_security(
        repo_path
        )


        agent_result = generate_security_report(
        findings
        )


    return {

        "selected_agent":
        selected_agent,


        "agent_result":
        agent_result,


        "important_files":
        important_files
    }