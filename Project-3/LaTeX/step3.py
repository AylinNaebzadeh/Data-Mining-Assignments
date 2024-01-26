tfidf = TfidfVectorizer()

tf_idf_matrix = tfidf.fit_transform(df_dropped['cleaned_title'] + ' ' + df_dropped['cleaned_abstract'])

"""
tf_idf_matrix

<22819x99910 sparse matrix of type '<class 'numpy.float64'>'
	with 2082915 stored elements in Compressed Sparse Row format>
"""

bow_vectorizer = CountVectorizer(max_df = 0.90, min_df = 2, max_features = 1000, stop_words='english')
bow_matrix = bow_vectorizer.fit_transform(df_dropped['cleaned_title'] + ' ' + df_dropped['cleaned_abstract'])

"""
bow_matrix

<22819x1000 sparse matrix of type '<class 'numpy.int64'>'
	with 1286156 stored elements in Compressed Sparse Row format>
"""
