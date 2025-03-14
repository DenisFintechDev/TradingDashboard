# This is a sample code for an interactive trading dashboard using Plotly and Dash.
# It visualizes sample stock price data and includes interactive elements.
# To run locally: pip install dash plotly, then run this script and visit http://127.0.0.1:8050/.

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data (replace with real data from IBKR API in a production environment)
data = pd.DataFrame({
    "Date": pd.date_range(start="2025-01-01", periods=30, freq="D"),
    "Price": [100, 102, 101, 105, 104, 107, 108, 110, 112, 111, 
              115, 116, 118, 120, 119, 122, 125, 123, 127, 130, 
              132, 135, 138, 140, 139, 142, 145, 143, 148, 150],
    "Volume": [2000, 2200, 2100, 2500, 2400, 2700, 2800, 3000, 3100, 2900, 
               3200, 3300, 3400, 3500, 3400, 3600, 3700, 3600, 3800, 3900, 
               4000, 4100, 4200, 4300, 4200, 4400, 4500, 4400, 4600, 4700]
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Create a Plotly figure for price and volume
fig_price = px.line(data, x="Date", y="Price", title="Stock Price Over Time")
fig_volume = px.bar(data, x="Date", y="Volume", title="Trading Volume Over Time")

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children="Interactive Trading Dashboard"),
    
    html.Div(children='''
        A simple dashboard to analyze stock price and volume data.
    '''),

    dcc.Graph(
        id="price-graph",
        figure=fig_price
    ),

    dcc.Graph(
        id="volume-graph",
        figure=fig_volume
    ),

    html.Div(children='''
        Built by Denis Shevchenko for market analysis.
    ''')
])

# Run the app (commented out for GitHub demo)
# if __name__ == "__main__":
#     app.run_server(debug=True)
