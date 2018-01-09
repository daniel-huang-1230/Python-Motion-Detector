from motion_detector import df

from bokeh.plotting import figure, show, output_file

p = figure(x_axis_type = "datetime", height = 100, width = 500, responsive = True, title = "Motion Graph")
p.yaxis.minor_tick_line_color = None #hide the unnecessary ticks on y-axis

p.ygrid[0].ticker.desired_num_ticks = 1 #hide the intermmediate lines/grid in the graph
#draw the bar chart with the quad glyph
q = p.quad(left = df['Start'], right = df['End'], top=1, bottom=0, color = "green")

output_file("Graph.html")
show(p)