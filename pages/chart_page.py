from dash import dcc, html, Input, Output, register_page, callback
from utils import TICKERS, PERIODS, get_ticker_data
import plotly.express as px


register_page(__name__, path='/ticker-chart')


layout = html.Div([
    html.H1('Ticker Line Chart'),
    dcc.RadioItems(
        options=TICKERS,
        value='AAPL',
        id='tickers-dropdown',
        inline=True,
        className="period-tabs"
    ),
    dcc.RadioItems(
        options=PERIODS,
        value='1mo',
        id='periods-dropdown',
        inline=True,
        className="period-tabs"
    ),  
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('tickers-dropdown', 'value'),
    Input('periods-dropdown', 'value')
)
def update_graph(ticker, period):
    ticker_df = get_ticker_data(ticker, period)
    return px.line(ticker_df, x='Date', y='Close', title=ticker)
