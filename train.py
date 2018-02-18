import os
from time import time
import data_visualization as dv
import pandas as pd
#import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score

class Solution(object):
    def __init__(self):

        self.X_train,self.X_test,self.y_train,self.y_test,self.dataframe_all=dv.preprocess(os.path.join(os.getcwd(),"bcw.txt"))

    def visualize(self):
        dv.visualization(self.X_test,self.y_test)

    def train_classifier(self,clf):
        ''' Fits a classifier to the training data. '''

        # Start the clock, train the classifier, then stop the clock
        start = time()
        clf.fit(self.X_train, self.y_train)
        end = time()

        # Print the results
        print("Trained model in {:.4f} seconds".format(end - start))

    def predict_labels(self,clf, features, target):
        ''' Makes predictions using a fit classifier based on F1 score. '''

        # Start the clock, make predictions, then stop the clock
        start = time()
        y_pred = clf.predict(features)

        end = time()
        # Print and return results
        print("Made predictions in {:.4f} seconds.".format(end - start))

        return f1_score(target, y_pred, pos_label=1), sum(target == y_pred) / float(len(y_pred))

    def train_predict(self,clf):
        ''' Train and predict using a classifer based on F1 score. '''

        # Indicate the classifier and the training set size
        print("Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(self.X_train)))

        # Train the classifier
        self.train_classifier(clf, self.X_train, self.y_train)

        # Print the results of prediction for both training and testing
        f1, acc = self.predict_labels(clf, self.X_train, self.y_train)
        print(f1, acc)
        print("F1 score and accuracy score for training set: {:.4f} , {:.4f}.".format(f1, acc))

        f1, acc = self.predict_labels(clf, self.X_test, self.y_test)
        print("F1 score and accuracy score for test set: {:.4f} , {:.4f}.".format(f1, acc))

    def pca(self):

        df=self.dataframe_all
        return dv.pca(df)




