import statistics
def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window

    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []
    for i in range(0, len(data), n):  # Increment by n for non-overlapping windows
        maximums.append(round(max(data[i:i + n]), 2))
    return maximums

def window_average(data: list, n: int) -> list:
    """Calculates the average of elements within sliding windows of size n.

    Args:
        data (list): The input list of numerical values.
        n (int): The size of the sliding window.

    Returns:
        list: A list of averages, where each element is the average of a window of size n.
    """
    averages = []
    for i in range(0, len(data), n):
        averages.append(round(statistics.mean(data[i:i + n]), 2))
    return averages

def window_stddev(data: list, n: int) -> list:
    """
    Calculates the standard deviation of non-overlapping windows within a given list of data.

    Args:
        data (list): The input list of numerical data.
        n (int): The size of each window.

    Returns:
        list: A list of standard deviations, one for each window.
    """
    stddevs = []
    if not data or n <= 0: 
        return stddevs

    for i in range(0, len(data), n):
        window = data[i:i + n]
        if len(window) > 1:
            stddev = statistics.stdev(window)
            stddevs.append(round(stddev, 2))  # Round to two decimal places
    return stddevs