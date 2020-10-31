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

    html.Div([
        html.Div(children="input file type:", style={"display":"inline-block"}),
        dcc.RadioItems(id="filetype2d",
            options=[
                {"label":"[tab separated .txt]", "value":"txt"},
                {"label":"[comma separated .csv]", "value":"csv"},
                {"label":"[.xlsx or .xls]", "value":"xlsx"}
            ],
            value="txt",
            style={"display":"inline-block"}
        )
    ]),

    html.Div([
    html.Div(children="multiple sheets (for .xlsx/.xls, columns must be the same position):", style={"display":"inline-block"}),
    dcc.RadioItems(id="multisheets2d",
                    options=[{"label": str(int(i)), "value": int(i)} for i in np.linspace(1, 5, 5)],
                    value = 1,
                    style={"display":"inline-block"})
    ]),

    html.P(children="~axis column positions~"),
    html.Div([
        html.Div(children="Label :", style={"display":"inline-block"}),
        dcc.RadioItems(id="labelaxis2d",
            options=[
                {"label":"1st", "value":0},
                {"label":"2nd", "value":1},
                {"label":"3rd", "value":2},
                {"label":"None", "value":"NONE"}
            ],
            value="NONE",
            style={"display":"inline-block"}
        )
    ]),
    html.Div([
        html.Div(children="x-axis:", style={"display":"inline-block"}),
        dcc.RadioItems(id="xaxis2d",
            options=[
                {"label":"1st", "value":0},
                {"label":"2nd", "value":1},
                {"label":"3rd", "value":2}
            ],
            value=0,
            style={"display":"inline-block"}
        )
    ]),
        html.Div([
        html.Div(children="y-axis:", style={"display":"inline-block"}),
        dcc.RadioItems(id="yaxis2d",
            options=[
                {"label":"1st", "value":0},
                {"label":"2nd", "value":1},
                {"label":"3rd", "value":2}
            ],
            value=1,
            style={"display":"inline-block"}
        )
    ]),


   
    html.Br(),
    dcc.Upload(
        id='upload-data',
        children=html.A("Click to Select 2d File (or drag and drop)"),
        multiple=True,
        max_size = 750000,
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

    html.Div([
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
        style={"height":"30px", "width":"150px", "display":"inline-block"}
    ),
    dcc.Dropdown(
        id="opacity2d",
        options=[{"label": round(i, 1), "value": round(i, 1)}\
             for i in np.linspace(0.1, 1, 10) ],
             value=0.5,
             style={"height":"30px", "width":"150px", "display":"inline-block"}
    ),
    dcc.Dropdown(
        id="size2d",
        options=[{"label":round(i,0), "value":round(i,0)}\
            for i in np.linspace(3,12,10)],
            value=5,
            style={"height":"30px", "width":"150px",  "display":"inline-block"}
    )]),
    html.Br(),

    html.P(id="title2d"),
    dcc.Input(id="xlabel", type="text", value="x"),
    dcc.Input(id="ylabel", type="text", value="y"),

    html.Div([
        html.Div([dcc.Graph(id="example-graph")],
        style={"height":"100%", "width":"100%"})
    ]),


    html.H2(children="3d-plot"),

     html.Div([
        html.Div(children="input file type:", style={"display":"inline-block"}),
        dcc.RadioItems(id="filetype3d",
            options=[
                {"label":"[tab separated .txt]", "value":"txt"},
                {"label":"[comma separated .csv]", "value":"csv"},
                {"label":"[.xlsx or .xls]", "value":"xlsx"}
            ],
            value="txt",
            style={"display":"inline-block"}
        )
    ]),

    html.Div([
    html.Div(children="multiple sheets (for .xlsx/.xls, columns must be the same position):", style={"display":"inline-block"}),
    dcc.RadioItems(id="multisheets3d",
                    options=[{"label": str(int(i)), "value": int(i)} for i in np.linspace(1, 5, 5)],
                    value = 1,
                    style={"display":"inline-block"})
    ]),

    html.P(children="~axis column positions~"),
    html.Div([
        html.Div(children="Label :", style={"display":"inline-block"}),
        dcc.RadioItems(id="labelaxis3d",
            options=[
                {"label":"1st", "value":0},
                {"label":"2nd", "value":1},
                {"label":"3rd", "value":2},
                {"label":"4th", "value":3},
                {"label":"None", "value":"NONE"}
            ],
            value="NONE",
            style={"display":"inline-block"}
        )
    ]),
    html.Div([
        html.Div(children="x-axis:", style={"display":"inline-block"}),
        dcc.RadioItems(id="xaxis3d",
            options=[
                {"label":"1st", "value":0},
                {"label":"2nd", "value":1},
                {"label":"3rd", "value":2},
                {"label":"4th", "value":3}
            ],
            value=0,
            style={"display":"inline-block"}
        )
    ]),
        html.Div([
        html.Div(children="y-axis:", style={"display":"inline-block"}),
        dcc.RadioItems(id="yaxis3d",
            options=[
                {"label":"1st", "value":0},
                {"label":"2nd", "value":1},
                {"label":"3rd", "value":2},
                {"label":"4th", "value":3}
            ],
            value=1,
            style={"display":"inline-block"}
        )
    ]),
        html.Div([
        html.Div(children="z-axis:", style={"display":"inline-block"}),
        dcc.RadioItems(id="zaxis3d",
            options=[
                {"label":"1st", "value":0},
                {"label":"2nd", "value":1},
                {"label":"3rd", "value":2},
                {"label":"4th", "value":3}
            ],
            value=2,
            style={"display":"inline-block"}
        )
    ]),


    html.Br(),
    dcc.Upload(
        id='upload-data3d',
        children=html.A("Click to Select 3d File (or drag and drop)"),
        multiple=True,
        max_size = 750000,

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

    html.Div([
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
        style={"height":"30px", "width":"150px", "display":"inline-block"}
    ),
    dcc.Dropdown(
        id="opacity3d",
        options=[{"label": round(i, 1), "value": round(i, 1)}\
             for i in np.linspace(0.1, 1, 10) ],
             value=0.5,
             style={"height":"30px", "width":"150px", "display":"inline-block"}
    ),
    dcc.Dropdown(
        id="size3d",
        options=[{"label":round(i,0), "value":round(i,0)}\
            for i in np.linspace(3,12,10)],
            value=5,
            style={"height":"30px", "width":"150px", "display":"inline-block"}
    )]),
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

