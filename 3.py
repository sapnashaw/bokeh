
#3. Generate a Bokeh bar chart representing the counts of different fruits using the following dataset.
#Here’s a concise guide to generating a Bokeh bar chart for the given dataset:

#Install Bokeh if you haven't:



#pip install bokeh
#Use this Python script to create the bar chart:

from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.transform import factor_cmap

output_notebook()

# Data
fruits = ['Apples', 'Oranges', 'Bananas', 'Pears']
counts = [20, 25, 30, 35]

# Create a new plot
p = figure(x_range=fruits, plot_height=400, title="Fruit Counts",
           toolbar_location=None, tools="")

# Add bar glyphs
p.vbar(x=fruits, top=counts, width=0.9, color=factor_cmap('fruits', 'Viridis4', fruits))

# Customize the plot
p.xgrid.grid_line_color = None
p.y_range.start = 0

# Show the plot
show(p)
#This will generate a bar chart representing the counts of different fruits.







