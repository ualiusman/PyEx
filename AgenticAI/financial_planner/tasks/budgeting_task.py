from crewai import Task


def create_budgeting_task(agent):
    return Task(
        description=(
            "Analyze the user's financial information.\n\n"

            "The financial information contains:\n"
            "- Monthly income\n"
            "- Monthly expenses\n"
            "- Current debts\n"
            "- Savings goal\n\n"

            "Perform the following steps:\n"
            "1. Calculate total monthly expenses.\n"
            "2. Calculate monthly disposable income.\n"
            "3. Compare disposable income with the savings goal.\n"
            "4. Identify unnecessary or potentially reducible expenses.\n"
            "5. Create a realistic monthly budget.\n"
            "6. Determine how much money can reasonably be allocated "
            "to debt repayment and savings.\n\n"

            "Do not invent missing financial information. "
            "Clearly state any assumptions."
        ),

        expected_output=(
            "A structured monthly budget containing:\n"
            "- Total income\n"
            "- Total expenses\n"
            "- Remaining disposable income\n"
            "- Recommended spending allocation\n"
            "- Recommended savings allocation\n"
            "- Amount potentially available for debt repayment\n"
            "- Areas where expenses could be reduced"
        ),

        agent=agent
    )