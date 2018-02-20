# CodeChallenge
Any dataset


    For predicting continuous data : California Housing
This is one of the first introductory data sets I've used to learn regression.

    For predicting discrete data : Breast Cancer Winsconsin

Unlike most datasets relating to cancer this one has a good distribution.

Benign: 458 (65.5%)
Malignant: 241 (34.5%)

Attribute Information: (class attribute has been moved to last column)

ID  Attribute                     Domain
-- -----------------------------------------
1. Sample code number            id number
2. Clump Thickness               1 - 10
3. Uniformity of Cell Size       1 - 10
4. Uniformity of Cell Shape      1 - 10
5. Marginal Adhesion             1 - 10
6. Single Epithelial Cell Size   1 - 10
7. Bare Nuclei                   1 - 10
8. Bland Chromatin               1 - 10
9. Normal Nucleoli               1 - 10
10. Mitoses                       1 - 10
11. Class:                        (2 for benign, 4 for malignant)



## Decide on a dataset


- Description and field of interest in this corpus

 # Field of interest for classification model is CLASS
 # Field of interest for regression model is median_house_value




## Preprocessing

    Attribute with few missing values was removed in the cancer dataset and imputed with the median in the housing data. I used pandas for data preprocessing




## Visualization

- Deploy on web server?

  Regression - python render.py will run Flask app to load the visualizations on localhost 127.0.0.1:/4000
  Classification - python runner.py will run Flask app to load the visualizations on localhost 127.0.0.1:/4000

- In addition to that, you can view the iPython notebooks Classification.ipynb and Regression.ipynb to see all the plots the code being executed step wise for processing the data

- Images are stored in static folder for each project



## ML Algorithm

- For regressions : Linear, SVM, Tree, Forrest
- For CLassification : Logistic,SVC,Xgboost



## Results

- Cancer dataset : F1 score and accuracy score for test set: 0.9630 , 0.9714
- Housing : RMSE of 22112.54



