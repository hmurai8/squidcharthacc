# load data from URL into dataframe

import pandas as pd

# TODO get this from an argument
url = "https://opendata.hawaii.gov/dataset/c2b3cc44-13db-4d91-bca0-e46d629e0141/resource/8241acde-528f-4895-84c9-aa21dc3bdc94/download/department-of-defense-state-civil-defense-emergency-siren-locations-csv.csv"

df = pd.read_csv(url)