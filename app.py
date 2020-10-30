import base64, io
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from sklearn.preprocessing import LabelEncoder
import numpy as np


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Plot Playground"),
    html.A("HOME", href="https://tsuchiya-ryo.github.io/orgsynscalc/"),
    html.H2(children="2d-plot"),
    dcc.Dropdown(id="labelside2d",
                options=[
                    {"label":"No label column", "value":"no"},
                    {"label":"Right-side label column", "value":"right"},
                    {"label":"Left-side label column", "value":"left"}
                ],
                value="no",
                style={"height":"30px", "width":"250px"}
                ),
    html.Br(),
    dcc.Upload(
        id='upload-data',
        children=html.A("Click to Select 2d File (or drag and drop)"),
        multiple=True,
        max_size = 500000,
     style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
     }),
    html.Br(),

    dcc.Dropdown(
        id="colorpalette2d",
        options=[
            {"label":"Viridis", "value":"viridis"},
            {"label":"Inferno", "value":"inferno"},
            {"label":"Twilight", "value":"twilight"},
            {"label":"Earth", "value":"earth"},
            {"label":"Tropic", "value":"tropic"},
            {"label":"Icefire","value":"icefire"},
            {"label":"Greys", "value":"greys"},
            {"label":"Electric", "value":"electric"},
            {"label":"Rainbow", "value":"rainbow"},
            {"label":"Plasma", "value":"plasma"},
            {"label":"Picnic", "value":"picnic"},
            {"label":"Speed", "value":"speed"},
            {"label":"Balance", "value":"balance"}
        ],
        value="viridis",
        style={"height":"30px", "width":"150px"}
    ),
    dcc.Dropdown(
        id="opacity2d",
        options=[{"label": round(i, 1), "value": round(i, 1)}\
             for i in np.linspace(0.1, 1, 10) ],
             value=0.5,
             style={"height":"30px", "width":"150px"}
    ),
    dcc.Dropdown(
        id="size2d",
        options=[{"label":round(i,0), "value":round(i,0)}\
            for i in np.linspace(3,12,10)],
            value=5,
            style={"height":"30px", "width":"150px"}
    ),
    html.Br(),

    html.P(id="title2d"),
    dcc.Input(id="xlabel", type="text", value="x"),
    dcc.Input(id="ylabel", type="text", value="y"),

    html.Div([
        html.Div([dcc.Graph(id="example-graph")],
        style={"height":"100%", "width":"100%"})
    ]),


    html.H2(children="3d-plot"),
    dcc.Dropdown(id="labelside3d",
                options=[
                    {"label":"No label column", "value":"no"},
                    {"label":"Right-side label column", "value":"right"},
                    {"label":"Left-side label column", "value":"left"}
                ],
                value="no",
                style={"height":"30px", "width":"250px"}
                ),
    html.Br(),
    dcc.Upload(
        id='upload-data3d',
        children=html.A("Click to Select 3d File (or drag and drop)"),
        multiple=True,
        max_size = 500000,

     style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
     }),
     html.Br(),


    dcc.Dropdown(
        id="colorpalette3d",
        options=[
            {"label":"Viridis", "value":"viridis"},
            {"label":"Inferno", "value":"inferno"},
            {"label":"Twilight", "value":"twilight"},
            {"label":"Earth", "value":"earth"},
            {"label":"Tropic", "value":"tropic"},
            {"label":"Icefire","value":"icefire"},
            {"label":"Greys", "value":"greys"},
            {"label":"Electric", "value":"electric"},
            {"label":"Rainbow", "value":"rainbow"},
            {"label":"Plasma", "value":"plasma"},
            {"label":"Picnic", "value":"picnic"},
            {"label":"Speed", "value":"speed"},
            {"label":"Balance", "value":"balance"}
        ],
        value="viridis",
        style={"height":"30px", "width":"150px"}
    ),
    dcc.Dropdown(
        id="opacity3d",
        options=[{"label": round(i, 1), "value": round(i, 1)}\
             for i in np.linspace(0.1, 1, 10) ],
             value=0.5,
             style={"height":"30px", "width":"150px"}
    ),
    dcc.Dropdown(
        id="size3d",
        options=[{"label":round(i,0), "value":round(i,0)}\
            for i in np.linspace(3,12,10)],
            value=5,
            style={"height":"30px", "width":"150px"}
    ),
    html.Br(),


    html.P(id="title3d"),
    dcc.Input(id="xlabel3d", type="text", value="x"),
    dcc.Input(id="ylabel3d", type="text", value="y"),
    dcc.Input(id="zlabel3d", type="text", value="z"),
    html.Div([
        html.Div([dcc.Graph(id="example-graph3d")],
        style={"height":"100%", "width":"100%"})
    ]),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br()
])

