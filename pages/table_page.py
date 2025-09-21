from dash import dcc, html, Input, Output, register_page, callback 
import dash_ag_grid as dag
from utils import TICKERS, PERIODS, get_ticker_data


register_page(__name__, path='/ticker-table')


layout = html.Div([
    html.H1('Ticker Data Table'),
    dcc.RadioItems(
        TICKERS, 
        'AAPL', 
        id='table-tickers-dropdown', 
        inline=True, 
        className="period-tabs"
    ),
    dcc.RadioItems(
        PERIODS, 
        '1mo', 
        id='table-periods-radio', 
        inline=True, 
        className="period-tabs"
    ),
    dag.AgGrid(
        id='ticker-grid',
        columnDefs=[
            {'field': c} 
            for c in ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']
        ],
        rowData=[],
        dashGridOptions={
            "pagination": True, 
            "paginationPageSize": 10,
            "domLayout": "autoHeight",
            "defaultColDef": {"resizable": True}
        },
        columnSize="sizeToFit"
    )
])

@callback(
    Output('ticker-grid', 'rowData'),
    Input('table-tickers-dropdown', 'value'),
    Input('table-periods-radio', 'value')
)
def update_table(ticker, period):
    ticker_df = get_ticker_data(ticker, period)
    return ticker_df.to_dict('records')