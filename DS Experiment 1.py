import pandas as pd

# Load the dataset
file_name = input("Enter Dataset Name: ")
df = pd.read_csv(file_name)

# Display first and last 10 records
print("\nFirst 10 Records:")
print(df.head(10))

print("\nLast 10 Records:")
print(df.tail(10))

# Display shape
print("\nShape of Dataset:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display duplicate records
print("\nDuplicate Records:")
print(df[df.duplicated()])

# Display memory usage
print("\nMemory Usage:")
print(df.memory_usage())

# Display unique values in each column
print("\nUnique Values:")
for column in df.columns:
    print(f"\n{column}:")
    print(df[column].unique())

# -----------------------------
# Identify inconsistent data
# -----------------------------

print("\nInconsistent Records:")

print("\nInvalid Age (should be between 17 and 30):")
print(df[(df["Age"] < 17) | (df["Age"] > 30)])

print("\nInvalid Entrance Exam Score (should be between 0 and 100):")
print(df[(df["Entrance_Exam_Score"] < 0) | (df["Entrance_Exam_Score"] > 100)])

print("\nInvalid Board Percentage (should be between 0 and 100):")
print(df[(df["Board_Percentage"] < 0) | (df["Board_Percentage"] > 100)])

# Admission statistics
print("\nAdmission Status Count:")
print(df["Admission_Status"].value_counts())

# Remove duplicate records
cleaned_df = df.drop_duplicates()

# Save cleaned dataset
cleaned_df.to_csv("UniversityAdmission_Cleaned.csv", index=False)

print("\nCleaned dataset saved as UniversityAdmission_Cleaned.csv")