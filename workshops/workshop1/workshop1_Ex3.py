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
        taxes = 0.2 * 400_000 + 0.35 * (income - 700_000) 
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



def tax_numpy(incomes):
    lower_bracket_income = np.minimum(np.maximum(incomes - 300_000, 0), 400_000)
    Upper_bracket_income = np.maximum(incomes - 700_000, 0)

    taxes = 0.2 * lower_bracket_income + 0.35 * Upper_bracket_income
    return taxes

taxes_vectorized = tax_numpy(incomes)
net_income_vectorized = incomes - taxes_vectorized
net_income_loop = incomes - taxes_loop

taxes_agree = np.allclose(taxes_loop, taxes_vectorized)
net_incomes_agree = np.allclose(net_income_loop, net_income_vectorized)

print(f'Tax calculations agree: {taxes_agree}')
print(f'After-tax incomes agree: {net_incomes_agree}')