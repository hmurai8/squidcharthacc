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
    # variables
    current_columns = df.columns
    types = df.dtypes
    aggregation = df.agg(['count', 'min', 'max', 'mean', 'sum'])
    unique = df.nunique()
    print("Current columns:")
    print(current_columns)
    print("Types of data:")
    print(types)
    print("Numeric data features:")
    print(aggregation)
    print("Number of unique values:")
    print(unique)
    print("* Suggested column fields: 10 unique values or less *")
    print("Types of displays possible:")
    print("Bar chart, Histogram, Pie chart, Line graph")

data_summarize()


# Prompt user for input based on above
# TODO implement this
print("plotting a histogram of Age...")
viz.histogram(df['Age'])