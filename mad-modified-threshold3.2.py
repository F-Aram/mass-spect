import pandas as pd
import numpy as np

# Define file path
file_path = r'C:\Users\aram\Desktop\ms data analysis python\ms wt nondiff.xlsx'

# Load the Excel file
df = pd.read_excel(file_path)

# Ensure columns are numeric (convert non-numeric to NaN), skipping the first column (protein names)
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Define MAD threshold for outlier detection (typically 3 * MAD)
mad_threshold = 3.2

# Function to detect outliers based on MAD (for each row)
def detect_outliers_mad_rowwise(row):
    median_value = np.median(row)  # Calculate median
    abs_deviations = np.abs(row - median_value)  # Absolute deviations from median
    mad = np.median(abs_deviations)  # Calculate MAD

    # Avoid division by zero if MAD is 0
    if mad == 0:
        return pd.Series([False] * len(row), index=row.index)

    modified_z_scores = 0.6745 * abs_deviations / mad  # Compute Modified Z-score
    outlier_flags = modified_z_scores > mad_threshold  # Flag outliers

    return outlier_flags

# Apply the outlier detection for each row (axis=1)
outlier_flags = df.iloc[:, 1:].apply(detect_outliers_mad_rowwise, axis=1)

# Add new columns for outlier flags
outlier_flags = outlier_flags.add_prefix('Outlier_')

# Combine original data with outlier flags
df_with_flags = pd.concat([df, outlier_flags], axis=1)

# Save the dataframe to a new Excel file
output_file = r'C:\Users\aram\Desktop\ms data analysis python\ms_mad_modified_outliers_rowwise_final.xlsx'
df_with_flags.to_excel(output_file, index=False)

print(f"Outlier detection using MAD (row-wise) complete. Results saved to: {output_file}")
