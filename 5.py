#5. Create a Bokeh heatmap using the provided dataset.

#Here’s how you can create a Bokeh heatmap using the given data_heatmap dataset:

#Install Bokeh if needed:


#pip install bokeh
#Use this Python script to create the heatmap:


import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColorBar, LinearColorMapper
from bokeh.transform import linear_cmap

output_notebook()

# Data
data_heatmap = np.random.rand(10, 10)
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
xx, yy = np.meshgrid(x, y)

# Flatten the grid and heatmap data
x_flat = xx.flatten()
y_flat = yy.flatten()
heatmap_values = data_heatmap.flatten()

# Create a color mapper
mapper = LinearColorMapper(palette="Viridis256", low=heatmap_values.min(), high=heatmap_values.max())

# Create a new plot
p = figure(title="Heatmap", plot_width=600, plot_height=600,
           x_range=(0, 1), y_range=(0, 1))

# Add the heatmap rectangles
p.rect(x_flat, y_flat, width=0.1, height=0.1, source=dict(x=x_flat, y=y_flat, value=heatmap_values),
       fill_color=linear_cmap('value', 'Viridis256', heatmap_values.min(), heatmap_values.max()), 
       line_color=None)

# Add a color bar
color_bar = ColorBar(color_mapper=mapper, location=(0, 0))
p.add_layout(color_bar, 'right')

# Show the plot
show(p)
#This script will generate a heatmap using the random data from data_heatmap. Each rectangle corresponds to a value in the dataset, and the colors represent the intensity of the values.








