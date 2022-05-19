import plotly.graph_objects as go
from plotly.subplots import make_subplots

def DoublePlot(df , x , y1 , y2):
    '''
    Gráfica que contiene dos series de puntos con dos escalas distintas, pero que comparten el eje X 
    Input:  df -> Dataframe - con los datos a graficar
            x -> String - nombre de la columna común del df
            y1 -> String - nombre de la columna del df con la primer serie de datos
            y2 -> String - nombre de la columna del df con la segunda serie de datos 
    Output: Figura de Graph Objects
    '''
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig. add_trace(go.Scatter(x=df[x], y=df[y1], mode="lines+markers", name=y1), secondary_y=False)
    fig. add_trace(go.Scatter(x=df[x], y=df[y2], mode="lines+markers", name=y2), secondary_y=True)
    fig.update_yaxes(title_text=y1, secondary_y=False)
    fig.update_yaxes(title_text=y2, secondary_y=True)
    return fig