# calculate the feature importance for each cluster
importance = []
for i in range(81):
  imp = 1 - np.std(centroids[:, i]) / (np.max(centroids[:, i]) - np.min(centroids[:, i]))
  importance.append(imp)

# sort the features by importance in descending order
features = X_scaled_df.columns
sorted_features = sorted(zip(features, importance), key=lambda x: x[1], reverse=True)

# print the feature importance
print("Feature importance for k-means clustering for all the samples:")
for f, i in sorted_features:
  print(f"{f}: {i:.4f}")