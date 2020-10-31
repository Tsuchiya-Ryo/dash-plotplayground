import base64, io
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from sklearn.preprocessing import LabelEncoder

app = dash.Dash(__name__)

# STYLE PARAMETER SETTINGS ----------------------------------------------------------
colorpalette = [{"label":x, "value":x} for x in [
                "Viridis", "Cividis", "Inferno", "Electric", "Rainbow",
                "Plasma", "Speed","Jet", "Plotly3", "Bluered","Thermal",
                "Portland", "HSV", "Phase", "Mrybm", "Mygbm"]]
filetypes = [{"label":"[tab separated .txt]", "value":"txt"},
            {"label":"[comma separated .csv]", "value":"csv"},
            {"label":"[excel file .xlsx/.xls]", "value":"xlsx"}]
filelimit = 750000
uploadstyle = {'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'}
opacityset = [{"label": round(i, 1), "value": round(i, 1)}\
            for i in np.linspace(0.1, 1, 10) ]
marksize = [{"label":round(i,0), "value":round(i,0)}\
            for i in np.linspace(3,16,14)]
dropdownbox = {"height":"30px", "width":"150px", "display":"inline-block"}
axis_name_input = {"height":"25px","width":"200px", "borderRadius":"5px",
                    "font-size":"16px", "borderWidth":"1px"}
multisheetscount = [{"label": str(int(i)), "value": int(i)} for i in np.linspace(1, 5, 5)]
xy_axis_position_2d = [{"label":i, "value":j} for i, j in zip(["1st","2nd","3rd"],range(3))]
xyz_axis_position_3d = [{"label":i, "value":j} for i, j in zip(["1st","2nd","3rd","4th"],range(4))]
label_axis_position_2d = xy_axis_position_2d.copy()
label_axis_position_2d.append({"label":"None","value":"NONE"})
label_axis_position_3d = xyz_axis_position_3d.copy()
label_axis_position_3d.append({"label":"None","value":"NONE"})

