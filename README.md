\# NovaTech Industries — HR Analytics \& Workforce Intelligence Dashboard



\## Project Overview



This project presents an HR analytics solution developed for \*\*NovaTech Industries\*\*, a multinational organization with employees across the \*\*United States, China, and Brazil\*\*.



The project analyzes employee workforce data to help management understand \*\*employee turnover, workforce trends, compensation patterns, and workforce aging\*\*. The analysis combines exploratory data analysis, statistical testing, and an interactive \*\*Streamlit dashboard\*\* to transform HR data into actionable business insights.



The goal is to support data-driven decisions around \*\*employee retention, compensation planning, workforce succession, and organizational planning\*\*.



\---



\## Business Problem



NovaTech Industries wants to better understand its workforce and identify areas that may require management attention.



Key questions addressed include:



\* What is the overall employee turnover rate?

\* Which departments and countries have the highest turnover?

\* Is employee tenure associated with turnover?

\* How do hiring and employee exits change over time?

\* How does compensation vary across departments, countries, and genders?

\* Are observed salary differences statistically significant?

\* What does the age distribution suggest about future workforce planning?

\* Where should management prioritize retention and succession efforts?



\---



\## Project Objectives



The analysis was designed to:



1\. Measure and understand employee turnover.

2\. Identify departments and employee groups with higher turnover.

3\. Analyze hiring and exit trends over time.

4\. Examine employee compensation patterns.

5\. Test whether salary differences across groups are statistically significant.

6\. Analyze workforce age and tenure distributions.

7\. Identify potential workforce succession risks.

8\. Provide practical recommendations for HR and management.

9\. Present the findings through an interactive Streamlit dashboard.



\---



\## Dataset



The dataset contains \*\*1,000 employee records\*\* covering employees across:



\* United States

\* China

\* Brazil



The dataset includes employee information such as:



\* Job

\* Department

\* Business Unit

\* Gender

\* Age

\* Hire Date

\* Salary

\* Bonus

\* Country

\* City

\* Exit Date

\* Tenure



The cleaned dataset used by the dashboard is:



`novatech\_hr\_cleaned.csv`



\---



\## Key Analysis Areas



\### 1. Workforce Overview



The dashboard provides an overview of the organization's workforce, including:



\* Total employees

\* Turnover rate

\* Average salary

\* Average age

\* Average tenure



Users can filter the analysis by:



\* Country

\* Department

\* Gender



\---



\### 2. Employee Turnover Analysis



Turnover was analyzed across different employee characteristics, including:



\* Tenure

\* Department

\* Gender

\* Country



The analysis identified substantial differences in turnover across employee groups.



\### Key Finding



The overall employee turnover rate was:



\*\*10.3%\*\*



Employees with \*\*0–2 years of tenure\*\* had a turnover rate of approximately:



\*\*20.90%\*\*



In comparison, employees with \*\*16+ years of tenure\*\* had a turnover rate of approximately:



\*\*3.17%\*\*



This suggests that early-tenure employees represent an important area for retention efforts.



\---



\## 3. Department Turnover



Turnover varied considerably across departments.



| Department  | Turnover Rate |

| ----------- | ------------: |

| HR          |        13.76% |

| IT          |        12.64% |

| Finance     |        12.24% |

| Accounting  |        11.30% |

| Engineering |         9.93% |

| Sales       |         6.00% |

| Marketing   |         4.55% |



HR had the highest observed turnover rate, while Marketing had the lowest among the departments analyzed.



\---



\## 4. Geographic Turnover



Turnover also varied across countries.



| Country       | Turnover Rate |

| ------------- | ------------: |

| United States |        11.51% |

| Brazil        |         8.63% |

| China         |         7.93% |



The United States recorded the highest turnover rate among the three countries.



\---



\## 5. Compensation Analysis



The project examined salary differences across:



\* Departments

\* Countries

\* Gender



The average salary observed for female employees was approximately:



\*\*$112,903.53\*\*



The average salary observed for male employees was approximately:



\*\*$105,520.23\*\*



These descriptive differences should not automatically be interpreted as evidence of discrimination because salary can also be influenced by factors such as job, seniority, department, experience, and tenure.



\---



\## 6. Statistical Analysis



Statistical testing was used to determine whether observed salary differences between groups were statistically significant.



\### Department



\* F-statistic: \*\*11.1188\*\*

\* p-value: \*\*2.065 × 10⁻¹¹\*\*

\* Result: \*\*Statistically significant\*\*



\### Gender



\* F-statistic: \*\*4.7685\*\*

\* p-value: \*\*0.0292\*\*

\* Result: \*\*Statistically significant\*\*



