# Machine Learning

## Business Case
Hypothesis → Data collection → Data preparation → Choosing ML Model → Model training → Evaluation → Hyper-parameter tuning → Prediction

- Understand the business case
- Set aside testing and training data (make presentations with test or test+ new data)
- Don't spend *too much time* on identifying the right algorithm. (Go with what you know)

[Neural Networks with JAVA](https://www.nnwj.de)

### Myth    
- Each use case = One best algorithm
- The goal of the project is one model


### Variables
- Nominal
- Ordinal
- Scale


## Linear discriminant analysis

Linear discriminant analysis is used to reduce the number of features to be more manageable before classification.

- Stepwise discriminant Analysis

## 1. Supervised Learning

Targets with more than two categories should be kept rare.

### Binary Classification

- Logistic Regression
    - Listwise Deletion
    - All inputs are either Used or Stepwise
    - Scale variables (or dummy coding)
    - Most transparent - lot of detail
    - Inputs are ranked from most to least important

- Decision Trees
- Naive Bayes
- K Nearest Neighbours

### Multi Class Classification
- K Nearest Neighbours | Takes more computational power | Brute force matching method
- Naive Bayes | Predictions are independent/ uncorrelated  

### Regression
- Not a good Machine Learning method
- Best used when looking for trends instead of classifying data into different groups
- Continous
- Linear regression

## 2. Unsupervised Learning
- K-means clustering

## 3. Reinforcement Learning
- Q Learning

## Ensemble Modelling

### Bagging
- Several different trees (multiple predictions)

### Boosting
- Different machine learning Algorithms
- K Means clustering + Decision Trees
- Semi Supervised Learning

### Stacking
- Stack several algorithms
- Feature Weighted Linear Stacking (upto 30 algorithms)


### Bayesian Principles
- Use prior knowledge
- Choose answer that explains observations the most
- Avoid making extra assumptions

## Probability theory
### Discrete vs Continous
Discreate: Probablility Mass Function (PMF)
Continous: Probability Density Function (PDF)
Chain Rule:
Sum Rule:

## Frequentists vs Bayesians

## Bias
High bias can cause an algorithm to miss the relevant relations between features and target outputs (underfitting)

### Underfitting, Overfitting, Balanced

![alt-text](https://docs.aws.amazon.com/machine-learning/latest/dg/images/mlconcepts_image5.png)
![alt-text](https://miro.medium.com/max/936/1*xwtSpR_zg7j7zusa4IDHNQ.png)



## List of Machine Learning Algorithms



## Paradigms of Machine Learning

### The 14 Learnings in Machine Learning ([collated by Jason Brownlee](https://machinelearningmastery.com/types-of-learning-in-machine-learning/))  

#### Learning Problems

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

#### Hybrid Learning Problems

4. Semi-Supervised Learning
5. Self-Supervised Learning
6. Multi-Instance Learning

#### Statistical Inference

7. Inductive Learning
8. Deductive Inference
9. Transductive Learning

#### Learning Techniques

10. Multi-Task Learning
11. Active Learning
12. Online Learning
13. Transfer Learning
14. Ensemble Learning


### Three paradigms of Machine Learning ([Alberto Bietti, Julien Mairal](https://lear.inrialpes.fr/people/mairal/resources/pdf/course_1.pdf))
Optimization
Kernal Methods
Deep Neural Methods
The sparsity principle


### Five paradigms of Machine Learning ([Pedro Domingos](https://www.amazon.in/Master-Algorithm-Ultimate-Learning-Machine/dp/0465065708)):

|                 |                      |                          |
| -----------     | -----------          | --------------           |
| Symbolists      | Logic, Philosophy    | Inverse deduction        |
| Connectionists  | Neuroscience         | Backpropagation          |
| Evolutionaries  | Evolutionary biology | Genetic Programming      |
| Bayesians       | Statistics           | Probabilistic inference  |   
| Analogizers     | Psychology           | Kernal Machines          |


## Machine Learning Methods

|  ML Methods                         |      Algorithms                 |                       
| -----------------------   | --------------------  |
| Deep Learning             | Deep Boltzman Machine, Deep Belief Network, Convolutional Neural Network, Stacked Auto Encoders |
| Ensemble                  |                       |                       
| Neural Networks           |                       |                       
| Regularisation            |                       |                       
| Rule System               |                       |                       
| Regression                |                       |                       
| Bayseian                  |                       |                       
| Decision Trees            |                       |                       
| Diamentionality Reduction |                       |                       
| Instance Based            |                       |                       
| Clustering                |                       |                       


## Bootstrap
Bootstrap simulates obtaining many new datasets by repeated sampling with replacement from the origional dataset.

## Bagging

## Boosting
An ensemble learning strategy that trains a series of weak models, each one attempting to correctly predict the observations the previous model got wrong.

## Bayesian Methods
- Works well even with small data.  
- Computationally costly in large data.  
- A prior must be chosen.   

# Greedy Algorithm
'Greedy algorithms take all of the data in a particular problem, and then set a rule for which elements to add to the solution at each step of the algorithm. In the animation above, the set of data is all of the numbers in the graph, and the rule was to select the largest number available at each level of the graph. The solution that the algorithm builds is the sum of all of those choices.' via [Brilliant](https://brilliant.org/wiki/greedy-algorithm/)

# Logistic regression
- Used in classification problems
- Predictive modelling algorithm
- It uses sigmoid function (logistic) to find the relationship between variables

# Support Vector Machine
- Can be used for both classification and regression problems but is mostly used for solving classification problems





## Image sources:
I1:  [Overfitting, Biased and Balanced via AWS Documentation](https://docs.aws.amazon.com/machine-learning/latest/dg/images/mlconcepts_image5.png)
