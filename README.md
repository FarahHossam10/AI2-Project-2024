## Predicting Heart Disease Risk Using Machine Learning
This project focuses on developing an AI-based system to predict the risk of heart disease in individuals using clinical and demographic data. By leveraging machine learning algorithms, the model analyzes features such as chest pain type, cholesterol levels, blood pressure, and other health indicators to assess the likelihood of heart-related conditions.

The primary goal is to enable early detection of potential risks, empowering healthcare providers to implement timely interventions and personalized treatment plans. This not only improves patient outcomes but also enhances healthcare efficiency by automating risk assessments. The system's predictive capabilities aim to assist medical professionals in decision-making, prioritize patient care, and ultimately save lives by reducing delays in diagnosis.

This innovative approach combines data science and medicine to address one of the leading causes of mortality worldwide—heart disease—highlighting the transformative potential of AI in healthcare


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
1. Linear Regression: While not typically used for classification, can predict a continuous risk score,
   useful for personalized risk assessment.
2. Logistic Regression: Estimates the probability of heart disease based on input features, interpretable
   and widely used.
3. K Nearest Neighbors (KNN): Classifies data points based on proximity to similar data points, simple but effective.
4. Support Vector Machine (SVM): Finds a hyperplane to separate data points into classes,
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

## Future Work:
**- Integration with Real-Time Data:**
Incorporate real-time clinical data from wearable devices (e.g., smartwatches) to dynamically update predictions and provide
continuous monitoring of heart health.


**- Increasing the Dataset Size:**
Expand the dataset by sourcing additional data from public repositories, hospitals, and clinical trials to improve the
model's accuracy, robustness, and generalizability.



**- Deployment as a Web or Mobile Application:**
Develop an accessible platform (web or mobile app) for healthcare providers and patients to use the model for
real-time heart disease risk assessment.


**- Incorporation of Advanced Algorithms:**
Explore more complex algorithms such as ensemble models (e.g., Random Forest, XGBoost) and deep learning techniques
to improve accuracy and handle larger datasets effectively.



**- Cross-Population Validation:**
Validate the model on datasets from diverse populations to ensure its generalizability and adaptability to different
demographics and healthcare systems.


**- Feature Expansion:**
Include additional features such as genetic information, detailed lifestyle habits, and environmental factors to
make predictions more comprehensive and personalized.


**- Explainable AI (XAI):**
Integrate explainability techniques to provide insights into how the model arrives at its predictions, increasing
trust and usability for clinicians.


**- Collaborations with Healthcare Providers:**
Partner with hospitals and research institutions to gather more accurate data, refine the model, and validate
its performance in clinical settings.


**- Integration of Risk Mitigation Strategies:**
Include personalized lifestyle and treatment recommendations alongside risk predictions to provide actionable 
insights for patients



## Realted Work:
- https://iopscience.iop.org/article/10.1088/1757-899X/1022/1/012072/meta
- https://www.mdpi.com/1999-4893/16/2/88
- https://docs.google.com/viewer?embedded=true&url=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FV-V-Ramalingam%2Fpublication%2F325116774_Heart_disease_prediction_using_machine_learning_techniques_A_survey%2Flinks%2F5d48560a299bf1995b68266f%2FHeart-disease-prediction-using-machine-learning-techniques-A-survey.pdf


  
#### Project Proposal [here](https://drive.google.com/file/d/1zbQRFr8rn5p_C6xAyr5r5TEYbQXefj5_/view?usp=sharing)
#### Watch this [video](https://youtu.be/nEtLE-8wS8k?si=qDj0I7F3-zC6oplA) to learn more details about our project
#### Also Check out our presentation [here](https://gamma.app/docs/AI2-Project-Predicting-Heart-Disease-Risk-Using-Machine-Learning-ekf34oik31f9wbz?mode=doc)









    
