import os


SECURITY_RULES = {


    "eval(": {

        "issue":
        "Unsafe eval usage",


        "risk":
        "User controlled input can execute malicious code",


        "fix":
        "Avoid eval. Use safer parsing methods",


        "severity":
        "CRITICAL"

    },



    "exec(": {

        "issue":
        "Unsafe exec usage",


        "risk":
        "Dynamic code execution vulnerability",


        "fix":
        "Remove exec usage",


        "severity":
        "CRITICAL"

    },



    "password =": {

        "issue":
        "Hardcoded password",


        "risk":
        "Credentials can leak through source code",


        "fix":
        "Use environment variables",


        "severity":
        "HIGH"

    },



    "secret": {

        "issue":
        "Possible secret exposure",


        "risk":
        "Application secrets may be leaked",


        "fix":
        "Move secrets to secure storage",


        "severity":
        "HIGH"

    }

}



def scan_security(repo_path):


    findings = []


    for root, dirs, files in os.walk(repo_path):


        for file in files:


            if file.endswith(".py"):


                path = os.path.join(root,file)


                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:


                    code = f.read().lower()


                for pattern, details in SECURITY_RULES.items():


                    if pattern in code:


                        findings.append(

                            {

                            "file":
                            path,


                            "detected_pattern":
                            pattern,


                            "issue":
                            details["issue"],


                            "risk":
                            details["risk"],


                            "recommended_fix":
                            details["fix"],


                            "severity":
                            details["severity"]

                            }

                        )


    return findings