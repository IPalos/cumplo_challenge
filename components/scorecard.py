from dash import html
import dash_bootstrap_components as dbc

def ScoreCard(title, value):
	'''
	Crea un componente estético para mostrar un dato numérico con su título
	Input:	title -> título del dato
					value -> valor numérico a mostrar
	Output:	Componente de Plotly Dash
	'''

	return html.Div([
		dbc.Card(
			dbc.CardBody([
					html.Div(title, className='card-title scorecard-title'),
					html.Div(value, className='card-text scorecard-data')
			]),
		className='scorecard'
		)
	])