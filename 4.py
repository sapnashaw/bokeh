#4. Create a Bokeh histogram to visualize the distribution of the given data.


#Here’s how you can create a Bokeh histogram to visualize the distribution of the data_hist dataset:

#Install Bokeh if needed:


#pip install bokeh
#Use this Python script to create the histogram:


import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

output_notebook()

# Data
data_hist = np.random.randn(1000)
hist, edges = np.histogram(data_hist, bins=30)

# Create a new plot
p = figure(title="Histogram of Random Data", plot_height=400, plot_width=700)

# Add quad glyphs for histogram bars
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], 
       fill_color="navy", line_color="white", alpha=0.7)

# Customize plot
p.y_range.start = 0
p.xaxis.axis_label = 'Data values'
p.yaxis.axis_label = 'Frequency'

# Show the plot
show(p)
#This will generate a histogram showing the distribution of the data_hist dataset.









