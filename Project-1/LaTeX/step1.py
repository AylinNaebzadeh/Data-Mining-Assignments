df_demographic = pd.read_csv(path + 'demographic.csv')

for column in df_demographic.columns:
  total_count = len(df_demographic[column])
  zero_count = (df_demographic[column] == 0).sum()
  nan_count = (df_demographic[column].isna()).sum()
  nan_percentage = (nan_count / total_count) * 100
  print(f"Column '{column}': {nan_count} cells with a value of NaN")
  print(f"Column '{column}': {zero_count} cells with a value of 0")
  print(f"Column '{column}': {nan_percentage:.2f}% of cells with a value of NaN")
  print("---------------------------------------")

df_demographic.head(n=10)