# 🏥 Healthcare Patient Analytics — Data Visualization

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-teal)
![Internship](https://img.shields.io/badge/Thiranex-Internship-purple)
 
This project explores a healthcare patient analytics dataset using **Python, Matplotlib, and Seaborn** to uncover meaningful patterns in patient demographics, treatment types, costs, and readmission risks.

---

## 📁 Project Structure

```
Healthcare_Visualization/
│
├── healthcare.csv                    # Dataset (download from Kaggle)
├── visualization.py                  # Main Python script
│
├── chart1_gender_count.png           # Patient count by gender
├── chart2_age_group.png              # Age group distribution
├── chart3_department_visits.png      # Visits by department
├── chart4_treatment_type.png         # Treatment type pie chart
├── chart5_cost_by_department.png     # Treatment cost by department
├── chart6_recovery_vs_readmission.png# Recovery score vs readmission risk
│
└── README.md                         # Project documentation
```

---

## 📊 Dataset Overview

| Property | Value |
|----------|-------|
| **Source** | [Kaggle — Healthcare Patient Analytics](https://www.kaggle.com/datasets/abbas829/healthcare-patient-analytics-dataset) |
| **Rows** | 5,000 |
| **Columns** | 12 |
| **Domain** | Healthcare / Patient Analytics |

### Columns
| Column | Description |
|--------|-------------|
| `patient_id` | Unique patient identifier |
| `visit_date` | Date and time of hospital visit |
| `age_group` | Age bracket (18-30, 31-45, 46-60, 60+) |
| `gender` | Patient gender (Male / Female) |
| `region` | Geographic region (North, South, East, West) |
| `department` | Hospital department visited |
| `treatment_type` | Type of treatment received |
| `visit_type` | Emergency or Routine visit |
| `length_of_stay_days` | Duration of hospital stay (days) |
| `treatment_cost` | Total treatment cost ($) |
| `recovery_score` | Patient recovery score (0–100) |
| `readmission_risk` | Probability of readmission (0–1) |

---

## 📈 Visualizations

### Chart 1 — Patient Count by Gender
> Nearly equal distribution: **2,508 Male** and **2,492 Female** patients.

### Chart 2 — Patient Distribution by Age Group
> The **31–45** age group has the highest number of visits (1,716), followed by 18–30 (1,283).

### Chart 3 — Number of Visits by Department
> **Orthopedics** leads with 1,058 visits, followed closely by Cardiology, General Medicine, Pediatrics, and Neurology.

### Chart 4 — Treatment Type Distribution
> Treatments are fairly evenly distributed across Observation (25.4%), Surgery (25.2%), Medication (24.7%), and Therapy (24.6%).

### Chart 5 — Treatment Cost by Department
> Average treatment cost across all departments is **$54,915**. Cost spread is similar across departments with notable outliers in Surgery cases.

### Chart 6 — Recovery Score vs Readmission Risk
> A general trend shows that **higher recovery scores correlate with lower readmission risk**. Emergency visits tend to cluster at higher risk values.

---

## 🔍 Key Insights

- 🧑‍⚕️ Patient distribution is nearly **50-50 by gender**
- 👨‍💼 The **31–45 age group** is the most frequent hospital visitors
- 🏨 **Orthopedics** is the busiest department
- 💰 Average treatment cost is approximately **$54,915**
- 📉 Higher **recovery scores** are associated with lower **readmission risk**
- 🚨 **Emergency visits** carry significantly higher readmission risk than routine visits

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Pandas** — data loading and manipulation
- **Matplotlib** — base plotting
- **Seaborn** — statistical visualizations

---
