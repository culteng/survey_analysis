# Get this figure: fig = py.get_figure("https://plotly.com/~hyang0177/6/")
# Get this figure's data: data = py.get_figure("https://plotly.com/~hyang0177/6/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="ANOVA for 5 tests", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plotly.com/~hyang0177/6/").get_data()[0]["y"]

# Get figure documentation: https://plotly.com/python/get-requests/
# Add data documentation: https://plotly.com/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plotly.com/python/getting-started
# Find your api_key here: https://plotly.com/settings/api

import plotly.graph_objects as go
import pandas as pd
import glob

import analysis

filenames = glob.glob("data/cleaned/*.csv")
df = analysis.populate_df(filenames)

x0 = df[df['i_am_a']=='student']['scl_happy']
x1 = df[df['i_am_a']=='parent']['scl_happy']
x2 = df[df['i_am_a']=='teacher']['scl_happy']
x3 = df[df['i_am_a']=='staff']['scl_happy']


trace1 = {
          "uid": "676d10", 
          "line": {"color": "rgb(214, 39, 40)"}, 
          "name": "Students", 
          "type": "box", 
          "y": x0,
          "fillcolor": "rgba(214, 39, 40, 0.47)"
        }
trace2 = {
          "uid": "67abba", 
          "line": {"color": "rgb(100, 39, 40)"}, 
          "name": "Parents", 
          "type": "box", 
          "y": x1
        }
trace3 = {
          "uid": "88c7cc", 
          "line": {"color": "rgb(0, 39, 40)"}, 
          "name": "Teachers", 
          "type": "box", 
          "y": x2 
        }
trace4 = {
          "uid": "39976f", 
          "line": {"color": "rgb(31, 119, 180)"}, 
          "name": "Staff", 
          "type": "box", 
          "y": x3
        }
data = [trace1, trace2, trace3, trace4]
layout = {
          "font": {
            "size": 12, 
            "color": "rgb(0, 0, 0)", 
            "family": "'Open sans', verdana, arial, sans-serif"
          }, 
          "title": "ANOVA across Survey Groups", 
          "width": 1713, 
          "xaxis": {
            "type": "category", 
            "dtick": 1, 
            "range": [-0.5, 4.5], 
            "tick0": 0, 
            "ticks": "", 
            "title": "Test Numbers", 
            "anchor": "y", 
            "domain": [0, 1], 
            "mirror": False, 
            "nticks": 0, 
            "ticklen": 5, 
            "position": 0, 
            "showgrid": False, 
            "showline": False, 
            "tickfont": {
              "size": 12, 
              "color": "rgb(255, 255, 255)"
            }, 
            "zeroline": False, 
            "autorange": True, 
            "gridcolor": "#eee", 
            "gridwidth": 1, 
            "linecolor": "#444", 
            "linewidth": 1, 
            "rangemode": "normal", 
            "tickangle": 90, 
            "tickcolor": "#444", 
            "tickwidth": 1, 
            "titlefont": {
              "size": 12, 
              "color": "rgb(255, 255, 255)"
            }, 
            "showexponent": "all", 
            "zerolinecolor": "#444", 
            "zerolinewidth": 1, 
            "exponentformat": "B", 
            "showticklabels": True
          }, 
          "yaxis": {
            "type": "linear", 
            "dtick": 10, 
            "range": [13.444444444444443, 104.55555555555556], 
            "tick0": 0, 
            "ticks": "", 
            "title": "Range from 1 (disagree) to 5 (agree)", 
            "anchor": "x", 
            "domain": [0, 1], 
            "mirror": False, 
            "nticks": 0, 
            "ticklen": 5, 
            "position": 0, 
            "showgrid": True, 
            "showline": False, 
            "tickfont": {
              "size": 12, 
              "color": "rgb(255, 255, 255)"
            }, 
            "zeroline": True, 
            "autorange": True, 
            "gridcolor": "#eee", 
            "gridwidth": 1, 
            "linecolor": "#444", 
            "linewidth": 1, 
            "rangemode": "normal", 
            "tickangle": 90, 
            "tickcolor": "#444", 
            "tickwidth": 1, 
            "titlefont": {
              "size": 12, 
              "color": "rgb(255, 255, 255)"
            }, 
            "showexponent": "all", 
            "zerolinecolor": "#444", 
            "zerolinewidth": 1, 
            "exponentformat": "B", 
            "showticklabels": True
          }, 
          "bargap": 0.2, 
          "boxgap": 0.3, 
          "height": 732, 
          "legend": {
            "x": 1.02, 
            "y": 1, 
            "font": {
              "size": 12, 
              "color": "rgb(0, 0, 0)"
            }, 
            "bgcolor": "#fff", 
            "xanchor": "left", 
            "yanchor": "top", 
            "traceorder": "normal", 
            "bordercolor": "#444", 
            "borderwidth": 0
          }, 
          "margin": {
            "b": 80, 
            "l": 80, 
            "r": 80, 
            "t": 100, 
            "pad": 0, 
            "autoexpand": True
          }, 
          "barmode": "group", 
          "boxmode": "overlay", 
          "autosize": True, 
          "dragmode": "zoom", 
          "hovermode": "x", 
          "titlefont": {
            "size": 12, 
            "color": "rgb(255, 255, 255)"
          }, 
          "separators": ".,", 
          "showlegend": True, 
          "bargroupgap": 0, 
          "boxgroupgap": 0.3, 
          "hidesources": False, 
          "plot_bgcolor": "#fff", 
          "paper_bgcolor": "rgb(0, 0, 0)"
        }
fig = go.Figure(data=data, layout=layout)
# plot_url = py.plot(fig)

fig.write_html("output/pltly_anova_box.html")


import scipy.stats as stats
# stats f_oneway functions takes the groups as input and returns F and P-value
fvalue, pvalue = stats.f_oneway(x0, x1, x2, x3)
print(fvalue, pvalue)
if pvalue > .05:
    print('p-value indicates a lack of significant difference across classes')
else:
    print('p-value indicates statiscally significant differences across classes')

