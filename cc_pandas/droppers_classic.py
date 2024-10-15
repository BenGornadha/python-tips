import pandas as pd

# Exemple d'un DataFrame avec des valeurs manquantes
df = pd.DataFrame({
    "First Name": ["Alice", "Bob", None],
    "Last Name": ["Smith", None, "Williams"],
    "Age in Years": [25, None, None],
    "Email Address": [None, "bob@example.com", "charlie@example.com"],
    "Phone Number": ["555-1234", None, "555-9876"]
})

# Drop des colonnes qui ont plus de 50% de NaN
threshold_col = int(0.5 * len(df))
df_cleaned_columns = df.dropna(axis=1, thresh=threshold_col)

# Drop des lignes qui ont plus de 50% de NaN
threshold_row = int(0.5 * len(df.columns))
df_cleaned_rows = df_cleaned_columns.dropna(axis=0, thresh=threshold_row)

print("DataFrame après avoir supprimé les colonnes avec plus de 50% de NaN :")
print(df_cleaned_columns)
print("\nDataFrame après avoir supprimé les lignes avec plus de 50% de NaN :")
print(df_cleaned_rows)