\### Country



\* F-statistic: \*\*0.2829\*\*

\* p-value: \*\*0.7536\*\*

\* Result: \*\*Not statistically significant\*\*



Welch's ANOVA was used for groups where unequal salary variances were identified, while standard one-way ANOVA was used where there was no evidence of unequal variances.



\---



\## 7. Workforce Aging



Workforce age distribution was analyzed to support future workforce planning and succession management.



The employee distribution included:



| Age Group | Employees |

| --------- | --------: |

| 25–34     |       249 |

| 35–44     |       230 |

| 45–54     |       291 |

| 55–65     |       230 |



Approximately \*\*52.1% of employees were aged 45 or older\*\*, highlighting the importance of succession planning, knowledge transfer, and workforce continuity.



\---



\## Dashboard



The project includes an interactive Streamlit dashboard with the following sections:



\### Overview



Provides high-level workforce KPIs and employee summaries.



\### Turnover



Explores employee turnover across tenure, department, gender, and country.



\### Workforce Trends



Analyzes hiring and employee exit trends over time.



\### Compensation



Examines salary patterns across departments, countries, and genders.



\### Workforce Aging



Provides insights into employee age distribution and potential succession considerations.



\### Statistical Analysis



Presents statistical tests examining salary differences across employee groups.



\### Recommendations



Translates the analytical findings into practical HR recommendations.



\---



\## Key Recommendations



Based on the analysis, the project recommends that NovaTech Industries:



\### 1. Strengthen Early-Tenure Retention



Employees in their first two years have substantially higher turnover than long-tenured employees.



Management should consider:



\* Structured onboarding

\* Early-career mentorship

\* Regular employee check-ins

\* Career development opportunities

\* Early identification of disengagement



\### 2. Review Departmental Compensation Structures



Salary differences across departments were statistically significant.



HR should review compensation structures while considering:



\* Job responsibilities

\* Seniority

\* Experience

\* Tenure

\* Role complexity

\* Market salary benchmarks



\### 3. Strengthen Succession Planning



With more than half of the workforce aged 45 or older, NovaTech should proactively plan for:



\* Knowledge transfer

\* Leadership succession

\* Critical-role backups

\* Mentorship programs

\* Workforce continuity



\### 4. Monitor High-Turnover Departments



Departments with relatively high turnover should receive additional investigation to understand potential contributing factors and identify appropriate retention strategies.



\---



\## Tools \& Technologies



The project was developed using:



\* \*\*Python\*\*

\* \*\*Pandas\*\*

\* \*\*Streamlit\*\*

\* \*\*Statistical Analysis\*\*

\* \*\*Data Visualization\*\*

\* \*\*Exploratory Data Analysis\*\*



The interactive dashboard was built with \*\*Streamlit\*\* to make the analysis easier for HR and management stakeholders to explore.



\---



\## Project Structure



```text

NovaTech-HR-Analytics/

│

├── app.py

├── novatech\_hr\_cleaned.csv

├── README.md

└── requirements.txt

```



\---



\## How to Run the Dashboard Locally



\### 1. Clone the repository



```bash

git clone <your-github-repository-url>

```



\### 2. Navigate to the project folder



```bash

cd NovaTech-HR-Analytics

```



\### 3. Install the required packages



```bash

pip install -r requirements.txt

```



\### 4. Run the Streamlit application



```bash

streamlit run app.py

```



The dashboard will open in your web browser.



\---



\## Analytical Notes \& Limitations



\* The analysis identifies \*\*associations and patterns\*\* in the workforce data; it does not establish causation.

\* Salary differences do not by themselves establish discrimination.

\* Additional variables such as job level, experience, performance, and tenure should be considered when conducting a deeper compensation-equity investigation.

\* Statistical results presented in the dashboard are based on the underlying analysis and are not recalculated dynamically when dashboard filters are changed.

\* Hiring and exit trends describe recorded workforce activity and should not automatically be interpreted as exact changes in total organizational headcount.



\---



\## Project Outcome



This project demonstrates how HR data can be transformed into an interactive decision-support solution.



The final solution combines:



\*\*Data Analysis → Statistical Testing → Visualization → Business Insights → Recommendations\*\*



The dashboard enables HR and management stakeholders to explore workforce patterns and identify areas requiring attention, particularly around \*\*early-tenure turnover, departmental compensation, and workforce succession planning\*\*.



\---



\## Author



\*\*Benjamin Happiness\*\*



Data Analyst | Excel | SQL | Power BI | Python | Machine Learning



This project is part of my data analytics portfolio and demonstrates practical application of data analysis, statistical reasoning, visualization, and business decision-making.



