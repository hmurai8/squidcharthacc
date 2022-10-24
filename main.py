import brains.data.url as url
import brains.viz.viz as viz


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

# Prompt user for input based on above
# TODO implement this
print("plotting a histogram of Age...")
viz.histogram(df['Age'])