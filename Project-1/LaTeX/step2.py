X_train, X_test, y_train_MCQ220, y_test_MCQ220 = train_test_split(X_list, MCQ220_elements, test_size=0.3, random_state=42)

# Initialize regression models
linear_reg_pca = LinearRegression()
knn_reg_pca = KNeighborsRegressor()
decision_tree_reg_pca = DecisionTreeRegressor()

# Train the models
linear_reg_pca.fit(X_train, y_train_MCQ220)
knn_reg_pca.fit(X_train, y_train_MCQ220)
decision_tree_reg_pca.fit(X_train, y_train_MCQ220)

# Make predictions on the testing data
linear_reg_pred_pca_cancer = linear_reg_pca.predict(X_test)
knn_reg_pred_pca_cancer = knn_reg_pca.predict(X_test)
decision_tree_reg_pred_pca_cancer = decision_tree_reg_pca.predict(X_test)
