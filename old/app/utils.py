import joblib

def load_model(path):
    """ Load the pre-trained model from specified path. """
    return joblib.load(path)