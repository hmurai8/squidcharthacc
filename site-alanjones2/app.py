# Taken from: https://github.com/alanjones2/Flask-Plotly/tree/main/plotlycallback-gm

from flask import Flask, config, render_template, request
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


class ActiveViz: # object to hold parameters for actuve visualization
    def __init__(self, path, df, features):
        self.path = None
        self.df = pd.DataFrame()
        self.features = self.feats()

        class feats:
            def __init__(self, avail, selected):
                self.avail = None
                self.selected = None




# call back method, refreshes when data is entered
@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return plot(request.args.get('data')) # calls a function to update


@app.route('/')
def index():
    # return render_template('chartsajax.html', graphJSON=gm())
    path = "../sample_data/example.csv"
    df = url.path_to_dataframe(path)
    return render_template('chartsajax.html', graphJSON=plot(), tables=[df.to_html(classes='data')], titles=df.columns.values)


def plot(path="../sample_data/example.csv"): # TODO add plot type and feature selection trhough callbacks
    # ploit the stuff

    df = url.path_to_dataframe(path)

    fig = pp.histogram(df['Age'])
    return fig
