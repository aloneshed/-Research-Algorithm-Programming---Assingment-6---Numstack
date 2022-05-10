import pandas as pd
import openpyxl

df = pd.read_csv('national-budget.csv')


def office_budget_by_year(office: str, year: int) -> int:
    relative_df = df.loc[(df['שם סעיף'] == office) & (df['שנה'] == year)]
    total_office_budget = relative_df['הוצאה נטו'].sum(axis=0)
    return total_office_budget


def education_budget(year: int) -> int:
    education_df = df.loc[(df['שם סעיף'] == 'משרד החינוך') & (df['שנה'] == year)]
    total_education_budget = education_df['הוצאה נטו'].sum(axis=0)
    print(total_education_budget)
    return total_education_budget


def security_budget_ratio(year: int) -> float:
    security_df = df.loc[(df['שם סעיף'] == 'משרד הבטחון') & (df['שנה'] == year)]
    total_security_budget = security_df['הוצאה נטו'].sum(axis=0)
    year_df = df.loc[df['שנה'] == year]
    total_year_budget = year_df['הוצאה נטו'].sum(axis=0)
    print(total_security_budget / total_year_budget)
    return total_security_budget / total_year_budget


def largest_budget_year(office: str) -> int:
    budget_list = []
    budget_by_year_df = pd.DataFrame()
    budget_by_year_df['year'] = [i for i in range(1997, 2023)]
    for index, row in budget_by_year_df.iterrows():
        budget_list.append(office_budget_by_year(office, row['year']))

    budget_by_year_df['bugdet'] = budget_list
    print(budget_by_year_df)

largest_budget_year("משרד החינוך")
