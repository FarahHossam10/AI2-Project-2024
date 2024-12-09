## Predicting Heart Disease Risk Using Machine Learning
In this project we tried building a machine learning model for predicting heart disease risk
based on several features like age, gender, blood pressure, etc.
below we state the problem, objectives and the development process.

### Team Members:
1. Farah Osama
2. Salma Shaheen
3. Ghada Hassan
4. Fatma Elkassaby
5. Farah Hossam

### Problem Statement:
Heart disease is a leading global cause of death, highlighting the urgent need for early detection.
Current diagnostic methods are often expensive, time-consuming, and inaccurate. This project uses
machine learning to create a reliable, data-driven model for predicting heart disease,
emphasizing effective feature selection, optimal algorithm performance, and practical clinical application.

### Project Objectives:
- Early Detection and Prevention
  Our project aims to develop an AI-powered model to predict heart disease risk early,
  enabling timely intervention and potentially saving lives.
- Personalized Healthcare
  The model will help healthcare providers tailor treatments and prevention strategies
  based on individual risk profiles.
- Improve Healthcare Efficiency
  By automating risk assessment, the model can free up healthcare professionals to focus on patient care.

## Development Process:
### 1- Data Preprocessing
- Features are renamed to ensure clarity and full understanding of their significance, and to avoid ambiguity.
- Handling Missing or Null values to ensure data completeness and readiness for analysis.
- Encoding Categorical Features: Categorical features are converted into numerical values allowing the model
  to understand them.
- Scaling Numerical Features: Numerical features are normalized or standardized to bring them to
  a comparable scale, ensuring better model performance.
- Splitting Data: The data is divided into training and testing sets using train\_test\_split,
  allowing the model to learn and be evaluated.
    
### 2- Exploratory Data Analysis (EDA) 
**Visualization and Correlation Analysis:**
We used several different visualizations:
- Histograms to view frequency distributions of different features.
- box plots to detect outliers.
- Heatmaps to visualize the relationships between features.
- pairplots to show scatterplots for every pair of numerical features in the dataset.
- bar charts to summarize and compare categorical data, in our case for example between the two categories
  of the label or target which is 1 or 0, a heart disease patient or not.

### 3- Model Training
**Algorithms Used:**
We used several different machine learning algorithms to achieve the highest accuracy for this dataset:
1- Linear Regression: While not typically used for classification, can predict a continuous risk score,
   useful for personalized risk assessment.
2- Logistic Regression: Estimates the probability of heart disease based on input features, interpretable
   and widely used.
3- K Nearest Neighbors (KNN): Classifies data points based on proximity to similar data points, simple but effective.
4- Support Vector Machine (SVM): Finds a hyperplane to separate data points into classes,
   powerful and versatile for complex patterns.
    
### 4- Model Evaluation
**We used a variety of evaluation methods:**
- Accuracy: Percentage of correct predictions made by the model, a general measure of model performance.
- Confusion Matrix: Visualizes the true vs. predicted classifications, showing the model's performance in detail.
- Precision, Recall, F1-Score: Additional metrics to evaluate the model's performance, particularly in imbalanced datasets.

**Evaluation Results:**
- The model achieved a highest accuracy of **88.33% using SVM.**
- A 79% F1-Score
- The SVM model demonstrates an 11% higher accuracy compared to KNN and achieves approximately 2% better accuracy than Logistic Regression.



#### Project Proposal [here](https://drive.google.com/file/d/1zbQRFr8rn5p_C6xAyr5r5TEYbQXefj5_/view?usp=sharing)
#### Watch this [video](https://youtu.be/nEtLE-8wS8k?si=qDj0I7F3-zC6oplA) to learn more details about our project
#### Also Check out our presentation [here](https://youtu.be/nEtLE-8wS8k?si=qDj0I7F3-zC6oplA)









    

