import pandas as pd
import openpyxl

"""
sources:
https://www.youtube.com/watch?v=vmEHCJofslg
"""

df = pd.read_csv('national-budget.csv') # read the csv file


# Helper function that get office name and year and return the total budget of the year
def office_budget_by_year(office: str, year: int) -> float:
    relative_df = df.loc[(df['שם סעיף'] == office) & (df['שנה'] == year)]
    total_office_budget = relative_df['הוצאה נטו'].sum(axis=0)
    return total_office_budget

# Query 1
def education_budget(year: int) -> float:
    education_df = df.loc[(df['שם סעיף'] == 'משרד החינוך') & (df['שנה'] == year)] # filter the dataframe for education office and specific year
    total_education_budget = education_df['הוצאה נטו'].sum(axis=0) # sum the column expenditure
    print(total_education_budget)
    return total_education_budget

# Query 2
def security_budget_ratio(year: int) -> float:
    security_df = df.loc[(df['שם סעיף'] == 'משרד הבטחון') & (df['שנה'] == year)] # filter the dataframe for security office and specific year
    total_security_budget = security_df['הוצאה נטו'].sum(axis=0) # sum the column expenditure
    year_df = df.loc[df['שנה'] == year] # filter the dataframe for specific year
    total_year_budget = year_df['הוצאה נטו'].sum(axis=0) # sum the total budget of specific year
    print(total_security_budget / total_year_budget)
    return total_security_budget / total_year_budget # return the security budget as a percentage of the total budget

# Query 3
def largest_budget_year(office: str) -> int:
    budget_list = []
    budget_by_year_df = pd.DataFrame()
    budget_by_year_df['year'] = [i for i in range(1997, 2023)]
    for index, row in budget_by_year_df.iterrows():
        budget_list.append(office_budget_by_year(office, row['year']))

    budget_by_year_df['bugdet'] = budget_list
    print(budget_by_year_df)


# Query 4
def ministry_of_Health_expenditure(year: int) -> float:
    relative_df = df.loc[(df['שם סעיף'] == "משרד הבריאות") & (df['שנה'] == year) & (df["הוצאה/הכנסה"] == "הוצאה")]
    total_office_budget = relative_df['הוצאה נטו'].sum(axis=0)
    return total_office_budget


# largest_budget_year("משרד החינוך")
# print(office_budget_by_year("משרד הבריאות", 2007))
# education_budget(2007)
# print(ministry_of_Health_expenditure(2007))