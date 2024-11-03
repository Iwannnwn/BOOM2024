import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Membuat contoh data
data = pd.DataFrame({
    "Year" : [2018, 2019, 2020, 2021, 2022, 2023],
    "Value" : [100, 200, 300, 400, 500, 600]
})

# Inisialisasi Aplikasi Dash
app = dash.Dash(__name__)

# Layout dari aplikasi dengan dropdown tambahan
app.layout = html.Div([
    html.H1("Aplikasi Data Interaktif"),
    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label' : 'Value', 'value' : 'Value'}],
        value='Value'
    ),
    dcc.Slider(
        id='year-slider',
        min=data['Year'].min(),
        max=data['Year'].max(),
        value=data['Year'].min(),
        marks={str(year) : str(year) for year in data['Year'].unique()},
        step=None
    ),
    dcc.Graph(id='updated-graph')
])

# Callback untuk memperbaharui grafik
@app.callback(
    Output('updated-graph', 'figure'),
    [Input('year-slider', 'value'),Input('column-dropdown', 'value')]
)

def update_graph(selected_year, selected_column):
    filtered_data = data[data['Year'] <= selected_year]
    fig = px.bar(filtered_data, x='Year', y=selected_column, title='Data Berdasarkan Pilihan')
    return fig

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run_server(debug=True, port=8057)