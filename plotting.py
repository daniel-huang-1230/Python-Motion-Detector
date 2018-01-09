from motion_detector import df

from bokeh.plotting import figure, show, output_file

p = figure(x_axis_type = "datetime", height = 100, width = 500, responsive = True, title = "Motion Graph")

#
q = p.quad(left = df['Start'], right = df['End'], top=1, bottom=0, color = "green")

output_file("Graph.html")
show(p)