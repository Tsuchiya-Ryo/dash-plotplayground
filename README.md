### dash-plotplayground

This application is deployed on [Heroku](https://rts-dashplayground.herokuapp.com/)

receives tab-separated(.txt) / comma separated(.csv) / excel sheets(.xlsx/.xls) file\
returns an interactive scatter plot.

required data shapes\
2d-plot: row x column = [num of data] x [2] or [num of data] x [2 + 1(label column)]\
3d-plot: row x column = [num of data] x [3] or [num of data] x [3 + 1(label column)]\
select the positions of each axis columns

options\
colorset, mark-style(opacity, size), axis labels
