from config.financial_data import USER_FINANCIAL_DATA
from crew import create_financial_crew


def main():

    financial_crew = create_financial_crew()

    result = financial_crew.kickoff(
        inputs=USER_FINANCIAL_DATA
    )

    print("\n")
    print("=" * 80)
    print("FINANCIAL PLANNING RESULT")
    print("=" * 80)

    print(result.raw)


if __name__ == "__main__":
    main()