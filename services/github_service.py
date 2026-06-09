import git
import tempfile
import os

def clone_repository(repo_url: str):

    temp_dir = tempfile.mkdtemp()

    try:
        git.Repo.clone_from(
            repo_url,
            temp_dir
        )

        return temp_dir
    
    except Exception as e:

        raise Exception(
            f"Clone failed: {str(e)}"
        )