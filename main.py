from brains.data import url
from brains.viz import viz



# TODO actually make a main function and/or wrap this into flask implementation

# Load data
# TODO prompt user to designate path
path = "sample_data/example.csv"
df = url.path_to_dataframe(path)

# Display summary of data
# Also tutorial for user as he goes along (suggesting what values to choose in pivot table
# based off of what is given in data summary)
# e.g. suggesting to use values that aren't unique, columns will be ideally 10 or less fields
#TODO make module/function for this
# e.g. data.summarize(df)

def data_summarize():
    # Make user aware of basic features
    print("Data features:")
    print(df.info())
    # Just to make user aware of current dataset columns
    print("Current columns + Types of data:")
    print(df.dtypes)
    # Number of unique values for each column reveals which columns have most and least unique values
    # This tells user to pick column w least unique values when customizing
    print("Number of unique values:")
    print(df.nunique())
    # Tell user which displays are available to use
    print("Types of displays possible:")
    print("Bar chart, histogram, pie chart")  # I think these?
    # User guide throughout to ensure most helpful data visualizations

data_summarize()


# Prompt user for input based on above
# TODO implement this
print("plotting a histogram of Age...")
viz.histogram(df['Age'])