### dash-plotplayground

This application is deployed on [Heroku](https://rts-dashplayground.herokuapp.com/)

Receives a tab-separated txt file and Returns an interactive plot.

required data shapes\
2d-plot: row x column = [num of data] x [2] or [num of data] x [2 + 1(label column)]\
3d-plot: row x column = [num of data] x [3] or [num of data] x [3 + 1(label column)]\
label position must be the last column(right side of the data)

options\
colorset, mark-style(opacity, size), axis labels
