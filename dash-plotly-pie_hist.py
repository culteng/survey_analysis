import pandas as pd
import glob
from plotly.offline import init_notebook_mode,iplot
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# import cufflinks as cf

# local import
import analysis

# readin data
filenames = glob.glob("data/cleaned/*.csv")
df = analysis.populate_df(filenames)

# defining data
trace = go.Histogram(x=df['scl_happy'],nbinsx=40,histnorm='percent')
data = [trace]
# defining layout
layout = go.Layout(
	title="Happiness Distribution", 
	xaxis={'tickformat': ',d'}, 
	bargroupgap = 0,
	bargap=0 #,    updatemenus=list([dict(buttons= list_updatemenus)])
    )
# defining figure and plotting
fig = go.Figure(data = data,layout = layout)
fig.write_html("output/pltly_hist.html")


########### GROUP HIST
x0 = df[df['ethnicity']=='b']['scl_happy']
x1 = df[df['ethnicity']=='l']['scl_happy']

fig = go.Figure()
fig.add_trace(go.Histogram(
    x=x0,
    histnorm='percent',
    name='black', # name used in legend and hover labels
    marker_color='#EB89B5',
    opacity=0.75
))
fig.add_trace(go.Histogram(
    x=x1,
    histnorm='percent',
    name='latina',
    marker_color='#330C73',
    opacity=0.75
))

fig.update_layout(
    title_text='Q 1.3 - Happiness?', # title of plot
    xaxis_title_text='Value', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
)


# Creates a list of dictionaries, which have the keys 'label' and 'value'.
def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list
    

html.Div(className='div-for-dropdown',
          children=[
              dcc.Dropdown(id='stockselector',
                           options=get_options(df['stock'].unique()),
                           multi=True,
                           value=[df['stock'].sort_values()[0]],
                           style={'backgroundColor': '#1E1E1E'},
                           className='stockselector')
                    ],
          style={'color': '#1E1E1E'})
          

@app.callback(Output('timeseries', 'figure'),
              [Input('stockselector', 'value')])
def update_timeseries(selected_dropdown_value):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    # STEP 1
    trace = []  
    df_sub = df
    # STEP 2
    # Draw and append traces for each stock
    for stock in selected_dropdown_value:   
        trace.append(go.Scatter(x=df_sub[df_sub['stock'] == stock].index,
                                 y=df_sub[df_sub['stock'] == stock]['value'],
                                 mode='lines',
                                 opacity=0.7,
                                 name=stock,
                                 textposition='bottom center'))  
    # STEP 3
    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    # STEP 4
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Stock Prices', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
              ),

              }

    return figure


fig.write_html("output/pltly_hist_eth2.html")



'''
if __name__ == '__main__':
    app.run_server(debug=True)
'''