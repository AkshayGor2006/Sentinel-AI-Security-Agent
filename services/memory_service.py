import json
from datetime import datetime

FILE_PATH = "storage/scan_history.json"

def save_scan(repo_url, report):
    with open(FILE_PATH, "r") as file:
        history = json.load(file)

        scan_data = {
            "repo": repo_url,
            "date": str(datetime.now()),
            "report": report
        }

        history.append(scan_data)

    with open(FILE_PATH, "w") as file:
            json.dump(
                history,
                file,
                indent=4
            )

    return scan_data

def get_history():


    with open(FILE_PATH,"r") as file:

        history = json.load(
            file
        )

    return history