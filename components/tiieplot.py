import plotly.graph_objects as go
from plotly.subplots import make_subplots

def TiiePlot(df , x , ys, names):
    '''
    Grfica que contiene los distintos valores de las TIIEs
    Input:  df -> DataFrame - contiene la información de las distintas series
            x -> String - nombre de la df que representa el eje X de la gráfica
            ys -> List - lista de valores para el eje Y de la gráfica
            names -> List - lista de nombres de cada serie
    Output: Graph Object
    '''
    fig = go.Figure()
    for i in range(len(ys)):
        fig.add_trace(go.Scatter(x=df[x], y=df.loc[:,ys[i]], mode="lines+markers", name=names[i]))
    return fig