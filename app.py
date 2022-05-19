# Commons
import datetime
import flask
from components.tiieplot import TiiePlot

# Dash Libraries
from dash import Dash, html, dcc , callback, Input, Output
import dash_bootstrap_components as dbc

# Local components
from components.cardplot import CardPlot
from components.doubleplot import DoublePlot
from components.scorecard import ScoreCard
from components.bmxtable import BmxTable

# Data Processing
from utils.data_processing import get_tiies, get_udis_usd

# Constants
from utils.constants import *

# Initial config
server = flask.Flask(__name__)
app = Dash(
    __name__,
    suppress_callback_exceptions=True, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
    ],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)


# App Layout
app.layout = html.Div([

    html.Div([

        # Date Picker
        html.H2("Seleccionar intervalo de fechas"),
        dcc.DatePickerRange(
            id='fechas',
            min_date_allowed=datetime.date(1990, 1, 1),
            max_date_allowed=datetime.date.today(),
            initial_visible_month=datetime.date(2000, 1, 1),
            start_date = datetime.date(2022,1,1),
            end_date=datetime.date.today()
        ),
        html.Br(),
        html.Br(),

        # Scorecards UDIS USD
        html.Div([
            html.H2("UDIS"),
            dbc.Row(id = "scorecards-udis"),
            html.H2("USD"),
            dbc.Row(id = "scorecards-dlrs"),
            ],
            className='container scorecard-container'
        ),

    ], className="container scorecard-container"),

    # UDIS USD Plot and table
    html.Div([
        dbc.Row([
            dbc.Col(CardPlot(id="udi-usd-plot"), width=9),
            dbc.Col(id="tbl", width=3)
        ]),
        ],
        className='container scorecard-container'
    ),

    html.Br(),

    # TIIEs Plot and table
    html.Div([
        dbc.Row([
            dbc.Col(CardPlot(id="tiie-plot"), width=9),
            dbc.Col(id="tiie-tbl", width=3)
        ]),
        ],
        className='container scorecard-container'
    ),


])

@app.callback(
    Output("udi-usd-plot", "figure"),
    Output("tbl", "children"),
    Output("scorecards-udis", "children"),
    Output("scorecards-dlrs", "children"),
    Output("tiie-plot", "figure"),
    Input("fechas", "start_date"),
    Input("fechas", "end_date"))
def update_data(start_date, end_date):
    df , (mean_u, mi_u, ma_u) ,(mean_d, mi_d, ma_d) = get_udis_usd(f'{s_udis},{s_dolar}', start_date, end_date)
    fig = DoublePlot(df, "fecha", "USD/MXN", "UDIS/MXN")
    tbl = BmxTable(df)

    scorecards_udis = [dbc.Col(ScoreCard("Promedio", mean_u), width=4),
                    dbc.Col(ScoreCard("Mínimo", mi_u),width=4),
                    dbc.Col(ScoreCard("Máximo", ma_u),width=4)]
    scorecards_dlr = [dbc.Col(ScoreCard("Promedio", mean_d), width=4),
                    dbc.Col(ScoreCard("Mínimo", mi_d),width=4),
                    dbc.Col(ScoreCard("Máximo", ma_d),width=4)]
    tiies = get_tiies(f'{s_tiie_obj},{s_tiie_1},{s_tiie_28},{s_tiie_91},{s_tiie_182}',start_date,end_date)
    a=list(tiies.columns[1:])
    tiies_plot = TiiePlot(tiies, "fecha", a, a)

    return fig , tbl, scorecards_udis, scorecards_dlr, tiies_plot

# Run server
if __name__ == '__main__':
    app.run_server(debug=True)