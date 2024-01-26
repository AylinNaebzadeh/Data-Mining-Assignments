# Create an LDA object with 20 topics
lda_tf_idf = LatentDirichletAllocation(n_components=20)
lda_bow = LatentDirichletAllocation(n_components=20)

tf_idf_topics = lda_tf_idf.fit_transform(tf_idf_matrix)
print(tf_idf_topics.shape) # Output will be (22819, 20)

bow_topics = lda_bow.fit_transform(bow_matrix)
print(bow_topics.shape) # Output will be(22819, 20)