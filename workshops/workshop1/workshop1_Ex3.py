import numpy as np

def tax(income):
    """
    Return the taxes ownd for a given income

    Parameters
    ----------
    income
        gross income

    Returns
    -------
    Tax owned
    """

  
    if income > 700_000:
        taxes = 0.35 * (income - 300_000) 
    elif income > 300_000:
        taxes = 0.2 * (income - 300_000)
    else:
        taxes = 0
    return taxes

incomes = np.linspace(0, 1_200_000, 13)


taxes_loop = []

for income in incomes:
    taxes = tax(income)
  
    taxes_loop.append(taxes)
  
    net_income = income - taxes

    print(f'Gross income: {income:10.0f}; '
        f'Taxes: {taxes:10.0f}; ' 
        f'Net income {net_income:10.0f}')