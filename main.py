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
    # variables
    import pandas as pd
    pd.set_option('display.float_format', lambda x: '%.1f' % x)
    current_columns = df.columns #list
    types = df.dtypes
    unique = df.nunique()
    description = df.describe()
    total = df.sum(numeric_only = True)

    print("Current columns:")
    print(', '.join(current_columns))
    print("Types of data:")
    print(types)
    print("Numeric data features:")
    print(description)
    print("Sum of numeric data:")
    print(total)
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

import plotly.express as px
def bar_chart(data,xlabel=None,ylabel="counts",title=None):
    fig = px.bar(data)
    fig.show()
bar_chart(df['Age'])
