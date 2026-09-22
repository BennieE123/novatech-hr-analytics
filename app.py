import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NovaTech HR Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.dashboard-title {
    font-size: 2.4rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
}

.dashboard-subtitle {
    font-size: 1.05rem;
    color: #5f6b7a;
    margin-bottom: 1.5rem;
}

div[data-testid="stMetric"] {
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 1rem;
    border-radius: 10px;
}

div[data-testid="stMetric"] label {
    color: #475569 !important;
}

div[data-testid="stMetricValue"] {
    color: #0f172a !important;
}

div[data-testid="stMetricDelta"] {
    color: #475569 !important;
}

section[data-testid="stSidebar"] {
    border-right: 1px solid #e2e8f0;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="dashboard-title">NovaTech Industries</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'HR Analytics & Workforce Intelligence Dashboard'
    '</div>',
    unsafe_allow_html=True
)

st.caption(
    "Workforce, turnover, compensation and succession insights "
    "across the United States, China and Brazil."
)

st.divider()

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

st.sidebar.title("Dashboard Filters")

st.sidebar.caption(
    "Use the filters below to explore workforce metrics."
)
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

    st.sidebar.divider()

st.sidebar.caption(
    "NovaTech Industries • HR Analytics"
)

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
with st.expander("📋 View Filtered Employee Data"):

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        label="⬇️ Download Filtered Employee Data",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="novatech_filtered_hr_data.csv",
        mime="text/csv"
    )

turnover_rate = filtered_df["Turnover"].mean() * 100
average_salary = filtered_df["Annual Salary"].mean()
average_age = filtered_df["Age"].mean()
average_tenure = filtered_df["Tenure Years"].mean()
st.header("Executive Overview")

st.caption(
    "High-level workforce indicators based on the selected filters."
)
# =========================================================
# DASHBOARD TABS
# =========================================================

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📊 Overview",
    "👥 Turnover",
    "📈 Workforce Trends",
    "💰 Compensation",
    "👴 Workforce Aging",
    "🔬 Statistical Analysis",
    "💡 Recommendations"
])


# =========================================================
# TAB 1 — OVERVIEW
# =========================================================

with tab1:

    # KPI CARDS
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Employees",
        f"{len(filtered_df):,}"
    )

    col2.metric(
        "Turnover Rate",
        f"{turnover_rate:.1f}%"
    )

    col3.metric(
        "Average Salary",
        f"${average_salary:,.0f}"
    )

    col4.metric(
        "Average Age",
        f"{average_age:.1f}"
    )

    col5.metric(
        "Average Tenure",
        f"{average_tenure:.1f} years"
    )

    st.divider()

    # EXECUTIVE SNAPSHOT
    st.subheader("Executive Snapshot")

    snapshot_col1, snapshot_col2, snapshot_col3 = st.columns(3)

    with snapshot_col1:

        st.markdown("### 👥 Workforce")

        st.write(
            f"NovaTech has **{len(filtered_df):,} employees** "
            f"within the selected filters, with an average age of "
            f"**{average_age:.1f} years**."
        )

    with snapshot_col2:

        st.markdown("### 🔄 Retention")

        st.write(
            f"The current turnover rate is **{turnover_rate:.1f}%**. "
            f"Turnover patterns can be explored in the Turnover tab."
        )

    with snapshot_col3:

        st.markdown("### 💰 Compensation")

        st.write(
            f"Average annual salary is **${average_salary:,.0f}**. "
            f"Detailed salary and bonus patterns are available "
            f"in the Compensation tab."
        )

    st.divider()

    # DEPARTMENT WORKFORCE
    st.subheader("Workforce Distribution")

    department_counts = (
        filtered_df["Department"]
        .value_counts()
        .sort_values(ascending=False)
    )

    st.bar_chart(department_counts)

    st.caption(
        "Number of employees within each department based on the selected filters."
    )


# =========================================================
# TAB 2 — TURNOVER
# =========================================================

