# import brains.data.url as url
from brains.data import url
from brains.viz import matplotlib_viz
# import brains.viz.viz as viz
from brains.viz import plotly_viz as pp
import urllib.error

import pandas as pd
# import brains.viz.viz as viz
import plotly.express as px

import brains.data.url as url


# Test this whole thing with csv Top 50 Employers Kauai
# TODO actually make a main function and/or wrap this into flask implementation

# Load data
# TODO prompt user to designate path
#path = "sample_data/example.csv"
#df = url.path_to_dataframe(path)

# Display summary of data
# Also tutorial for user as he goes along (suggesting what values to choose in pivot table
# based off of what is given in data summary)
# e.g. suggesting to use values that aren't unique, columns will be ideally 10 or less fields

# Can't figure out how to get rid of trailing and leading whitespace for columns
# Function to summarize dataset
def data_summarize(df):
    pd.set_option('display.float_format', lambda x: '%.0f' % x)
    print("-- Data summary --\n")
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
    print("* Suggested column fields: 10 unique values or less * \n")
    print("Types of displays possible:")
    print("Bar Chart, Histogram, Pie Chart, Line Graph \n")

# User prompted to enter dataset
# User enters dataset url
# Loops til user enter correct csv url
# while True:
#     try:
#         path = input("Please enter the csv url for data visualization: \n")
#         df = url.path_to_dataframe(path)
#         break

path = input("Please enter the csv url for data visualization: \n")
df = url.path_to_dataframe(path)

#TODO make module/function for this
# e.g. data.summarize(df)
#
#     except FileNotFoundError as fnfe:
#         print("That is not a correct csv url, please try again.")
#     except urllib.error.HTTPError as ur:
#         print("That is not a correct csv url, please try again.")
#     except urllib.error.URLError as ure:
#         print("That is not a correct csv url, please try again.")

# User views data summary
data_summarize(df)

# User chooses fields for pivot table
# NOTE: not sure how x, y, color values should correspond to pivot table fields

    # NOTE: Annual Sales has a space after (need to correct, but for now type extra space at end)
print("From the columns listed previously, choose your fields for your pivot table.")
print("Please enter it exactly how it is shown under Columns.")

def user_generation():
    try:
        user_columns = input("Please enter columns for your pivot table: ")  # Enter Private-Govt
        user_index = input("Please enter the rows for your pivot table: ") # Enter Contact Gender
        user_values = input("Please enter values for your pivot table: ")  # Enter Annual Sales with space at end

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
        # User then generates one of the visualization options -- Bar Chart, Histogram, Pie Chart, Line Graph (letter for letter correct)
        # Just one of the visualization options -- Bar Chart
        data_vis_options = ["Bar Chart", "Histogram", "Pie Chart", "Line Graph"]
        print("Choices for graph: Bar Chart, Histogram, Pie Chart, Line Graph")
        user_graph = input("Please enter the type of graph you would like to generate: \n")
        user_graph_title = input("Please enter the title of your graph: \n")

        while True:
            if user_graph == "Bar Chart":
                def bar_chart(df, x, y, color, title):
                    fig = px.bar(df, x=x, y=y, color=color, title=title)
                    fig.show()
                bar_chart(df, x=user_columns, y=user_values, color=user_index, title=user_graph_title)
                break

            elif user_graph == "Histogram":
                def histogram(df, x, title):
                    fig = px.histogram(df, x=x, title=title)
                    fig.show()
                histogram(df, x=user_columns, title=user_graph_title)
                break

            elif user_graph == "Pie Chart":
                def pie_chart(df, values, names, title):
                    fig = px.pie(df, values=values, names=names, title=title)
                    fig.show()
                pie_chart(df, values=user_values, names=user_columns, title=user_graph_title)
                break

            elif user_graph == "Line Graph":
                def line_chart(df, x, y, color, title):
                    fig = px.line(df, x=x, y=y, color = color, title=title)
                    fig.show()
                line_chart(df, x=user_columns, y=user_values, color=user_index, title=user_graph_title)
                break

            else:
                print("Incorrect type of data visualization option. Please try again.")
        # User then generates one of the visualization options -- Bar Chart, Histogram, Pie Chart, Line Graph

    except KeyError as ke:
        print('Key Not Found in Columns under Data Summary:', ke)
        print("Please try to enter chosen field exactly how it appears under Columns.")

user_generation()
while True:
    redo = input("Do you want to redo pivot table and graph fields?(Y/N)")
    redo.strip().lower()
    if redo == "y":
        user_generation()
        break
    elif redo == "n":
        break
    else:
        print("Invalid response, please try again")

# CONTINUE PROGRAM: Does user want to redo graph?
# Just ends if error, find way to retrace back to input where error occured

# Prompt user for input based on above
# TODO implement this
# print("plotting a histogram of Age...")
# viz.histogram(df['Age'])

# series_columns = df.columns
# index_string = ""
# for column in series_columns:
#     ref_column = column.strip()
#     index_string += ref_column + "|"
# index_list = list(index_string.split("|"))
# print(', '.join(index_list))
# df = df.reindex(index_list)


