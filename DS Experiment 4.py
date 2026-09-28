import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
data = {
    "Patient_ID": range(1, 16),

    "Hospital": [
        "Apollo", "Fortis", "AIIMS", "Apollo", "Fortis",
        "AIIMS", "Apollo", "Fortis", "AIIMS", "Apollo",
        "Fortis", "AIIMS", "Apollo", "Fortis", "AIIMS"
    ],

    "Age": [
        25, 45, 60, 35, 50,
        42, 38, 55, 65, 70,
        48, 33, 28, 75, 90
    ],

    "Blood_Pressure": [
        120, 135, 180, 128, 140,
        130, 125, 145, 190, 135,
        138, 126, 124, 200, 250
    ],

    "Sugar_Level": [
        90, 110, 180, 95, 130,
        120, 100, 140, 250, 115,
        118, 105, 98, 260, 400
    ],

    "Heart_Rate": [
        72, 80, 95, 75, 82,
        78, 74, 85, 100, 76,
        79, 73, 71, 105, 140
    ]
}

df = pd.DataFrame(data)

print("=" * 60)
print("PATIENT HEALTH DATA")
print("=" * 60)
print(df)
print("\n================ DESCRIPTIVE STATISTICS ================\n")

print(df.describe())
print("\n================ PATIENT DISTRIBUTION ================\n")

hospital_count = df["Hospital"].value_counts()

print(hospital_count)

mean_patients = hospital_count.mean()

print("\nHospitals with Abnormal Patient Distribution")

for hospital, count in hospital_count.items():

    if count > mean_patients:
        print(f"{hospital} : Higher than average")

    elif count < mean_patients:
        print(f"{hospital} : Lower than average")

    else:
        print(f"{hospital} : Average")
        # ============================================================
        # Outlier Detection using IQR
        # ============================================================

        print("\n================ IQR OUTLIER DETECTION ================\n")

        Q1 = df[["Blood_Pressure", "Sugar_Level", "Heart_Rate"]].quantile(0.25)
        Q3 = df[["Blood_Pressure", "Sugar_Level", "Heart_Rate"]].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers_iqr = df[
            ((df[["Blood_Pressure", "Sugar_Level", "Heart_Rate"]] < lower) |
             (df[["Blood_Pressure", "Sugar_Level", "Heart_Rate"]] > upper)).any(axis=1)
        ]

        print(outliers_iqr)
        # ============================================================
        # Outlier Detection using Z-Score
        # ============================================================

        print("\n================ Z-SCORE OUTLIER DETECTION ================\n")

        z_scores = np.abs(zscore(df[["Blood_Pressure", "Sugar_Level", "Heart_Rate"]]))

        outliers_z = df[(z_scores > 3).any(axis=1)]

        print(outliers_z)
        # ============================================================
        # Correlation Analysis
        # ============================================================

        print("\n================ CORRELATION MATRIX ================\n")

        correlation = df[["Age", "Blood_Pressure", "Sugar_Level", "Heart_Rate"]].corr()

        print(correlation)
        # ============================================================
        # Histogram
        # ============================================================

        plt.figure(figsize=(6, 4))
        plt.hist(df["Sugar_Level"], bins=8)

        plt.title("Sugar Level Distribution")
        plt.xlabel("Sugar Level")
        plt.ylabel("Frequency")

        plt.show()
        # ============================================================
        # Box Plot
        # ============================================================

        plt.figure(figsize=(6, 4))
        sns.boxplot(y=df["Blood_Pressure"])

        plt.title("Blood Pressure Box Plot")
        plt.show()
        # ============================================================
        # Scatter Plot
        # ============================================================

        plt.figure(figsize=(6, 4))

        plt.scatter(df["Age"], df["Blood_Pressure"])

        plt.title("Age vs Blood Pressure")
        plt.xlabel("Age")
        plt.ylabel("Blood Pressure")

        plt.show()
        # ============================================================
        # Correlation Heatmap
        # ============================================================

        plt.figure(figsize=(6, 5))

        sns.heatmap(
            correlation,
            annot=True,
            cmap="coolwarm"
        )

        plt.title("Correlation Heatmap")

        plt.show()
        # ============================================================
        # Analytical Observations
        # ============================================================

        print("\n================ ANALYTICAL OBSERVATIONS ================\n")

        print("1. Descriptive statistics summarize patient health data.")
        print("2. Hospital-wise distribution identifies patient load.")
        print("3. IQR detects abnormal health values.")
        print("4. Z-Score identifies extreme outliers.")
        print("5. Correlation shows relationships among health parameters.")
        print("6. Histogram displays the sugar level distribution.")
        print("7. Box plot highlights blood pressure outliers.")
        print("8. Scatter plot shows the relationship between age and blood pressure.")
        print("9. Heatmap visualizes feature correlations.")
        print("10. These analyses help monitor patient health effectively.")
        
