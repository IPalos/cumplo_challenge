from dash import dash_table

def BmxTable(df):
    '''
    Componente que crea la tabla de fecha, UDIS y USD
    Input: DataFrame para tabular
    Output: Componente de Plotly Dash
    '''
    return dash_table.DataTable(
                    df.to_dict('records'),
                    [{"name": i, "id": i} for i in df.columns],
                    style_table={
                        'height': 450,
                        'overflowY': 'scroll',
                    }
                )
