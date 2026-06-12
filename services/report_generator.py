from services.risk_engine import calculate_risk

def generate_security_report(findings):

    report = {
        "total_issues": len(findings),
        "severity_count": {
            "CRITICAL":0,
            "HIGH":0,
            "MEDIUM":0,
            "LOW":0
        },
        "issues": []
    }

    for finding in findings:

        risk = calculate_risk(
        finding
        )

        severity = risk["severity"]

        report["severity_count"][severity] += 1

        report["issues"].append(
            {

                "file":
                finding["file"],


                "issue":
                finding["issue"],


                "risk":
                finding["risk"],


                "fix":
                finding["recommended_fix"],


                "severity":
                severity,


                "risk_score":
                risk["risk_score"],


                "priority":
                risk["priority"]

            }
        )

    return report