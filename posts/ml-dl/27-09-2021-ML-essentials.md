
### Machine Learning Essentials

Machine learning theory is a field that intersects statistical, probabilistic, computer science and algorithmic aspects arising from learning from data and finding hidden insights which can be used to build intelliget applications. 

There are many reasons why the mathematics of Machine Learning is important: 
1. Selecting the right algorithm which includes giving considerations to _accuracy_, _training time_, _model complexity_, number of _parameters_ and number of _features_. 
2. Choosing _parameter settings_ and _validation_ strategies. 
3. Identifying underfitting and overfitting by understanding the _Bias-Variance tradeoff_. 
4. Estimating the right _confidence_, _interval_ and _uncertainty_. 

## Cheatsheets
![](https://scikit-learn.org/stable/_static/ml_map.png)

![](https://miro.medium.com/max/1400/0*B6MGGFnT-os8NQQV)

### Popular Models
- Linear Discriminant Analysis
- K Neighbours Classifier
- Quadratic Discriminant Analysis 
- Logistic Regression
- Naive Bayes
- Gradient Boosting Classifier
- Decision Tree Classifier
- Extra Tree Classifier 
- Random Forest Classifier
- Ada Boost Classifier
- Light Gradient Boosting
- Machine Ridge Classifier 
- SVM - Linear Kernel




|Column|Information| Definition|
|---|---|---|
|Accuracy| Overall correctness of predictions | Higher the value, better the model|
|AUC | Area Under Curve | This is a measure of ratio between true positive and False positives|
|Recall| Ratio of true positive with sum of true positive and false negative| This gives the fraction of good classifications that are done with respect to overall classification| 
|Prec| Precision Ration of True positive with sum of true positive and false positive| Used when the cost of false positive is greater that that of getting a false negative|
|F1|Balance between precision and recall|More useful than accuracy in determining model quality when the data contains widely different number of data for each class|
|Kappa | THe degree of arrangement between true values and predicted values|
|MCC|Matthews correlation coefficient|A measure of quality of classifications. Used only in case of binary classificiation|
|TT| Time taken| Time taken in seconds for model to predict the output after an input is given to it| 