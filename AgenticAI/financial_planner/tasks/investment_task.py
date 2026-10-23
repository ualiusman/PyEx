from crewai import Task


def create_investment_task(agent, budgeting_task, debt_management_task):
    return Task(
        description=(
            "Assess the user's financial situation and develop "
            "an appropriate investment strategy.\n\n"

            "Perform the following steps:\n"
            "1. Assess the user's financial goals.\n"
            "2. Assess their risk tolerance if provided.\n"
            "3. Consider their available monthly cash flow.\n"
            "4. Consider their existing debt and repayment strategy.\n"
            "5. Consider their savings goal and emergency savings needs.\n"
            "6. Recommend suitable investment categories such as "
            "stocks, bonds, mutual funds, or ETFs when appropriate.\n"
            "7. Provide a brief explanation of potential risks and "
            "returns for each recommendation.\n"
            "8. Explain how much money could reasonably be invested "
            "without compromising essential expenses, debt repayment, "
            "or emergency savings.\n\n"

            "If the user has insufficient information about risk "
            "tolerance or investment horizon, explicitly identify "
            "the missing information rather than inventing it."
        ),

        expected_output=(
            "A personalized investment plan containing:\n"
            "- Financial goals\n"
            "- Risk considerations\n"
            "- Recommended investment categories\n"
            "- Risk and return considerations\n"
            "- Suggested investment allocation\n"
            "- Important assumptions or missing information"
        ),

        agent=agent,

        context=[
            budgeting_task,
            debt_management_task
        ]
    )