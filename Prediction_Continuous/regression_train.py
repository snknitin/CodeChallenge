import os
from time import time
import pipeline as prep
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.model_selection import GridSearchCV
import shared_utils as su
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedShuffleSplit


class Solution(object):
    def __init__(self):

        self.dataframe_all=su.load()

    def setup_training(self):
        ''' Fits a regression model to the training data. '''

        split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
        for train_index, test_index in split.split(self.dataframe_all, self.dataframe_all["income_cat"]):
            self.strat_train_set = self.dataframe_all.loc[train_index]
            self.strat_test_set = self.dataframe_all.loc[test_index]

        self.dataframe_all = self.strat_train_set.drop("median_house_value", axis=1)  # drop labels for training set
        self.feature_labels = self.strat_train_set["median_house_value"].copy()

    def preprocess(self):
        self.prepared_data = prep.process_pipeline(self.dataframe_all)


    def predict_values(self):
        ''' Makes predictions using a fit classifier based on F1 score. '''

        self.forest_reg = RandomForestRegressor(random_state=42)
        self.forest_reg.fit(self.prepared_data, self.feature_labels)
        price_predictions = self.forest_reg.predict(self.prepared_data)
        forest_mse = mean_squared_error(self.feature_labels, price_predictions)
        forest_rmse = np.sqrt(forest_mse)
        print(" Forest RMSE ", forest_rmse)
        forest_scores = cross_val_score(self.forest_reg, self.prepared_data, self.feature_labels,
                                        scoring="neg_mean_squared_error", cv=10)
        forest_rmse_scores = np.sqrt(-forest_scores)
        print("Scores:", forest_rmse_scores)
        print("Mean:", forest_rmse_scores.mean())
        print("Standard deviation:", forest_rmse_scores.std())

    def grid_search(self):
        param_grid = [
            # try 12 (3×4) combinations of hyperparameters
            {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
            # then try 6 (2×3) combinations with bootstrap set as False
            {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
        ]

        forest_reg = self.forest_reg
        # train across 5 folds, that's a total of (12+6)*5=90 rounds of training
        grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                                   scoring='neg_mean_squared_error', return_train_score=True)
        grid_search.fit(self.prepared_data, self.feature_labels)

        return grid_search.best_estimator_

    def test(self,final_model):
        self.final_model=final_model
        X_test = self.strat_test_set.drop("median_house_value", axis=1)
        y_test = self.strat_test_set["median_house_value"].copy()

        X_test_prepared = prep.process_pipeline(X_test)
        final_predictions = final_model.predict(X_test_prepared)

        some_data = X_test.iloc[:10]
        some_labels = y_test[:10]
        some_data_prepared = prep.process_pipeline(some_data)
        print("Predictions:", final_model.predict(some_data_prepared))
        print("Labels:", list(some_labels))

        final_mse = mean_squared_error(y_test, final_predictions)
        final_rmse = np.sqrt(final_mse)
        print(" Final RMSE ", final_rmse)






if __name__=="__main__":
    s=Solution()

    s.setup_training()
    s.preprocess()
    s.predict_values()
    s.test(s.grid_search())







