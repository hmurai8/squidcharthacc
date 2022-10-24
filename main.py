import brains.data.url as url
import brains.viz.viz as viz



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
    # Just to make user aware of current dataset columns
    print("Current columns + Types of data:")
    print(df.dtypes)
    # Make user aware of basic numeric data features
    print("Numeric data features:")
    print(df.agg(['count', 'min', 'max', 'mean', 'sum']))
    # Number of unique values for each column reveals which columns have most and least unique values
    # This tells user to pick column with the least unique values when customizing
    print("Number of unique values:")
    print(df.nunique())
    # Tell user which displays are available to use (should choose one with least amt of unique values)
    print("Types of displays possible:")
    print("Bar chart, histogram, pie chart")  # I think these?
    # User guide to help user customize most helpful data visualizations after seeing data summary (what you should
    # be looking for in certain fields and what type of chart fits best for certain types of data)

data_summarize()


# Prompt user for input based on above
# TODO implement this
print("plotting a histogram of Age...")
viz.histogram(df['Age'])