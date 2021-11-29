import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("ProjectData.csv")
data = df["Avg Rating"].tolist()

Distribution = ff.create_distplot([data], ["Rating Distribution"], show_hist=True)
Distribution.show()