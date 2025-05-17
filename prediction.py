import joblib

load_model = lambda path: joblib.load(path)

model = load_model("random_forest_model.joblib")
result_target = load_model("random_forest_model.joblib")

def prediction(dataframe):
    """
    Predict the target based on input dataframe.

    Parameters:
        dataframe (pd.DataFrame): Preprocessed input data

    Returns:
        int: Predicted class label (0 or 1)
    """
    prediction_result = model.predict(dataframe)
    return prediction_result.item()