# INTERFACE --------------------------------------------------------------------------
# HEADER -----------------------------------------------------------------------------
app.layout = html.Div(children=[
    html.H1(children="Plot Playground"),
    html.Div([
    html.A("HOME", href="https://tsuchiya-ryo.github.io/orgsynscalc/"),
    html.Br(),
    html.A("Plot使い方", href="https://tsuchiya-ryo.github.io/orgsynscalc/plot-explanation.html")
    ]),

# 2D PLOT AREA -----------------------------------------------------------------------
    html.H2(children="2d-plot"),
    html.Div([
        html.Div(children="input file type:", style={"display":"inline-block"}),
        dcc.RadioItems(id="filetype2d",
            options=filetypes,
            value="txt",
            style={"display":"inline-block"}
        )
    ]),

    html.Div([
    html.Div(children="multiple sheets (for .xlsx/.xls, columns must be the same position):", style={"display":"inline-block"}),
    dcc.RadioItems(id="multisheets2d",
                    options=multisheetscount,
                    value = 1,
                    style={"display":"inline-block"})
    ]),

    html.P(children="~axis column positions~"),
    html.Div([
        html.Div(children="Label :", style={"display":"inline-block"}),
        dcc.RadioItems(id="labelaxis2d",
            options=label_axis_position_2d,
            value="NONE",
            style={"display":"inline-block"}
        )
    ]),
    html.Div([
        html.Div(children="x-axis:", style={"display":"inline-block"}),
        dcc.RadioItems(id="xaxis2d",
            options=xy_axis_position_2d,
            value=0,
            style={"display":"inline-block"}
        )
    ]),
        html.Div([
        html.Div(children="y-axis:", style={"display":"inline-block"}),
        dcc.RadioItems(id="yaxis2d",
            options=xy_axis_position_2d,
            value=1,
            style={"display":"inline-block"}
        )]),

    html.Br(),

    dcc.Upload(
        id='upload-data',
        children=html.A("Click to Select 2d File (or drag and drop)"),
        multiple=True,
        max_size=filelimit,
        style=uploadstyle),
    html.Br(),

    html.Div([
        dcc.Dropdown(
        id="colorpalette2d",
        options=colorpalette,
        value="Viridis",
        style=dropdownbox
    ),
    dcc.Dropdown(
        id="opacity2d",
        options=opacityset,
        value=0.5,
        style=dropdownbox
    ),
    dcc.Dropdown(
        id="size2d",
        options=marksize,
        value=5,
        style=dropdownbox
    )]),
    html.Br(),

    html.P(id="title2d"),
    dcc.Input(id="xlabel", type="text", value="x", style=axis_name_input),
    dcc.Input(id="ylabel", type="text", value="y", style=axis_name_input),

    html.Div([
        html.Div([dcc.Graph(id="example-graph")],
        style={"height":"100%", "width":"100%"})
    ]),
# 3D PLOT AREA --------------------------------------------------------------------
    html.H2(children="3d-plot"),

     html.Div([
        html.Div(children="input file type:", style={"display":"inline-block"}),
        dcc.RadioItems(id="filetype3d",
            options=filetypes,
            value="txt",
            style={"display":"inline-block"}
        )
    ]),

    html.Div([
    html.Div(children="multiple sheets (for .xlsx/.xls, columns must be the same position):", style={"display":"inline-block"}),
    dcc.RadioItems(id="multisheets3d",
                    options=multisheetscount,
                    value = 1,
                    style={"display":"inline-block"})
    ]),

    html.P(children="~axis column positions~"),
    html.Div([
        html.Div(children="Label :", style={"display":"inline-block"}),
        dcc.RadioItems(id="labelaxis3d",
            options=label_axis_position_3d,
            value="NONE",
            style={"display":"inline-block"}
        )]),
    html.Div([
        html.Div(children="x-axis:", style={"display":"inline-block"}),
        dcc.RadioItems(id="xaxis3d",
            options=xyz_axis_position_3d,
            value=0,
            style={"display":"inline-block"}
        )]),
        html.Div([
        html.Div(children="y-axis:", style={"display":"inline-block"}),
        dcc.RadioItems(id="yaxis3d",
            options=xyz_axis_position_3d,
            value=1,
            style={"display":"inline-block"}
        )]),
        html.Div([
        html.Div(children="z-axis:", style={"display":"inline-block"}),
        dcc.RadioItems(id="zaxis3d",
            options=xyz_axis_position_3d,
            value=2,
            style={"display":"inline-block"}
        )]),

    html.Br(),

    dcc.Upload(
        id='upload-data3d',
        children=html.A("Click to Select 3d File (or drag and drop)"),
        multiple=True,
        max_size=filelimit,
        style=uploadstyle),
     html.Br(),

    html.Div([
    dcc.Dropdown(
        id="colorpalette3d",
        options=colorpalette,
        value="Viridis",
        style=dropdownbox
    ),
    dcc.Dropdown(
        id="opacity3d",
        options=opacityset,
        value=0.5,
        style=dropdownbox
    ),
    dcc.Dropdown(
        id="size3d",
        options=marksize,
        value=5,
        style=dropdownbox
    )]),

    html.Br(),

    html.P(id="title3d"),
    dcc.Input(id="xlabel3d", type="text", value="x", style=axis_name_input),
    dcc.Input(id="ylabel3d", type="text", value="y", style=axis_name_input),
    dcc.Input(id="zlabel3d", type="text", value="z", style=axis_name_input),
    html.Div([
        html.Div([dcc.Graph(id="example-graph3d")],
        style={"height":"100%", "width":"100%"})
    ]),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br()
    ])
# INTERFACE END -----------------------------------------------------------------------

# READ FILE AND RETURN DATAFRAME 2D-----------------------------------------------------
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

# READ FILE AND RETURN DATAFRAME 3D-----------------------------------------------------
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
 

# CALLBACK FOR 2D GRAPH ------------------------------------------------------------
@app.callback(
    Output('example-graph', 'figure'),

    Input('upload-data', 'contents'),
    Input("filetype2d", "value"),
    Input("multisheets2d", "value"),
    Input("xaxis2d", "value"),
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

# CALLBACK FOR DISPLAY FILENAME 2D--------------------------------------------------
@app.callback(
    Output("title2d", "children"),
    Input("upload-data", "filename")
)
def show_filename(filename):
    return filename

# CALLBACK FOR 3D GRAPH ------------------------------------------------------------
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

# CALLBACK FOR DISPLAY FILENAME 3D ----------------------------------------------------
@app.callback(
    Output("title3d", "children"),
    Input("upload-data3d", "filename")
)
def show_filename3d(filename):
    return filename

# RUN APPLICATION ---------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(host="0.0.0.0")