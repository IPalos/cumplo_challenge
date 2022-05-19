from dash import html, dcc
import dash_bootstrap_components as dbc

def CardPlot(id):
    '''
    Componente que enmarca las gráficas dinámicas en una "Bootstrap Card" con fínes estéticos
    Input: id de la gráfica
    Output: Componente de Plotly Dash
    '''
    return html.Div([
            dbc.Card(
                dbc.CardBody([
                    dcc.Graph(id=id),
                ]),
                className='card-plot'
            ),
        ])
