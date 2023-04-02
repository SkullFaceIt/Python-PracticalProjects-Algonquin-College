import sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class ChartGenerator:
    def generate_pie_chart(selectedPotatos):
        """Generate a pie chart pased on the "selectedPotatos" using the GEO column

        Args:
            selectedPotatos (dbPotato): A database object containing a GEO column
        """
        geos = []
        grades = []
        values = []
        # Extract GEO from potatos
        for potato in selectedPotatos:
            geos.append(potato["GEO"])
            
        # Initialize an empty dictionary to keep track of counts
        geo_dict = {}

        # Loop through the array and count each kind of geo
        for geo in geos:
            # If the current geo is already a key in the geo_counts dictionary, increment its count
            if geo in geo_dict:
                geo_dict[geo] += 1
            # Otherwise, add the current geo as a new key with count 1
            else:
                geo_dict[geo] = 1
                
        # Itterate through giving geo, count and i (index)
        for i, (geo, count) in enumerate(geo_dict.items()):
            grades.append(geo)
            values.append(count)
            
        #Build the pie chart
        plt.pie(values, labels=grades, autopct="%2.1f%%")
        # Flush any buffered output to the console before launching the pie chart ui
        sys.stdout.flush()
        # Launch the pie chart ui
        plt.show()
        
        # Close the figure explicitly to avoid issues with the pie chart ui
        plt.close()