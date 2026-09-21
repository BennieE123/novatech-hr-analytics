import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NovaTech HR Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("NovaTech Industries — HR Analytics Dashboard")

st.markdown("""
### Workforce, Turnover, Compensation & Succession Insights

This dashboard analyzes NovaTech Industries' 1,000-employee workforce
across the United States, China, and Brazil to support decisions on
employee retention, compensation, and workforce planning.
""")

st.divider()

df = pd.read_csv("novatech_hr_cleaned.csv")
# st.write(df.columns.tolist())

df["Tenure Group"] = pd.cut(
    df["Tenure Years"],
    bins=[0, 2, 5, 10, 15, float("inf")],
    labels=["0-2", "3-5", "6-10", "11-15", "16+"],
    include_lowest=True
)

st.sidebar.header("Filters")
country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["Country"].unique().tolist())
)
department = st.sidebar.selectbox(
    "Select Department",
    ["All"] + sorted(df["Department"].unique().tolist())
)
gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + sorted(df["Gender"].unique().tolist())
)
filtered_df = df.copy()

if country != "All":
    filtered_df = filtered_df[filtered_df["Country"] == country]

if department != "All":
    filtered_df = filtered_df[filtered_df["Department"] == department]

if gender != "All":
    filtered_df = filtered_df[filtered_df["Gender"] == gender]

# st.write("Bonus values:")
# st.write(filtered_df["Bonus %"].head())

# bonus_by_department = (
#     filtered_df.groupby("Department")["Bonus %"]
#     .mean()
#     .mul(100)
#     .sort_values(ascending=False)
# )

# st.subheader("Average Bonus % by Department")
# st.bar_chart(bonus_by_department)

# st.write(df)
st.dataframe(filtered_df)
st.download_button(
    label="Download Filtered Employee Data",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="novatech_filtered_hr_data.csv",
    mime="text/csv"
)

turnover_rate = filtered_df["Turnover"].mean() * 100
average_salary = filtered_df["Annual Salary"].mean()
average_age = filtered_df["Age"].mean()
average_tenure = filtered_df["Tenure Years"].mean()

st.subheader("Key HR Metrics")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Employees", f"{len(filtered_df):,}")
col2.metric("Turnover Rate", f"{turnover_rate:.1f}%")
col3.metric("Average Salary", f"${average_salary:,.0f}")
col4.metric("Average Age", f"{average_age:.1f}")
col5.metric("Average Tenure", f"{average_tenure:.1f} years")

department_counts = df["Department"].value_counts()

st.subheader("Employees by Department")
st.bar_chart(department_counts)

