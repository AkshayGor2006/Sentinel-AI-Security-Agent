def select_relevant_files(
        code_analysis,
        user_query
):
    selected_files = []

    keywords = (user_query.lower().split())

    for file_info in code_analysis:
        score = 0

        file_text = (
            str(file_info).lower()
        )

        for word in keywords:

            if word is file_text:
                score += 1


            if score > 0:

                selected_files.append(
                    {
                    "file": file_info["file"],
                    "score": score
                    }
                )

        selected_files.sort(
            key=lambda x:x["score"],
            reverse=True
        )

        return selected_files