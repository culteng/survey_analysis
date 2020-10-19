# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd
import lorem
import pathlib

if False:
    # Path
    BASE_PATH = pathlib.Path(__file__).parent.resolve()
    DATA_PATH = BASE_PATH.joinpath("data/cleaned").resolve()

    ## Read in data
    survey = pd.read_csv(DATA_PATH.joinpath("student-diversity-survey_20200911_213237.csv"))


survey = pd.read_csv("data/cleaned/student-diversity-survey_20200911_213237.csv")


# Colours
color_1 = "#003399"
color_2 = "#00ffff"
color_3 = "#002277"
color_b = "#F8F8FF"

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div(
    children=[
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src=app.get_asset_url(
                                                            "./imgs/logo_strickland.png"
                                                        ),
                                                        className="page-1a",
                                                    )
                                                ),
                                                html.Div(
                                                    [
                                                        html.H6("Suscipit nibh"),
                                                        html.H5("LOREM IPSUM DOLOR"),
                                                        html.H6("Blandit pretium dui"),
                                                    ],
                                                    className="page-1b",
                                                ),
                                            ],
                                            className="page-1c",
                                        )
                                    ],
                                    className="page-1d",
                                ),
                                html.Div(
                                    [
                                        html.H1(
                                            [
                                                html.Span("03", className="page-1e"),
                                                html.Span("19"),
                                            ]
                                        ),
                                        html.H6("Suscipit nibh vita"),
                                    ],
                                    className="page-1f",
                                ),
                            ],
                            className="page-1g",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6("Felecia Conroy", className="page-1h"),
                                        html.P("453-264-8591"),
                                        html.P("ilq@w.ipq"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Olin Dach", className="page-1h"),
                                        html.P("497-234-2837r"),
                                        html.P("isw@vxogiqyds.umf"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "Dominique Durgan", className="page-1h"
                                        ),
                                        html.P("913-823-9541"),
                                        html.P("rgd@hp.xji"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Abraham Lemke", className="page-1h"),
                                        html.P("248-865-2687"),
                                        html.P("mc@a.kur"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Abraham Lemke", className="page-1h"),
                                        html.P("284-671-3721"),
                                        html.P("j@jdvwnqucm.etv"),
                                    ],
                                    className="page-1i",
                                ),
                            ],
                            className="page-1j",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            "Viverra, imperdiet, praesent pellentesque",
                                            className="page-1h",
                                        ),
                                        html.P(lorem.paragraph() * 2),
                                    ],
                                    className="page-1k",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "Facilisis mauris parturient, eget vitae",
                                            className="page-1h",
                                        ),
                                        html.P(lorem.paragraph() * 2),
                                    ],
                                    className="page-1l",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "A suspendisse mauris aliquam tincidunt hac",
                                            className="page-1h",
                                        ),
                                        html.P(lorem.paragraph() * 2),
                                    ],
                                    className="page-1m",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "A elementum lorem dolor aliquam nisi diam",
                                            className="page-1h",
                                        ),
                                        html.P(lorem.paragraph()),
                                    ],
                                    className="page-1l",
                                ),
                            ],
                            className="page-1n",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
        # Page 2
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H1("LOREM IPSUM")], className="page-2a"),
                        html.Div(
                            [
                                html.P(lorem.paragraph() * 3, className="page-2b"),
                                html.P(lorem.paragraph() * 2, className="page-2c"),
                                html.P(lorem.paragraph() * 2, className="page-2c"),
                            ],
                            className="page-3",
                        ),
                        html.Div(
                            [
                                html.P(lorem.paragraph() * 2, className="page-2b"),
                                html.P(lorem.paragraph() * 3, className="page-2c"),
                            ],
                            className="page-3",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
        # Page 3
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H1("LOREM IPSUM")], className="page-3a"),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H6(
                                                    "Mauris feugiat quis lobortis nisl sed",
                                                    className="page-3b",
                                                ),
                                                html.P(
                                                    lorem.paragraph(),
                                                    className="page-3c",
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.P(
                                                            lorem.paragraph() * 2,
                                                            className="page-3d",
                                                        )
                                                    ],
                                                    className="page-3e",
                                                ),
                                                html.Div(
                                                    [
                                                        html.P(
                                                            lorem.paragraph() * 2,
                                                            className="page-3d",
                                                        )
                                                    ],
                                                    className="page-3f",
                                                ),
                                                html.Div(
                                                    [
                                                        html.P(
                                                            lorem.paragraph(),
                                                            className="page-3d",
                                                        )
                                                    ],
                                                    className="page-3g",
                                                ),
                                            ],
                                            className="page-3i",
                                        ),
                                        html.Div(
                                            [
                                                html.P(
                                                    lorem.paragraph(),
                                                    className="page-2c",
                                                )
                                            ]
                                        ),
                                    ],
                                    className="page-3j",
                                )
                            ]
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
        # Page 4
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Strong(
                                                    "Ultricies fusce vel, ad ultricies enim, at, egestas",
                                                    className="page-3h",
                                                ),
                                                html.P(
                                                    "Quis mauris dolor amet cubilia mattis, finibus magnis lacus",
                                                    className="page-3k",
                                                ),
                                            ],
                                            className="title six columns",
                                        ),
                                        html.Div(
                                            [
                                                html.Strong(
                                                    "Feugiat justo, aliquam feugiat justo suspendisse leo blandit",
                                                    className="page-3h",
                                                ),
                                                html.P(
                                                    "Praesent, morbi, rhoncus habitant at maximus mauris",
                                                    className="page-3k",
                                                ),
                                            ],
                                            className="title six columns",
                                        ),
                                    ],
                                    className="thirdPage first row",
                                )
                            ],
                            className="page-3l",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        dcc.Graph(
                                                            figure={
                                                                "data": [
                                                                    go.Scatter(
                                                                        x=survey[
                                                                            "grade"
                                                                        ],
                                                                        y=survey[
                                                                            "scl_ldrshp"
                                                                        ],
                                                                        hoverinfo="y",
                                                                        line={
                                                                            "color": color_1,
                                                                            "width": 1.5,
                                                                        },
                                                                        name="Demand",
                                                                    ),
                                                                ],
                                                                "layout": go.Layout(
                                                                    height=250,
                                                                    xaxis={
                                                                        "range": [
                                                                            1988,
                                                                            2015,
                                                                        ],
                                                                        "showgrid": False,
                                                                        "showticklabels": True,
                                                                        "tickangle": -90,
                                                                        "tickcolor": "#b0b1b2",
                                                                        "tickfont": {
                                                                            "family": "Arial",
                                                                            "size": 9,
                                                                        },
                                                                        "tickmode": "linear",
                                                                        "tickprefix": "1Q",
                                                                        "ticks": "",
                                                                        "type": "linear",
                                                                        "zeroline": True,
                                                                        "zerolinecolor": "#FFFFFF",
                                                                    },
                                                                    yaxis={
                                                                        "autorange": False,
                                                                        "linecolor": "#b0b1b2",
                                                                        "nticks": 9,
                                                                        "range": [
                                                                            -3000,
                                                                            5000,
                                                                        ],
                                                                        "showgrid": False,
                                                                        "showline": True,
                                                                        "tickcolor": "#b0b1b2",
                                                                        "tickfont": {
                                                                            "family": "Arial",
                                                                            "size": 9,
                                                                        },
                                                                        "ticks": "outside",
                                                                        "ticksuffix": " ",
                                                                        "type": "linear",
                                                                        "zerolinecolor": "#b0b1b2",
                                                                    },
                                                                    margin={
                                                                        "r": 10,
                                                                        "t": 5,
                                                                        "b": 0,
                                                                        "l": 40,
                                                                        "pad": 2,
                                                                    },
                                                                    hovermode="closest",
                                                                    legend={
                                                                        "x": 0.5,
                                                                        "y": -0.4,
                                                                        "font": {
                                                                            "size": 9
                                                                        },
                                                                        "orientation": "h",
                                                                        "xanchor": "center",
                                                                        "yanchor": "bottom",
                                                                    },
                                                                ),
                                                            }
                                                        )
                                                    ],
                                                    className="page-3m",
                                                )
                                            ],
                                            className="six columns",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src=app.get_asset_url(
                                                            "./imgs/logo_strickland.png"
                                                        ),
                                                        className="page-1a",
                                                    )
                                                )
                                            ],
                                            className="page-3m",
                                        ),
                                    ],
                                    className="thirdPage row",
                                )
                            ],
                            className="page-7",
                        ),
                        html.Div(
                            [
                                html.P("Bibendum tellus phasellus turpis sapien:"),
                                html.P(
                                    lorem.paragraph() * 2,
                                    style={
                                        "border-left": "5px",
                                        "border-left-style": "solid",
                                        "padding": "30px",
                                        "border-left-color": color_1,
                                        "padding-left": "20px",
                                        "border-left-width": "7px",
                                        "background-color": color_b,
                                    },
                                ),
                            ],
                            style={
                                "float": "left",
                                "margin-top": "20px",
                                "margin-left": "30px",
                            },
                            className="eleven columns",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Strong(
                                            "Ultricies fusce vel, ad ultricies enim, at, egestas",
                                            style={
                                                "color": color_1,
                                                "padding-top": "100px",
                                            },
                                        ),
                                        html.P(
                                            "Quis mauris dolor amet cubilia mattis, finibus magnis lacus",
                                            className="page-3k",
                                        ),
                                    ],
                                    className="title six columns",
                                ),
                                html.Div(
                                    [
                                        html.Strong(
                                            "Feugiat justo, aliquam feugiat justo suspendisse leo blandit",
                                            className="page-3h",
                                        ),
                                        html.P(
                                            "Praesent, morbi, rhoncus habitant at maximus mauris",
                                            className="page-3k",
                                        ),
                                    ],
                                    className="title six columns",
                                ),
                            ],
                            className="thirdPage first row",
                            style={
                                "position": "relative",
                                "top": "20px",
                                "margin-left": "30px",
                            },
                        ),
                        html.Div(
                            [
                                html.Div(
                                                    html.Img(
                                                        src=app.get_asset_url(
                                                            "./imgs/logo_strickland.png"
                                                        ),
                                                        className="page-1a",
                                                    )
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                                    html.Img(
                                                        src=app.get_asset_url(
                                                            "./imgs/logo_strickland.png"
                                                        ),
                                                        className="page-1a",
                                                    ),
                                            className="exhibit six columns",
                                        )
                                    ],
                                    className="page-2c",
                                ),
                            ],
                            className="page-7",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
