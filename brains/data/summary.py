import pandas as pd

def df_summary(df):
    dtypes = df.dtypes
    dtypes.name="type"
    nunique=df.nunique()
    nunique.name="nuinque"
    summary = pd.merge(dtypes,nunique,right_index=True,left_index=True)

    return summary
