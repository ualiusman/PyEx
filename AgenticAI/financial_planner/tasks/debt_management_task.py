from crewai import Task


def create_debt_management_task(agent, budgeting_task):
    return Task(
        description=(
            "Analyze the user's current debts, including balances "
            "and interest rates.\n\n"

            "Perform the following steps:\n"
            "1. List all debts and their interest rates.\n"
            "2. Identify the highest-interest debt.\n"
            "3. Recommend an appropriate repayment priority.\n"
            "4. Develop a practical repayment strategy.\n"
            "5. Consider the monthly cash flow identified by the "
            "budgeting analysis.\n"
            "6. Explain potential debt consolidation or lower-interest "
            "options when appropriate.\n"
            "7. Explain how the proposed strategy could reduce "
            "interest costs or repayment time.\n\n"

            "Do not recommend debt payments that exceed the user's "
            "available monthly cash flow."
        ),

        expected_output=(
            "A debt management plan containing:\n"
            "- Debt prioritization\n"
            "- Recommended repayment strategy\n"
            "- Suggested monthly allocation\n"
            "- Explanation of why the strategy was selected\n"
            "- Potential consolidation/refinancing considerations"
        ),

        agent=agent,

        context=[budgeting_task]
    )