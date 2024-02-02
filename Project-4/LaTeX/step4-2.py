importance_0 = []
importance_1 = []
features = X.columns
for i in range(len(features)):
  imp_0 = 1 - np.std(centroids_0[:, i]) / (np.max(centroids_0[:, i]) - np.min(centroids_0[:, i]))
  importance_0.append(imp_0)
  imp_1 = 1 - np.std(centroids_1[:, i]) / (np.max(centroids_1[:, i]) - np.min(centroids_1[:, i]))
  importance_1.append(imp_1)

sorted_features_0 = sorted(zip(features, importance_0), key=lambda x: x[1], reverse=True)
sorted_features_1 = sorted(zip(features, importance_1), key=lambda x: x[1], reverse=True)
def weighted_average(x, y, w):
  return [w * a + (1 - w) * b for a, b in zip(x, y)]
w_0 = len(X_0) / len(X)
w_1 = len(X_1) / len(X)
importance_avg = weighted_average(importance_0, importance_1, w_0)
sorted_features_avg = sorted(zip(features, importance_avg), key=lambda x: x[1], reverse=True)
print("Feature importance for k-means clustering based on the weighted average:")
for f, i in sorted_features_avg:
  print(f"{f}: {i:.4f}")