import dash
import dash_core_components as dcc
import dash.dependencies as dd
import dash_html_components as html
from dash.dependencies import Input, Output
from wordcloud import WordCloud
from io import BytesIO

import pandas as pd
import plotly.graph_objs as go
import base64

# Dataset Processing

path = 'https://github.com/anasofiapqsilva/Data-Visualization'
df = pd.read_csv(path + 'netflix_df.csv')

# The app itself

app = dash.Dash(__name__, external_stylesheets='')

app.layout = html.Div([
    html.Img(id="image_wc"),
])

def plot_wordcloud(data):
    d = {a: x for a, x in data.values}
    wc = WordCloud(background_color='black', width=480, height=360)
    wc.fit_words(d)
    return wc.to_image()

@app.callback(dd.Output('image_wc', 'src'), [dd.Input('image_wc', 'id')])
def make_image(b):
    img = BytesIO()
    plot_wordcloud(data=df).save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())


if __name__ == '__main__':
    app.run_server(port=8050, host='127.0.0.1')