with tab2:

    st.subheader("Employee Turnover Analysis")

    st.caption(
        "Explore turnover patterns across departments, gender, "
        "countries and employee tenure."
    )

    # Department and Gender
    col1, col2 = st.columns(2)

    with col1:

        turnover_by_department = (
            filtered_df.groupby("Department")["Turnover"]
            .mean()
            .mul(100)
            .sort_values(ascending=False)
        )

        st.markdown("### Turnover by Department")

        st.bar_chart(turnover_by_department)

        st.caption(
            "Percentage of employees who exited within each department."
        )

    with col2:

        turnover_by_gender = (
            filtered_df.groupby("Gender")["Turnover"]
            .mean()
            .mul(100)
            .sort_values(ascending=False)
        )

        st.markdown("### Turnover by Gender")

        st.bar_chart(turnover_by_gender)

        st.caption(
            "Percentage of employees who exited within each gender group."
        )

    st.divider()

    # Country and Tenure
    col3, col4 = st.columns(2)

    with col3:

        turnover_by_country = (
            filtered_df.groupby("Country")["Turnover"]
            .mean()
            .mul(100)
            .sort_values(ascending=False)
        )

        st.markdown("### Turnover by Country")

        st.bar_chart(turnover_by_country)

        st.caption(
            "Percentage of employees who exited within each country."
        )

    with col4:

        turnover_by_tenure = (
            filtered_df.groupby(
                "Tenure Group",
                observed=True
            )["Turnover"]
            .mean()
            .mul(100)
        )

        st.markdown("### Turnover by Tenure")

        st.bar_chart(turnover_by_tenure)

        st.caption(
            "Percentage of employees who exited within each tenure group."
        )

    st.divider()

    st.info(
        "Analytical note: turnover patterns identify associations "
        "within the dataset and do not establish causal relationships."
    )


# =========================================================
# TAB 3 — WORKFORCE TRENDS
# =========================================================

with tab3:

    st.subheader("Hiring & Exit Trends")

    st.caption(
        "Annual hiring and employee exit activity based on recorded "
        "hire and exit dates."
    )

    hiring = (
        filtered_df
        .groupby("Hire Year")
        .size()
    )

    exits = (
        filtered_df
        .dropna(subset=["Exit Year"])
        .groupby("Exit Year")
        .size()
    )

    hiring_vs_exit = pd.concat(
        [hiring, exits],
        axis=1
    ).fillna(0)

    hiring_vs_exit.columns = [
        "Hires",
        "Exits"
    ]

    hiring_vs_exit.index = (
        hiring_vs_exit.index
        .astype(int)
    )

    st.line_chart(hiring_vs_exit)

    st.caption(
        "Recorded hires and exits by year."
    )

    st.divider()

    hiring_vs_exit["Net Change"] = (
        hiring_vs_exit["Hires"]
        - hiring_vs_exit["Exits"]
    )

    st.subheader("Annual Net Workforce Change")

    st.line_chart(
        hiring_vs_exit["Net Change"]
    )

    st.caption(
        "Annual hires minus recorded exits. This represents "
        "recorded workforce activity and should not be interpreted "
        "as exact annual headcount growth."
    )


# =========================================================
# TAB 4 — COMPENSATION
# =========================================================

