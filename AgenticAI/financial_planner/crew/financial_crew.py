from crewai import Crew, Process

from agents import (
    create_budgeting_agent,
    create_investment_agent,
    create_debt_management_agent
)

from tasks import (
    create_budgeting_task,
    create_investment_task,
    create_debt_management_task
)


def create_financial_crew():

    # -------------------------
    # Create Agents
    # -------------------------

    budgeting_agent = create_budgeting_agent()

    investment_agent = create_investment_agent()

    debt_management_agent = create_debt_management_agent()


    # -------------------------
    # Create Tasks
    # -------------------------

    budgeting_task = create_budgeting_task(
        budgeting_agent
    )

    debt_management_task = create_debt_management_task(
        debt_management_agent,
        budgeting_task
    )

    investment_task = create_investment_task(
        investment_agent,
        budgeting_task,
        debt_management_task
    )


    # -------------------------
    # Create Crew
    # -------------------------

    crew = Crew(
        agents=[
            budgeting_agent,
            debt_management_agent,
            investment_agent
        ],

        tasks=[
            budgeting_task,
            debt_management_task,
            investment_task
        ],

        process=Process.sequential,

        verbose=True
    )

    return crew