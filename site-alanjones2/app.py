# Taken from: https://github.com/alanjones2/Flask-Plotly/tree/main/plotlycallback-gm

from flask import Flask, config, render_template, request, session
import pandas as pd
import json
import plotly
import plotly.express as px

# Bug 14 fix: https://www.geeksforgeeks.org/python-import-from-parent-directory/

import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

# our libaries
from brains.viz import plotly_viz as pp
from brains.data import url as url


app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'SquidBrainsAresShapedLikeDonuts' # this is so we can use "session"


def df_session_load(): # because we will do this often, just want a fast way to get it back to a df
    return pd.read_json(session['df'])


def update_data(form):
    """Update the dataframe"""

    session['path'] = form


# call back method, refreshes when data is entered
@app.route('/callback', methods=['POST', 'GET'])
def cb():
    print(request.args.get('data'))
    return plot(request.args.get('data'),session['features']) # calls a function to update


@app.route('/', methods=['GET','POST'])
def index():
    # return render_template('chartsajax.html', graphJSON=gm())
    path = "../sample_data/example.csv"

    # session['viz'] = ActiveViz(path)

    session['path'] = path  # location of data
    df = url.path_to_dataframe(session['path'])
    session['df'] = df.to_json()
    # session['features'] = df.columns
    session['selected'] = ['Age']

    if request.method == 'POST':
        if request.form['button'] == "data_fetch":
            print('Fetching data...')
            pass
        elif request.form['button'] == "plot":
            print('plotting data...')
            return render_template('chartsajax.html', graphJSON=plot(session['path'], session['selected']),
                                   tables=[df.to_html(classes='data')], titles=df.columns.values)
            # pass
        else:
            print('reset')
            return render_template('start.html')
            pass
        print("request form: ")
        print(request.form)
        # print(request.form['plot_button'])
        print('Button pressed')
    else:
        return render_template("start.html")




    # TODO render a page with a feature selection option and a plot button
    # print(df.columns.values)
    return render_template('chartsajax.html', graphJSON=plot(session['path'],session['selected']), tables=[df.to_html(classes='data')], titles=df.columns.values)


def plot(path, features): # TODO add plot type and feature selection trhough callbacks
    # plot the stuff
    print("Path: " + path)
    session['path'] = path
    # try:
    df = df_session_load()
    fig = pp.histogram(df[features])
    # except:
    #     fig = None

    return fig
