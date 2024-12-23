"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""


from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers


import matplotlib.pyplot as plt
import os



def run(filename: str) -> None:
   """
   Process heart rate data from the specified file, clean it, calculate metrics,
   and save visualizations.


   Args:
       filename (str): The path to the data file (e.g., 'data/data1.txt').


   Steps:
       1. Read the file into a list of strings.
       2. Use `filter_nondigits` to clean the data and remove invalid entries.
       3. Use `filter_outliers` to remove unrealistic heart rate samples (<30 or >250).
       4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
       5. Save the plots to the `images/` folder:
           - Rolling maximums -> 'images/maximums.png'
           - Rolling averages -> 'images/averages.png'
           - Rolling standard deviations -> 'images/stdevs.png'


   Returns:
       list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
   """ 
   data = []


   # open file and read into the `data` list
   # return all 3 lists
   with open(filename, 'r') as file:
       for line in file:
           data.append(line.strip())


   # clean data using provided functions
   filtered_data_digits = filter_nondigits(data)
   filtered_data = filter_outliers(filtered_data_digits)


   if not filtered_data:  # Handle empty data after filtering
       return [], [], []

   maximums = window_max(filtered_data, 6)
   averages = window_average(filtered_data, 6)
   stdevs = window_stddev(filtered_data, 6)


   # create the "images" directory if it doesn't exist
   os.makedirs("images", exist_ok=True)




   plt.plot(maximums)
   plt.title('Rolling Maximums')
   plt.savefig('images/maximums.png')
   plt.clf()  # Clear the current figure


   plt.plot(averages)
   plt.title('Rolling Averages')
   plt.savefig('images/averages.png')
   plt.clf()


   plt.plot(stdevs)
   plt.title('Rolling Standard Deviations')
   plt.savefig('images/stdevs.png')
   plt.clf()
   return maximums, averages, stdevs
if __name__ == "__main__":
   filename = "data/data1.txt"
   run("data/data1.txt")