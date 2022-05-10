# Programming for DS

1. ``assignment1/``: basic logic programming
    * ``Q1.py``: BMI calculator.
    * ``Q2.py``: Analysis words or tokens frequency from input text file.
    * ``Q3.py``: Analysis list from input file.
2. ``assignment2/``: basic logic programming: OOP
    * ``Q1.py``: Create classes ``Film`` and ``Film`` to analysis films data.
    * ``Q2.py``: Create classes ``SentimentLexicon`` and ``Classifier`` to analysis sentiment of text by the positive/negative words data.
    * ``Q3.py``: Add more class methods to analysis in class ``Classifier``
3. ``classification_model_selection``: Predict stone types, which containing data preparation, data modeling, models comparison and tuning hyper-parameters. some used techniques/algorithms listed below:
    1. Preparation stage: **One Hot Encoder** (Change input features to numeric columns), **Label Encoder** (Change output(Sample_type) column to number),**StandandScaler** (scaling traing data)
    2. Matrices: **confusion_matrix**, **macro f1 score**. 
    3. Modeling: **NaiveBayes** and **DecisionTree**, **GridSearchCV** for tuning hypers
    4. Analysis model: **Boxplot**, **Mann-Whitney U Test**
4. ``computer_vision``: Process image color and analysis results, mainly using ``cv2`` library.