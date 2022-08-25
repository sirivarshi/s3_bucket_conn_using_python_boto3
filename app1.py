# write a program to string from lower to uppercase letter
import pandas as pd
import numpy as np
from sklearn import ensemble,metrics,model_selection,decomposition,preprocessing,pipeline
from functools import partial
import optuna
from skopt import space ,gp_minimize
from hyperopt import hp,fmin



if __name__ == "__main__":
    df = pd.read_csv(r"C:\Users\HY20367012\Documents\train.csv")
    df.head()

    x = df.drop("price_range", axis=1).values
    y = df.price_range.values
    clf = ensemble.RandomForestClassifier(n_jobs=-1)
    params = {
        "n_estimators":np.arange(1,1500,100),
         "max_depth": np.arange(1,20),
        "criterion": ["gini", "entropy"]
    }
    model = model_selection.RandomizedSearchCV(
        estimator=clf,
        param_distributions=params,
        scoring="accuracy",
        verbose=10,
        n_jobs=1,
        cv=5
    )
    model.fit(x, y)
    print(model.best_score_)
    print(model.best_estimator_.get_params())