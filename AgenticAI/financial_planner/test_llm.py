from config.llm import llm


def main():
    response = llm.call(
        messages=[
            {
                "role": "user",
                "content": (
                    "Reply with exactly: "
                    "DeepSeek integration is working."
                ),
            }
        ]
    )

    print(response)


if __name__ == "__main__":
    main()