from brains.data import url
from brains.viz import viz


# TODO actually make a main funciton and/or wrap this into flask implementation

# Load data
# TODO prompt user to designate path
path = "sample_data/example.csv"
df = url.path_to_dataframe(path)

# Display summary of data
#TODO make module/function for this
# e.g. data.summarize(df)
print(df.columns)
print(df.dtypes)
print(df)

# Prompt user for input based on above
# TODO implement this
print("plotting a histogram of Age...")
viz.histogram(df['Age'])