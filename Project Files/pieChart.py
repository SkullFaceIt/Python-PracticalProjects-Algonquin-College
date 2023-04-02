import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

class ChartGenerator:
    def generate_pie_chart(self, grades, values, colors, explode):
        #Build the pie chart
        plt.pie(values, labels=grades, colors=colors, explode=explode, autopct="%2.1f%%")
        plt.show()

        #Two lines to make our compiler able to draw:
        plt.savefig(sys.stdout.buffer)
        sys.stdout.flush()

