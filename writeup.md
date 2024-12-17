## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

[The device is not picking up some of the measurements. This could be due to issues with the sensor or other factors. Filtering these values could potentially skew the results. It is good to take multiple readings to minimize this.] 

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

[The standard deviation describes of the variability from the heart rate data averages. For example, sometimes heart rate can be faster or slower.] 

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

[Drastic increase at x = 10 and drastic decrease at x = 30.]

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

[Yes, drastic increase at x = 10 and drastic decrease at x = 30. These major differences do align with the averages.png graph. The stdevs.png graph has more peaks and valleys overall.]
