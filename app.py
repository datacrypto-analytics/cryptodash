import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("bitcoin_daily.csv")

data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d")
data.sort_values("date", inplace=True)

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])



external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "DataCrypto Analytics - Software"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
				html.Img(src=app.get_asset_url('logo-datacrypto-analytics.png'), className="image"),
            ],
            className="header",
        ),



		html.Div(
			children=[
				html.Label('Criptomoeda '),
				    dcc.Input(value=' ₿ Bitcoin', type='text'),
			],
			className="input"		
		),


        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": True},
                        figure={
                            "data": [
                                {
                                    "x": data["date"],
                                    "y": data["dpr"],
                                    "type": "lines",
                                    "hovertemplate": "$%{y:.2f}"
                                                     "<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Preço Fechamento",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": False},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": False,
                                },
                                "colorway": ["#212121"],
                            },
                        }, className="card",
                    ),
                    
                ),


				
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": True},
                        figure={
                            "data": [
                                {
                                    "x": data["date"],
                                    "y": data["txs"],
                                    "type": "bar",
                                  
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Transações",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": False},
                                "yaxis": {"fixedrange": False},
                                "colorway": ["#ff8c05"],
                            },
                        },
                    ),
                    className="card-vol",
                ),
            ],
            className="wrapper",
        ),


                html.Div(
                    children=dcc.Graph(
                        id="price-chart-tx",
                        config={"displayModeBar": True},
                        figure={
                            "data": [
                                {
                                    "x": data["date"],
									"y": data["dmv"],
                                    "type": "bar",
                                    "hovertemplate": "$%{y:.2f}"
                                                     "<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Valor médio da transação (USD)",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": False},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": False,
                                },
                                "colorway": ["#212121"],
                            },
                        }, className="tx",
                    ),
                    
                ),


                html.Div(
                    children=dcc.Graph(
                        id="dif",
                        config={"displayModeBar": True},
                        figure={
                            "data": [
                                {
                                    "x": data["date"],
									"y": data["dif"],
                                    "type": "bar",
                                    "hovertemplate": "%{y:.2f}"
                                                     "<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Difficulty",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": False},
                                "yaxis": {
                                    "tickprefix": "",
                                    "fixedrange": False,
                                },
                                "colorway": ["#1b1f22"],
                            },
                        }, className="dif",
                    ),
                    
                ),


                html.Div(
                    children=dcc.Graph(
                        id="out",
                        config={"displayModeBar": True},
                        figure={
                            "data": [
                                {
                                    "x": data["date"],
									"y": data["out"],
                                    "type": "bar",
                                    "hovertemplate": "$%{y:.2f}"
                                                     "<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Saída total do bloco",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": False},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": False,
                                },
                                "colorway": ["#1b1f22"],
                            },
                        }, 
						className="out",
                    ),
                    
                ),
 html.Div(
	children=dcc.Markdown('''


### [Termos Legais](https://datacryptoanalytics.com/termos-legais)   -    [Política Privacidade](https://datacryptoanalytics.com/privacy-policy) 

COPYRIGHT © ALL RIGHTS RESERVED : [DATACRYPTO ANALYTICS.](https://datacryptoanalytics.com/)


'''),
className="mark",
),

    ]
)



if __name__ == "__main__":
    app.run_server(debug=True)
