import plotly.express as px
import brains.data.url as url

path = "sample_data/top-50-employers-kauai.csv"
df = url.path_to_dataframe(path)

fig = px.bar\
        (df,
        x= 'Private-Govt',
        y = 'Annual Sales',
        color = 'Contact Gender',
        title = 'Age by Zip Code'
        )
fig.show()