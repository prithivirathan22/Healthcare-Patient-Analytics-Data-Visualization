import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ── Global Style ─────────────────────────────────────────────
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

# ── Load Dataset ─────────────────────────────────────────────
df = pd.read_csv("healthcare.csv")
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

print("✅ Dataset loaded successfully!")
print(f"   Rows: {df.shape[0]}  |  Columns: {df.shape[1]}\n")

# ============================================================
# CHART 1 — Patient Count by Gender (Count Plot)
# ============================================================
plt.figure(figsize=(7, 5))
ax = sns.countplot(x="gender", data=df, palette="Set2",
                   order=df["gender"].value_counts().index)
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=12, fontweight='bold')
plt.title("Patient Count by Gender", fontsize=14, fontweight='bold')
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.savefig("chart1_gender_count.png", dpi=150)
plt.show()
print("✅ Chart 1 saved: chart1_gender_count.png")

# ============================================================
# CHART 2 — Patient Distribution by Age Group (Bar Chart)
# ============================================================
plt.figure(figsize=(8, 5))
age_order = ["18-30", "31-45", "46-60", "60+"]
ax = sns.countplot(x="age_group", data=df, palette="Blues_d", order=age_order)
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=11, fontweight='bold')
plt.title("Patient Distribution by Age Group", fontsize=14, fontweight='bold')
plt.xlabel("Age Group")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.savefig("chart2_age_group.png", dpi=150)
plt.show()
print("✅ Chart 2 saved: chart2_age_group.png")

# ============================================================
# CHART 3 — Visits by Department (Horizontal Bar Chart)
# ============================================================
plt.figure(figsize=(9, 5))
dept_counts = df["department"].value_counts()
sns.barplot(x=dept_counts.values, y=dept_counts.index, palette="Set3")
plt.title("Number of Visits by Department", fontsize=14, fontweight='bold')
plt.xlabel("Number of Visits")
plt.ylabel("Department")
plt.tight_layout()
plt.savefig("chart3_department_visits.png", dpi=150)
plt.show()
print("✅ Chart 3 saved: chart3_department_visits.png")

# ============================================================
# CHART 4 — Treatment Type Distribution (Pie Chart)
# ============================================================
plt.figure(figsize=(7, 6))
counts = df["treatment_type"].value_counts()
colors = sns.color_palette("pastel", len(counts))
plt.pie(counts, labels=counts.index, autopct="%1.1f%%",
        colors=colors, startangle=140,
        wedgeprops=dict(edgecolor='white', linewidth=2))
plt.title("Treatment Type Distribution", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig("chart4_treatment_type.png", dpi=150)
plt.show()
print("✅ Chart 4 saved: chart4_treatment_type.png")

# ============================================================
# CHART 5 — Treatment Cost by Department (Box Plot)
# ============================================================
plt.figure(figsize=(11, 5))
sns.boxplot(x="department", y="treatment_cost", data=df, palette="muted")
plt.title("Treatment Cost by Department", fontsize=14, fontweight='bold')
plt.xlabel("Department")
plt.ylabel("Treatment Cost ($)")
plt.xticks(rotation=20, ha='right')
plt.tight_layout()
plt.savefig("chart5_cost_by_department.png", dpi=150)
plt.show()
print("✅ Chart 5 saved: chart5_cost_by_department.png")

# ============================================================
# CHART 6 — Recovery Score vs Readmission Risk (Scatter Plot)
# ============================================================
plt.figure(figsize=(9, 5))
sns.scatterplot(x="recovery_score", y="readmission_risk",
                hue="visit_type", data=df,
                palette="Set1", alpha=0.6)
plt.title("Recovery Score vs Readmission Risk", fontsize=14, fontweight='bold')
plt.xlabel("Recovery Score")
plt.ylabel("Readmission Risk")
plt.legend(title="Visit Type")
plt.tight_layout()
plt.savefig("chart6_recovery_vs_readmission.png", dpi=150)
plt.show()
print("✅ Chart 6 saved: chart6_recovery_vs_readmission.png")

# ============================================================
# DONE
# ============================================================
print("\n🎉 All 6 charts generated and saved successfully!")
print("📁 Files saved in your project folder:")
for c in [
    "chart1_gender_count.png",
    "chart2_age_group.png",
    "chart3_department_visits.png",
    "chart4_treatment_type.png",
    "chart5_cost_by_department.png",
    "chart6_recovery_vs_readmission.png"
]:
    print(f"   ✅ {c}")