def parse_contents(contents):
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)
    with open("./plotdata/tmp.csv", "w") as f:
        f.write(decoded.decode("utf-8"))

    df = pd.read_table("./plotdata/tmp.csv", header=None)
    x = df.iloc[:,0]
    y = df.iloc[:,1]

    if df.shape[1] == 2:
        labeltext = [0 for x in range(len(df))]
    elif df.shape[1] == 3:
        labeltext = df.iloc[:,2]

    return x, y, labeltext
    


##------------------------------------------------

def parse_contents3d(contents3d):
    content_type3d, content_string3d = contents3d.split(",")
    decoded3d = base64.b64decode(content_string3d)
    with open("./plotdata/tmp3d.csv", "w") as f:
        f.write(decoded3d.decode("utf-8"))
 
    df3d = pd.read_table("./plotdata/tmp3d.csv", header=None)

    x = df3d.iloc[:, 0]
    y = df3d.iloc[:, 1]
    z = df3d.iloc[:, 2]

    if df3d.shape[1] == 3:
        labeltext = [0 for x in range(len(df3d))]
    elif df3d.shape[1] == 4:
        labeltext = df3d.iloc[:,3]

    return x, y, z, labeltext

# callback for rendering 2d graph
@app.callback(
    Output('example-graph', 'figure'),
    Input('upload-data', 'contents'),
    Input("xlabel", "value"),
    Input("ylabel", "value"),
    Input("colorpalette2d","value"),
    Input("opacity2d","value"),
    Input("size2d","value"),
    Input("labelside2d", "value")
)
def update_graph(contents, xcolumn, ycolumn, colorset, opacity, size, labelside):
    x, y, labeltext = parse_contents(contents[0])
    le = LabelEncoder()
    if labelside == "no":
        xvalue = x
        yvalue = y
        ltext = [str(x) for x in labeltext]
        lvalue = labeltext

    elif labelside == "right":
        xvalue = x
        yvalue = y
        labelvalue = le.fit_transform(labeltext)
        ltext = [str(x) for x in labeltext]
        lvalue = labelvalue

    elif labelside == "left":
        xvalue = y
        yvalue = labeltext
        ltext = [str(i) for i in x]
        lavelvalue = le.fit_transform(x)
        lvalue = labelvalue

    return {"data":[go.Scatter(
        x=xvalue,
        y=yvalue,
        text=ltext,
        mode="markers",
        marker={
            "size":size,
            "color":lvalue,
            "colorscale":colorset,
            "opacity":opacity
        }
    )],
    "layout":go.Layout(
        xaxis={"title":xcolumn},
        yaxis={"title":ycolumn}
    )}

# callback for showing inputted 3d filename
@app.callback(
    Output("title2d", "children"),
    Input("upload-data", "filename")
)
def show_filename(filename):
    return filename

# callback for rendering 3d graph
@app.callback(
    Output("example-graph3d", "figure"),
    Input("upload-data3d", "contents"),
    Input("xlabel3d", "value"),
    Input("ylabel3d", "value"),
    Input("zlabel3d", "value"),
    Input("colorpalette3d","value"),
    Input("opacity3d","value"),
    Input("size3d","value"),
    Input("labelside3d", "value")
)
def update_graph3d(contents3d, xcolumn, ycolumn, zcolumn, colorset, opacity, size, labelside):
    x, y, z, labeltext= parse_contents3d(contents3d[0])
    le = LabelEncoder()
    if labelside == "no":
        xvalue = x
        yvalue = y
        zvalue = z
        ltext = [str(x) for x in labeltext]
        lvalue = labeltext

    elif labelside == "right":
        xvalue = x
        yvalue = y
        zvalue = z
        ltext = [str(x) for x in labeltext]
        lavelvalue = le.fit_transform(labeltext)
        lvalue = lavelvalue

    elif labelside == "left":
        xvalue = y
        yvalue = z
        zvalue = labeltext
        ltext = [str(i) for i in x]
        labelvalue = le.fit_transform(x)
        lvalue = labelvalue

    return {"data": [go.Scatter3d(
        x=xvalue,
        y=yvalue,
        z=zvalue,
        text=ltext,
        mode='markers',
        marker=dict(
            size=size,
            color=lvalue,
            colorscale=colorset,
            opacity=opacity
        )
    )],
    "layout":go.Layout(
	autosize=False,
	width=900,
	height=900,
    scene=go.layout.Scene(
        xaxis=go.layout.scene.XAxis(title=xcolumn),
        yaxis=go.layout.scene.YAxis(title=ycolumn),
        zaxis=go.layout.scene.ZAxis(title=zcolumn)
    )
    )
     }

# callback for showing inputted 3d filename
@app.callback(
    Output("title3d", "children"),
    Input("upload-data3d", "filename")
)
def show_filename3d(filename):
    return filename


if __name__ == '__main__':
    app.run_server(host="0.0.0.0")
