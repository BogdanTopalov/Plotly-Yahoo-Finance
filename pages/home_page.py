from dash import html, register_page


register_page(__name__, path='/')

layout = html.Div([
    html.H1('Multi-page Stock Ticker Dashboard', id='home-title'),
])