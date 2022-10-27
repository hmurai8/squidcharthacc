import pandas as pd

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

def data_summarize(df):
    import pandas as pd
    pd.set_option('display.float_format', lambda x: '%.0f' % x)
    current_columns = df.columns #list USE THIS
    types = df.dtypes
    unique = df.nunique()
    description = df.describe()
    total = df.sum(numeric_only = True)
    value_index = 0
    agg = df.describe().loc[['count','max', 'min', 'mean']]

    print("Current columns:")
    print(', '.join(current_columns))
    print("Types of data:")
    print(types)
    print("Object Count")
    print("Numeric data aggregation:")
    print(description)
    print("Sum of numeric data:")
    print(agg)
    max_index_tot = len(total) - 1
    print(total)
    # for value in total:
    #     column_name = total[value_index] # NOT columns use total (need to make list)
    #     print("Sum of values ==> " + str(value))
    #     while value_index < max_index_tot:
    #         value_index += 1
    print("* Suggested column fields: 10 unique values or less *")
    print(len(unique))
    max_index_uni = len(unique) - 1
    for value in unique:
        column_name = current_columns[value_index] # Could use columns here or make list unique
        print("Number of unique values in " + str(column_name) + " column ==> " + str(value))
        while value_index < max_index_uni:
            value_index += 1

    print(unique)
    print("Types of displays possible:")
    print("Bar chart, Histogram, Pie chart, Line graph")

data_summarize(df)

# User should actually should choose fields; those get put in as parameters
def pivot_table(df):
    piv_tab = pd.pivot_table(df, values="Age", index=["Name", "Zip Code"], columns=["Gender"], aggfunc="sum")
    return piv_tab

print("Pivot Table")
print(pivot_table(df))

#just trying out things
import plotly.express as px
def bar_chart(data, x=None, y=None, title=None):
    fig = px.bar(df, x = "Age", y = "Gender", title = "Bar Chart")
    fig.show()
#not sure how to make parameters work
bar_chart(df, x = "Age", y = "Gender", title = "Bar Chart")

# Prompt user for input based on above
# TODO implement this
print("plotting a histogram of Age...")
viz.histogram(df['Age'])



