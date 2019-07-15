from flask import Flask, request, Response
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from tensorflow import keras
import pickle
from keras.preprocessing import sequence
from embedding import to_index_array, padding, decompose_string


app = Flask(__name__)
CORS(app)

MAX_LEN = 681

with open('jamo.pydict', 'rb') as f:
    jamodict = pickle.load(f)

def encode_review(text):
    text = decompose_string(text)
    text = to_index_array(text, jamodict)
    text = padding(text, MAX_LEN)
    return text


def predict(text):
    model = tf.keras.models.load_model('models/latest-yok-detect-model.h5')
    graph = tf.get_default_graph()

    indices = encode_review(text)
    indices = np.array([indices])
    with graph.as_default():
        result = model.predict_classes(indices)
    poornag = ''
    if result == 0:
        poornag = '욕아님'
    else:
        poornag = '욕'
    return poornag





@app.route('/', methods=['POST'])
def upload_train():
    data = request.get_json()
    print(data['text'])

    poornag = predict(data['text'])

    response = Response()
    response.headers[
        'Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'

    return poornag, 200


app.run(port=5000, debug=True, threaded=True)