# import numpy as np
# import pandas as pd
# from scipy.io import arff
# from matplotlib import pyplot as plt
from sklearn.metrics import roc_auc_score #, roc_curve 

def auc_roc_model(model,X_test,y_test,test=False):
    if test == True:
        model_probs = model.predict_proba(X_test)
        model_probs = model_probs[:, 1]
        auc_score = roc_auc_score(y_test,model_probs)
        return auc_score
    else:
        try:
            model_probs = model.predict_proba(X_test)
            model_probs = model_probs[:, 1]
            auc_score = roc_auc_score(y_test,model_probs)
            return auc_score
        except Exception:
            return 0
