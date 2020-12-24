from flask import Flask, render_template, request, session
from flask_session import Session
from forms import Message

import os
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import _tree
import pickle
from joblib import dump,load
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.config['SECRET_KEY'] = '52ac5291db0d76d2fa284f8a5a145d4ed78c'
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)



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

    return "<h1>Hello wold!</h1><a href='/predict'>Click here to start</a>"

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

def print_disease(node):
    node = node[0]
    val  = node.nonzero()
    disease = le.inverse_transform(val[0])
    return disease


if __name__ == '__main__':
    app.run(debug = True)
