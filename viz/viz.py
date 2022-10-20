# visualization file

from matplotlib import pyplot as plt
plt.interactive(False)

# get dataframe
# TODO change this to an import from data.url
import pandas as pd
url = "https://opendata.hawaii.gov/dataset/c2b3cc44-13db-4d91-bca0-e46d629e0141/resource/8241acde-528f-4895-84c9-aa21dc3bdc94/download/department-of-defense-state-civil-defense-emergency-siren-locations-csv.csv"
df = pd.read_csv(url)

# visualize

# TODO write functions for different visualizations and call them here

# A histogram
plt.hist(df['DECIBEL'])
plt.xlabel('decibel')
plt.ylabel('counts')
plt.title('Sirens')
plt.show()