st.subheader("Turnover Analysis")
turnover_by_department = (
    filtered_df.groupby("Department")["Turnover"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)
st.bar_chart(turnover_by_department)

turnover_by_gender = (
    filtered_df.groupby("Gender")["Turnover"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

st.subheader("Turnover by Gender")
st.bar_chart(turnover_by_gender)

turnover_by_country = (
    filtered_df.groupby("Country")["Turnover"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

st.subheader("Turnover by Country")
st.bar_chart(turnover_by_country)

turnover_by_tenure = (
    filtered_df.groupby("Tenure Group", observed=True)["Turnover"] 
    .mean()
    .mul(100)
)

st.subheader("Turnover by Tenure Group")
st.bar_chart(turnover_by_tenure)

hiring = filtered_df.groupby("Hire Year").size()

exits = (
    filtered_df.dropna(subset=["Exit Year"])
    .groupby("Exit Year")
    .size()
)

hiring_vs_exit = pd.concat(
    [hiring, exits],
    axis=1
).fillna(0)

hiring_vs_exit.columns = ["Hires", "Exits"]
hiring_vs_exit.index = hiring_vs_exit.index.astype(int)
st.subheader("Hiring vs Exit Trends")

st.line_chart(hiring_vs_exit)

hiring_vs_exit["Net Change"] = (
    hiring_vs_exit["Hires"] - hiring_vs_exit["Exits"]
)


st.subheader("Annual Net Workforce Change")

st.line_chart(hiring_vs_exit["Net Change"])

st.subheader("Compensation & Pay Equity")

salary_by_department = (
    filtered_df.groupby("Department")["Annual Salary"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(salary_by_department)
# st.write("TEST: Compensation section reached")

salary_by_gender = (
    filtered_df.groupby("Gender")["Annual Salary"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Salary by Gender")
st.bar_chart(salary_by_gender)

salary_by_country = (
    filtered_df.groupby("Country")["Annual Salary"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Salary by Country")
st.bar_chart(salary_by_country)

bonus_by_department = (
    filtered_df.groupby("Department")["Bonus %"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

st.subheader("Average Bonus % by Department")
st.bar_chart(bonus_by_department)

bonus_by_gender = (
    filtered_df.groupby("Gender")["Bonus %"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

st.subheader("Average Bonus % by Gender")
st.bar_chart(bonus_by_gender)

bonus_by_country = (
    filtered_df.groupby("Country")["Bonus %"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

st.subheader("Average Bonus % by Country")
st.bar_chart(bonus_by_country)

st.subheader("Workforce Aging & Succession Planning")

age_group_counts = (
    filtered_df["Age Group"]
    .value_counts()
    .sort_index()
)

st.subheader("Employees by Age Group")
st.bar_chart(age_group_counts)

employees_55_plus = (
    filtered_df[filtered_df["Age"] >= 55]
    .groupby("Department")
    .size()
    .sort_values(ascending=False)
)

st.subheader("Employees Aged 55+ by Department")
st.bar_chart(employees_55_plus)

age_55_pct = (
    filtered_df.groupby("Department")["Age"]
    .apply(lambda x: (x >= 55).mean() * 100)
    .sort_values(ascending=False)
)

st.subheader("Percentage of Employees Aged 55+ by Department")
st.bar_chart(age_55_pct)

# Senior and experienced employees by department
senior_experienced = (
    filtered_df[
        (filtered_df["Age"] >= 45) &
        (filtered_df["Tenure Years"] >= 11)
    ]
    .groupby("Department")
    .size()
    .sort_values(ascending=False)
)

st.subheader("Employees Aged 45+ with 11+ Years of Tenure")
st.bar_chart(senior_experienced)


# Average age by department
average_age_by_department = (
    filtered_df.groupby("Department")["Age"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Age by Department")
st.bar_chart(average_age_by_department)


# Average age by country
average_age_by_country = (
    filtered_df.groupby("Country")["Age"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Age by Country")
st.bar_chart(average_age_by_country)

st.subheader("Salary ANOVA Results — Full Dataset")

st.caption(
    "These ANOVA results are calculated using the complete 1,000-employee "
    "dataset and do not change with the dashboard filters."
)

anova_results = pd.DataFrame({
    "Grouping Variable": [
        "Department",
        "Gender",
        "Country"
    ],
    "F-statistic": [
        11.1188,
        4.7685,
        0.2829
    ],
    "p-value": [
        0.00000000002065,
        0.0292,
        0.7536
    ],
    "Significant": [
        "Yes",
        "Yes",
        "No"
    ]
})

st.dataframe(anova_results, hide_index=True)

st.subheader("Key Findings")

st.markdown("""
**1. Employee Turnover**
- Overall turnover rate is **10.3%**.
- Employees with **0–2 years of tenure have the highest turnover rate (20.9%)**.
- Human Resources, IT, and Finance have turnover rates above the company-wide rate.

**2. Compensation & Pay Equity**
- Salary differences are more pronounced across departments than across countries.
- Welch's ANOVA found significant salary differences by department (**p < 0.001**).
- A significant overall salary difference was also observed by gender (**p = 0.029**).
- Country-level salary differences were not statistically significant (**p = 0.754**).

**3. Workforce Aging**
- The average employee age is **44.4 years**.
- **52.1% of employees are aged 45 or older**.
- Employees aged 55+ are concentrated in several departments, creating a need for proactive succession and knowledge-transfer planning.
""")

st.subheader("HR Recommendations")

st.markdown("""
**1. Strengthen Early-Tenure Retention**
Focus onboarding, employee engagement, mentoring, and early-career development initiatives on employees within their first two years, where turnover is highest.

**2. Review Departmental Compensation Structures**
Conduct a structured review of salary bands, job levels, comparable roles, and bonus allocation across departments. Gender differences should be investigated using role- and seniority-adjusted comparisons rather than relying only on overall averages.

**3. Establish Succession and Knowledge-Transfer Plans**
Identify critical roles with experienced and long-tenured employees, introduce mentoring and cross-training, and document critical institutional knowledge to support workforce continuity.
""")

st.divider()

st.subheader("Business Decision")

st.markdown("""
Based on the analysis, NovaTech Industries should focus its HR strategy
on three interconnected priorities:

**1. Reduce early-tenure turnover**

Employees with 0–2 years of tenure recorded the highest turnover rate
at 20.90%. HR should therefore strengthen onboarding, mentoring,
employee engagement, and early-career development programs.

**2. Review compensation structures**

Salary differences are more pronounced across departments than across
countries. HR should review departmental salary bands, job levels,
comparable roles, and bonus allocation. The observed gender difference
should also be investigated using role, seniority, tenure, and
department-adjusted comparisons.

**3. Prepare for workforce succession**

More than half of the workforce is aged 45 or older. NovaTech should
strengthen succession planning, knowledge transfer, mentoring,
cross-training, and leadership development, particularly in departments
with larger concentrations of experienced employees.

### Overall Business Direction

NovaTech should adopt a proactive HR strategy that combines **retention,
compensation governance, and succession planning** rather than addressing
turnover as a single company-wide issue.
""")