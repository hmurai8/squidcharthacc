# load data from URL into dataframe

import os
import pandas as pd


# TODO get this from an argument
# url = "https://opendata.hawaii.gov/dataset/c2b3cc44-13db-4d91-bca0-e46d629e0141/resource/8241acde-528f-4895-84c9-aa21dc3bdc94/download/department-of-defense-state-civil-defense-emergency-siren-locations-csv.csv"
# df = pd.read_csv(url)

def path_to_dataframe(path):
    """
    Convert a file to a dataframe

    :param path: Location of data. May be a local path or a URL
    :return df: a dataframe that the path has been read into
    """

    # TODO extract extension from path and determine the correct way to read in a file
    # file_type = os.path.

    df = pd.read_csv(path) # right now only working for csv's

    return df