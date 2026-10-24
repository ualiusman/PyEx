from crewai import Task


def create_financial_planning_task(
    agent,
    budgeting_task,
    debt_management_task,
    investment_task
):
    """
    Create the final financial planning task.

    This task combines the outputs of:
    - Budgeting Agent
    - Debt Management Agent
    - Investment Agent

    The Financial Planner Agent converts those analyses into
    one concise, actionable financial plan for the user.
    """

    return Task(
        description="""
You are the final financial planner.

Review the outputs produced by the following specialists:

1. Budgeting Advisor
2. Debt Management Specialist
3. Investment Advisor

Your job is to combine their findings into ONE concise,
practical financial plan.

IMPORTANT RULES:

- Do NOT repeat the detailed analysis from the specialist agents.
- Do NOT write a long financial report.
- Focus only on the most important conclusions.
- Resolve conflicts between recommendations.
- Make sure the recommended allocation is consistent with
  the user's available income.
- Do not invent missing financial information.
- If important information is missing, mention it briefly.
- Do not guarantee investment returns.
- Do not recommend taking excessive financial risk.
- Give the user no more than 3 immediate action items.
- Keep the final response below 250 words.

The final plan should answer:

1. How much money comes in each month?
2. How much is being spent?
3. How much is available?
4. What should the user prioritize?
5. How should the available money be divided?
6. What should the user do next?

Return ONLY the final financial plan.
""",

        expected_output="""
Return the answer using EXACTLY this structure:

FINANCIAL PLAN

Monthly Summary
Income: $X
Expenses: $X
Available: $X

Priorities
1. [Most important priority]
2. [Second priority]
3. [Third priority]

Monthly Allocation
Expenses: $X
Debt: $X
Savings: $X
Investment: $X

Action Plan
1. [Action]
2. [Action]
3. [Action]

Warnings
- [Important warning or missing information]
- [If there are no important warnings, write: None]

Keep the entire response under 250 words.
Do not add sections.
Do not add an introduction or conclusion.
""",

        agent=agent,

        context=[
            budgeting_task,
            debt_management_task,
            investment_task
        ]
    )