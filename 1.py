#1.Create a Bokeh plot displaying a sine wave. Set x-values from 0 to 10 and y-values as the sine of x.

import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook

# Set x-values from 0 to 10
x = np.linspace(0, 10, 500)
# Calculate y-values as the sine of x
y = np.sin(x)

# Create a new plot with a title and axis labels
p = figure(title="Sine Wave", x_axis_label='x', y_axis_label='sin(x)', plot_width=700, plot_height=400)

# Add a line renderer with the x and y values
p.line(x, y, legend_label="sin(x)", line_width=2)

# Show the plot in the notebook
output_notebook()
show(p)