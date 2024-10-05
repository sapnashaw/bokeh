#
# 2.Create a Bokeh scatter plot using randomly generated x and y values. Use different sizes and colors for the#


H#ere's a concise version of the steps to create the Bokeh scatter plot:

#Install Bokeh:


import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.transform import linear_cmap
from bokeh.models import ColumnDataSource

output_notebook()

# Generate random data
x = np.random.rand(500) * 100
y = np.random.rand(500) * 100
sizes = np.random.rand(500) * 30 + 10
colors = np.random.rand(500) * 255

source = ColumnDataSource(data=dict(x=x, y=y, sizes=sizes, colors=colors))

p = figure(title="Random Scatter Plot", x_axis_label='x', y_axis_label='y', plot_width=700, plot_height=400)
p.scatter('x', 'y', size='sizes', color=linear_cmap('colors', 'Viridis256', 0, 255), source=source)

show(p)
#This will create a scatter plot with random values, marker sizes, and colors.







#markers based on the 'sizes' and 'colors' columns.