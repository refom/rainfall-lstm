
import os
from rainfall import app
# from tensorflow import keras

MODELS_PATH = os.path.join(app.config["MODELS_PATH"], 'saved_model.pb')

if os.path.exists(MODELS_PATH):
    # model = keras.models.load_model(app.config["MODELS_PATH"])
    model = None
else:
    model = None


class Model:
    models = model
    look_back = 1
    features = 1

