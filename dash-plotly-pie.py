import pandas as pd
import glob
import plotly.graph_objects as go

filenames = glob.glob("data/cleaned/*.csv")
df = analysis.populate_df(filenames)

#labels
lab = df["gender"].value_counts().keys().tolist()
lab = ['Female', 'Male']
#values
val = df["gender"].value_counts().values.tolist()
trace = go.Pie(labels=lab, 
                values=val, 
                marker=dict(colors=['red']), 
                # Seting values to 
                hoverinfo="value"
              )
data = [trace]
layout = go.Layout(title="Gender Split")
fig = go.Figure(data = data,layout = layout)
fig.write_html("output/pltly_circle.html")