def parse_contents(contents, filetype, numsheets, xaxis, yaxis, labelaxis):
    _, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)

    if filetype != "xlsx":
        with open("./plotdata/tmp.csv", "w") as f:
            f.write(decoded.decode("utf-8"))
    
    if filetype == "txt":
        df = pd.read_table("./plotdata/tmp.csv", header=None)
    elif filetype == "csv":
        df = pd.read_csv("./plotdata/tmp.csv", header=None)
    elif filetype == "xlsx":
        if numsheets == 1:
            df = pd.read_excel(io.BytesIO(decoded), header=None, sheet_name=0)
        elif numsheets > 1:
            sheet_name = [x for x in range(0, numsheets)]
            df_dict = pd.read_excel(io.BytesIO(decoded), header=None, sheet_name=sheet_name)
            df = pd.concat([df_dict[x] for x in range(0, numsheets)])

    return df

##------------------------------------------------

def parse_contents3d(contents3d, filetype, numsheets, xaxis, yaxis, zaxis, labelaxis):
    _, content_string3d = contents3d.split(",")
    decoded3d = base64.b64decode(content_string3d)

    if filetype != "xlsx":
        with open("./plotdata/tmp3d.csv", "w") as f:
            f.write(decoded3d.decode("utf-8"))
    
    if filetype == "txt":
        df3d = pd.read_table("./plotdata/tmp3d.csv", header=None)
    elif filetype == "csv":
        df3d = pd.read_csv("./plotdata/tmp3d.csv", header=None)
    elif filetype == "xlsx":
        if numsheets == 1:
            df3d = pd.read_excel(io.BytesIO(decoded3d), header=None, sheet_name=0)
        elif numsheets > 1:
            sheet_name = [x for x in range(0, numsheets)]
            df3d_dict = pd.read_excel(io.BytesIO(decoded3d), header=None, sheet_name=sheet_name)
            df3d = pd.concat([df3d_dict[x] for x in range(0, numsheets)])
    
    return df3d
 

# callback for rendering 2d graph
@app.callback(
    Output('example-graph', 'figure'),

    Input('upload-data', 'contents'), # contents
    Input("filetype2d", "value"), # filetype
    Input("multisheets2d", "value"), # numsheets
    Input("xaxis2d", "value"), # xaxis
    Input("yaxis2d", "value"),
    Input("labelaxis2d", "value"),
    Input("xlabel", "value"),
    Input("ylabel", "value"),
    Input("colorpalette2d","value"),
    Input("opacity2d","value"),
    Input("size2d","value"),
)
def update_graph(contents, filetype, numsheets, xaxis, yaxis, labelaxis, xcolumn, ycolumn, colorset, opacity, size):
    df = parse_contents(contents[0], filetype, numsheets, xaxis, yaxis, labelaxis)
    
    if labelaxis == "NONE":
        x = df.iloc[:, xaxis]
        y = df.iloc[:, yaxis]
        labeltext = [0 for x in range(len(df))]
    
    else:
        x = df.iloc[:, xaxis]
        y = df.iloc[:, yaxis]
        labeltext = df.iloc[:, labelaxis]
        
    le = LabelEncoder()
    labelvalue = le.fit_transform(labeltext)
    
    xvalue = x
    yvalue = y
    ltext = labeltext
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
        autosize=False,
        width=900,
        height=600,
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
    Input("filetype3d", "value"),
    Input("multisheets3d", "value"), # numsheets
    Input("xaxis3d", "value"), # xaxis
    Input("yaxis3d", "value"),
    Input("zaxis3d", "value"),
    Input("labelaxis3d", "value"),
    Input("xlabel3d", "value"),
    Input("ylabel3d", "value"),
    Input("zlabel3d", "value"),
    Input("colorpalette3d","value"),
    Input("opacity3d","value"),
    Input("size3d","value"),
)
def update_graph3d(contents3d, filetype, numsheets, xaxis, yaxis, zaxis, labelaxis, xcolumn, ycolumn, zcolumn, colorset, opacity, size):
    df3d= parse_contents3d(contents3d[0], filetype, numsheets, xaxis, yaxis, zaxis, labelaxis)
    
    if labelaxis == "NONE":
        x = df3d.iloc[:, xaxis]
        y = df3d.iloc[:, yaxis]
        z = df3d.iloc[:, zaxis]
        labeltext = [0 for x in range(len(df3d))]
    
    else:
        x = df3d.iloc[:, xaxis]
        y = df3d.iloc[:, yaxis]
        z = df3d.iloc[:, zaxis]
        labeltext = df3d.iloc[:, labelaxis]
        
    le = LabelEncoder()
    labelvalue = le.fit_transform(labeltext)
    
    xvalue = x
    yvalue = y
    zvalue = z
    ltext = labeltext
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