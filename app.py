# app.py
from dash import Dash, html, dcc, page_container
from cache_config import cache


app = Dash(
    title="Stock Ticker Dashboard",
    use_pages=True
)

cache.init_app(app.server, config={
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
})

app.layout = html.Div([
    html.Header([
        dcc.Link("Home", href="/"),
        dcc.Link("Chart", href="/ticker-chart"),
        dcc.Link("Table", href="/ticker-table"),
    ]),
    page_container
])


if __name__ == "__main__":
    app.run(debug=True)
