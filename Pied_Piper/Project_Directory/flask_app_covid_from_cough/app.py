from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from forms import Message

import os
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import _tree
import pickle
import librosa
from joblib import dump,load
import warnings
import matplotlib.pyplot as plt
from PIL import Image

import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.models import load_model

warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.config['SECRET_KEY'] = '52ac5291db0d76d2fa284f8a5a145d4ed78c'
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def foo():
    session['counter'] = 0
    session['symptoms_present'] = []
    session['messages'] = []

    session['node'] = 0
    session['depth'] = 1

    file_root = os.path.dirname(os.path.abspath(__file__))
    classifier = load(os.path.join(file_root,'entropy.joblib'))

    f = open(os.path.join(file_root,'dimensionality_reduction'),'rb')
    session['dimensionality_reduction'] = pickle.load(f)
    f.close()

    with open(os.path.join(file_root, 'features.pkl'), 'rb') as f:
        cols = pickle.load(f)


    print(len(cols))

    #global variable 

    session['tree_'] = classifier.tree_
    session['feature_name'] = [
                            cols[i] if i != _tree.TREE_UNDEFINED else "undefined!"
                            for i in session.get('tree_').feature
                        ]

    session['messages'].append("Please reply with yes/Yes/y or no/No/n for the following symptoms")
    name = session['feature_name'][session['node']]
    session['messages'].append(name + "?")

    return redirect(url_for('audioPrediction'))

@app.route("/predict", methods = ['GET', 'POST'])
def chat_page():
    form = Message()

    file_root = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(file_root, 'classes.pkl'), 'rb') as f:
        classes = pickle.load(f)

    le = LabelEncoder()
    le.fit(classes)

    if request.method == 'POST':
        if request.form.get('clear'):
            session['messages'] = []
            session['symptoms_present'] = []
            session['node'] = 0
            session['depth'] = 1
            session['counter'] = 0

            session['messages'].append("Please reply with yes/Yes/y or no/No/n for the following symptoms")
            name = session['feature_name'][session['node']]
            session['messages'].append(name + "?")
        else:
            message = request.form.get('message')
            session['messages'].append(message)

            threshold = session['tree_'].threshold[session['node']]
            if message.lower() == 'yes' or message.lower() == 'y':
                val = 1
            else:
                val = 0

            if val <= threshold:
                session['node'] = session['tree_'].children_left[session['node']]
                session['depth'] = session['depth'] + 1
            else:
                name = session['feature_name'][session['node']]
                session['symptoms_present'].append(name)
                session['node'] = session['tree_'].children_right[session['node']]
                session['depth'] = session['depth'] + 1

            if session['tree_'].feature[session['node']] != _tree.TREE_UNDEFINED:
                name = session['feature_name'][session['node']]
                session['messages'].append(name + " ?")
            else:
                temp = session['tree_'].value[session['node']][0].nonzero()
                present_disease = le.inverse_transform(temp[0])
                session['messages'].append( "You may have " +  present_disease )
                red_cols = session['dimensionality_reduction'].columns 
                symptoms_given = red_cols[session['dimensionality_reduction'].loc[present_disease].values[0].nonzero()]
                session['messages'].append("symptoms present  " + str(list(session['symptoms_present'])))
                session['messages'].append("symptoms given "  +  str(list(symptoms_given)) )  
                confidence_level = (1.0*len(session['symptoms_present']))/len(symptoms_given)
                session['messages'].append("confidence level is " + str(confidence_level))
                session['node'] = 0
                session['depth'] = 1

    return render_template('message.html', form = form, me = session['messages'])

# def print_disease(node):
#     node = node[0]
#     val  = node.nonzero() 
#     disease = le.inverse_transform(val[0])
#     return disease

@app.route('/audio', methods = ['GET', 'POST'])
def audioPrediction():
    file_root = os.path.dirname(os.path.abspath(__file__))
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            y, sr = librosa.load(os.path.join(app.config['UPLOAD_FOLDER'],file.filename) , mono = True, duration = 2)
            print(len(y))
            cmap = plt.get_cmap('inferno')
            plt.specgram(y, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=cmap, sides='default', mode='default', scale='dB')
            plt.axis('off')
            plt.savefig(f'{file_root}/image_data/{file.filename[:-3].replace(".", "")}.png')
            plt.clf()

        im = Image.open(f'{file_root}/image_data/{file.filename[:-3].replace(".", "")}.png')
        target_size = (128,128)

        im = im.resize(target_size)
        im = np.array(im)
        im = im[:,:,:3]
        im = np.expand_dims(im, axis = 0)

        print(im.shape)

        model = load_model('v_2.h5')
        print(model.summary())
        prediction = model.predict(im)
        print(prediction)
        if(prediction > 1e-7):
            disease = 'Sorry you may be affected by Covid!'
        else:
            disease = 'Hurray you are not affected by covid!'
        

        return render_template('audio.html', pred = prediction, di = disease)

    return render_template('audio.html')

if __name__ == '__main__':
    app.run(debug = True, threaded = True)

# llvmlite==0.34.0