# Create a PCA object with 2 components
pca_tf_idf = PCA(n_components=2)
pca_bow = PCA(n_components=2)

tf_idf_reduced = pca_tf_idf.fit_transform(tf_idf_topics)
print(tf_idf_reduced.shape) # Output will be (22819, 2)

bow_reduced = pca_bow.fit_transform(bow_topics)
print(bow_reduced.shape) # Output will be (22819, 2)