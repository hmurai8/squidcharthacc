# Taken from: https://github.com/alanjones2/Flask-Plotly/tree/main/plotlycallback-gm

from flask import Flask, config, render_template, request, session
import pandas as pd

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

    session['path'] = form['fname']
    df = url.path_to_dataframe(session['path'])
    session['df'] = df.to_json()
    return


def get_features(form):
    """Update the dataframe"""

    print("form:")
    print(form)
    session['selected'] = form.getlist('selected')
    return


@app.route('/', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        if request.form['button'] == "fetch_data":
            print('Fetching data...')
            update_data(request.form)
            df = df_session_load()
            print(session)
            return render_template('select.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
        elif request.form['button'] == "plot":
            print('Plotting')
            get_features(request.form)
            print('plotting data...')
            df = df_session_load()
            return render_template('plot.html', graphJSON=plot(),tables=[df.to_html(classes='data')], titles=df.columns.values)
            # pass
        else:
            # TODO add reset button to each page
            print('reset')
            return render_template('start.html')
            pass
    else:
        return render_template("start.html")


def plot(): # TODO add plot type and feature selection trhough callbacks

    # try:
    df = df_session_load()

    fig = pp.histogram(df[session['selected']])

    return fig
