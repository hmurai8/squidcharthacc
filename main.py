import pandas as pd

import brains.data.url as url
import brains.viz.viz as viz



# TODO actually make a main function and/or wrap this into flask implementation

# Load data
# TODO prompt user to designate path
#path = "sample_data/example.csv"
#df = url.path_to_dataframe(path)

# User prompted to enter dataset
# User enters dataset url
path = input("Please enter the csv url for data visualization: \n")
df = url.path_to_dataframe(path)

# Display summary of data
# Also tutorial for user as he goes along (suggesting what values to choose in pivot table
# based off of what is given in data summary)
# e.g. suggesting to use values that aren't unique, columns will be ideally 10 or less fields
#TODO make module/function for this
# e.g. data.summarize(df)

# Function to summarize dataset
def data_summarize(df):
    import pandas as pd
    pd.set_option('display.float_format', lambda x: '%.0f' % x)
    print("General Dataset Information")
    print(df.info())
    print("Columns:")
    print(', '.join(df.columns))
    print("Types of data:")
    print(df.dtypes)
    print("Object Count")
    print("Numeric data aggregation:")
    print(df.describe().loc[['count','max', 'min', 'mean']])
    print("Sum of numeric data: ")
    print(df.sum(numeric_only=True))
    print("Number of unique values for all columns:")
    print(df.nunique())
    print("* Suggested column fields: 10 unique values or less *")
    print("Types of displays possible:")
    print("Bar Chart, Histogram, Pie Chart, Line Graph")

# User views data summary
data_summarize(df)

# User chooses fields for pivot table
# NOTE: not sure how x, y, color values should correspond to pivot table fields
print("From the current columns listed above, choose your fields for your pivot table.")
print("Please enter it exactly how it is shown under Columns.")
user_values = input("Please enter values for your pivot table (y values) : ")
user_index = input("Please enter the index for your pivot table (color) : ")
user_columns = input("Please enter columns for your pivot table (x values) : ")

# Pivot table generated based off of user input (if user inputted correctly)
def pivot_table(df, values, index, columns, aggfunc):
    piv_tab = pd.pivot_table(
        df, values=values,
        index=index,
        columns=columns,
        aggfunc=aggfunc
    )
    return piv_tab

print("--- Pivot Table ---")
print(pivot_table(df,
        values=[user_values],
        index=[user_index],
        columns=[user_columns],
        aggfunc="sum"))

# Prompt user to enter type of data visualization
user_graph = input("Please enter the type of graph you would like to generate: \n")

# User then generates one of the visualization options -- Bar Chart, Histogram, Pie Chart, Line Graph

# Just one of the visualization options -- Bar Chart
import plotly.express as px
def bar_chart(df, x, y, color, title):
    fig = px.bar(df,x=x,y=y,color = color, title=title)
    fig.show()

bar_chart(df, x = user_columns, y = user_values, color = user_index, title = "Bar Chart")
# Customize title option??

# Prompt user for input based on above
# TODO implement this
print("plotting a histogram of Age...")
viz.histogram(df['Age'])

# Just example data visualization (top 50 employers kauai)
path = "sample_data/top-50-employers-kauai.csv"
df = url.path_to_dataframe(path)

fig = px.bar\
        (df,
        x= 'Private-Govt',
        y = 'Annual Sales',
        color = 'Contact Gender',
        title = 'Annual Sales by Sector and Gender'
        )
fig.show()