with tab4:

    st.subheader("Compensation & Pay Equity")

    st.caption(
        "Explore salary and bonus differences across departments, "
        "gender groups and countries."
    )

    # Salary analysis
    st.markdown("### Salary Analysis")

    col1, col2 = st.columns(2)

    with col1:

        salary_by_department = (
            filtered_df
            .groupby("Department")["Annual Salary"]
            .mean()
            .sort_values(ascending=False)
        )

        st.markdown("#### Average Salary by Department")

        st.bar_chart(
            salary_by_department
        )

    with col2:

        salary_by_gender = (
            filtered_df
            .groupby("Gender")["Annual Salary"]
            .mean()
            .sort_values(ascending=False)
        )

        st.markdown("#### Average Salary by Gender")

        st.bar_chart(
            salary_by_gender
        )

    salary_by_country = (
        filtered_df
        .groupby("Country")["Annual Salary"]
        .mean()
        .sort_values(ascending=False)
    )

    st.markdown("#### Average Salary by Country")

    st.bar_chart(
        salary_by_country
    )

    st.divider()

    # Bonus analysis
    st.markdown("### Bonus Analysis")

    col3, col4 = st.columns(2)

    with col3:

        bonus_by_department = (
            filtered_df
            .groupby("Department")["Bonus %"]
            .mean()
            .mul(100)
            .sort_values(ascending=False)
        )

        st.markdown("#### Average Bonus by Department")

        st.bar_chart(
            bonus_by_department
        )

    with col4:

        bonus_by_gender = (
            filtered_df
            .groupby("Gender")["Bonus %"]
            .mean()
            .mul(100)
            .sort_values(ascending=False)
        )

        st.markdown("#### Average Bonus by Gender")

        st.bar_chart(
            bonus_by_gender
        )

    bonus_by_country = (
        filtered_df
        .groupby("Country")["Bonus %"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )

    st.markdown("#### Average Bonus by Country")

    st.bar_chart(
        bonus_by_country
    )

    st.info(
        "Analytical note: differences in average compensation do not "
        "by themselves establish pay discrimination. Role, seniority, "
        "tenure and department should be considered when evaluating pay equity."
    )


# =========================================================
# TAB 5 — WORKFORCE AGING
# =========================================================

with tab5:

    st.subheader("Workforce Aging & Succession Planning")

    st.caption(
        "Assess workforce age structure and identify areas requiring "
        "succession and knowledge-transfer planning."
    )

    # Age distribution
    st.markdown("### Age Distribution")

    age_group_counts = (
        filtered_df["Age Group"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(
        age_group_counts
    )

    st.divider()

    # 55+ analysis
    col1, col2 = st.columns(2)

    with col1:

        employees_55_plus = (
            filtered_df[
                filtered_df["Age"] >= 55
            ]
            .groupby("Department")
            .size()
            .sort_values(ascending=False)
        )

        st.markdown("### Employees Aged 55+ by Department")

        st.bar_chart(
            employees_55_plus
        )

    with col2:

        age_55_pct = (
            filtered_df
            .groupby("Department")["Age"]
            .apply(
                lambda x:
                (x >= 55).mean() * 100
            )
            .sort_values(ascending=False)
        )

        st.markdown("### Percentage Aged 55+")

        st.bar_chart(
            age_55_pct
        )

    st.divider()

    # Experienced workforce
    senior_experienced = (
        filtered_df[
            (filtered_df["Age"] >= 45) &
            (filtered_df["Tenure Years"] >= 11)
        ]
        .groupby("Department")
        .size()
        .sort_values(ascending=False)
    )

    st.markdown(
        "### Employees Aged 45+ with 11+ Years of Tenure"
    )

    st.bar_chart(
        senior_experienced
    )

    st.caption(
        "This group represents employees with both substantial "
        "organizational experience and longer tenure."
    )

    st.divider()

    # Average age
    col3, col4 = st.columns(2)

    with col3:

        average_age_by_department = (
            filtered_df
            .groupby("Department")["Age"]
            .mean()
            .sort_values(ascending=False)
        )

        st.markdown("### Average Age by Department")

        st.bar_chart(
            average_age_by_department
        )

    with col4:

        average_age_by_country = (
            filtered_df
            .groupby("Country")["Age"]
            .mean()
            .sort_values(ascending=False)
        )

        st.markdown("### Average Age by Country")

        st.bar_chart(
            average_age_by_country
        )


# =========================================================
# TAB 6 — STATISTICAL ANALYSIS
# =========================================================

with tab6:

    st.subheader("Salary Statistical Analysis")

    st.caption(
        "Statistical tests are based on the complete 1,000-employee "
        "dataset and are independent of the dashboard filters."
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

    st.dataframe(
        anova_results,
        hide_index=True,
        use_container_width=True
    )

    st.divider()

    st.markdown("### Interpretation")

    st.markdown("""
    **Department:** Salary differences across departments are statistically
    significant (Welch's ANOVA, p < 0.001).

    **Gender:** The overall salary difference between gender groups is
    statistically significant (Welch's ANOVA, p = 0.029).

    **Country:** Salary differences across countries are not statistically
    significant (ANOVA, p = 0.754).
    """)

    st.divider()

    with st.expander("📚 Statistical Methodology"):

        st.write(
            "Welch's ANOVA was used for department and gender comparisons "
            "because Levene's test indicated unequal salary variances. "
            "Standard one-way ANOVA was retained for country because there "
            "was no evidence of unequal variances."
        )

        st.write(
            "Statistical significance does not establish causation. "
            "Observed salary differences should be investigated further "
            "using factors such as job role, seniority and tenure."
        )


# =========================================================
# TAB 7 — RECOMMENDATIONS
# =========================================================

with tab7:

    st.subheader("Key Findings & HR Recommendations")

    # Key findings
    st.markdown("### Key Findings")

    finding_col1, finding_col2, finding_col3 = st.columns(3)

    with finding_col1:

        st.markdown("#### 🔄 Turnover")

        st.write(
            "Overall turnover is 10.3%, with employees in the "
            "0–2 year tenure group recording the highest turnover "
            "rate at 20.90%."
        )

    with finding_col2:

        st.markdown("#### 💰 Compensation")

        st.write(
            "Salary variation is more pronounced across departments "
            "than across countries. Department and gender differences "
            "were statistically significant."
        )

    with finding_col3:

        st.markdown("#### 👴 Workforce Aging")

        st.write(
            "52.1% of employees are aged 45 or older, creating a need "
            "for proactive succession and knowledge-transfer planning."
        )

    st.divider()

    # Recommendations
    st.markdown("### HR Recommendations")

    st.markdown("""
    **1. Strengthen Early-Tenure Retention**

    Focus onboarding, mentoring, employee engagement and early-career
    development initiatives on employees within their first two years,
    where turnover is highest.

    **2. Review Departmental Compensation Structures**

    Conduct a structured review of salary bands, job levels, comparable
    roles and bonus allocation across departments. Gender differences
    should be investigated using role- and seniority-adjusted comparisons.

    **3. Establish Succession and Knowledge-Transfer Plans**

    Identify critical roles with experienced and long-tenured employees.
    Introduce mentoring, cross-training and knowledge documentation to
    support workforce continuity.
    """)

    st.divider()

    # Business decision
    st.markdown("### Business Decision")

    st.success(
        "NovaTech should prioritize three interconnected HR strategies: "
        "reducing early-tenure turnover, strengthening compensation "
        "governance and preparing for workforce succession."
    )

    st.write(
        "The analysis suggests that turnover should not be treated as a "
        "single company-wide problem. HR should target early-tenure "
        "retention while simultaneously addressing departmental "
        "compensation structures and long-term workforce continuity."
    )

    st.divider()

    # Methodology
    with st.expander("📚 Dashboard Methodology"):

        st.write(
            "The dashboard is based on 1,000 employee records covering "
            "the United States, China and Brazil."
        )

        st.write(
            "Turnover rate is calculated as the percentage of employees "
            "with a Turnover indicator of 1."
        )

        st.write(
            "Salary and bonus analyses use employee-level compensation "
            "data. Workforce aging analysis uses employee age and tenure."
        )

        st.write(
            "Statistical analysis uses ANOVA, Welch's ANOVA and post-hoc "
            "testing where appropriate."
        )

        st.write(
            "Findings represent associations within the dataset and "
            "should not automatically be interpreted as causal effects."
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "NovaTech Industries • HR Analytics & Workforce Intelligence Dashboard"
)

st.caption(
    "Prepared for HR leadership | Data-driven workforce insights "
    "across the United States, China and Brazil"
)
