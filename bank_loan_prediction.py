import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

path = r"F:\Data Science\Bank Data.xlsx"  # dataset path
orig_data = pd.read_excel(path, index_col="id")

# replace categorical data with '1' and '0'
data = orig_data.replace(['NO', 'YES'], [0, 1])
data = pd.get_dummies(data)

# split data into training set and test set
train_data = data.sample(frac=0.80, random_state=10)
test_data = data.drop(train_data.index)

train_features = train_data.loc[:, train_data.columns != 'loan']
train_label = train_data.loc[:, train_data.columns == 'loan']

test_features = test_data.loc[:, train_data.columns != 'loan']
test_label = test_data.loc[:, train_data.columns == 'loan']

# scaling data set using standardization
scale_train_feat = (train_features - train_features.mean())/train_features.std()
scale_test_feat = (test_features - test_features.mean())/test_features.std()

# classifier for training
classifier = DecisionTreeClassifier(criterion="entropy", random_state=0)
classifier.fit(scale_train_feat, train_label)

# predicting test results
predict_data = classifier.predict(scale_test_feat)
test_data['predicted_loan'] = predict_data
test_data.to_excel("Prediction Result.xlsx")

# confusion matrix
matrix = confusion_matrix(test_label, predict_data)
print("Confusion matrix for Decision Tree prediction \n", matrix)

# accuracy
accuracy = (matrix[0, 0]+matrix[1, 1])/matrix.sum()
print("Decision Tree prediction accuracy is ", accuracy)
