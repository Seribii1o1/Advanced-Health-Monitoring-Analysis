import statistics
def window_max(data: list, n: int) -> list:
    maximums = []
    for i in range(0, len(data), n):  # Increment by n for non-overlapping windows
        maximums.append(max(data[i:i + n]))  # Simplified slicing
    return maximums
"""
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
def window_average(data: list, n: int) -> list:
    averages = []
    for i in range(0, len(data), n):
        averages.append(statistics.mean(data[i:i + n]))
    return averages

def window_stddev(data: list, n: int) -> list:
    stddevs = []
    if not data or n <= 0: 
        return stddevs

    for i in range(0, len(data), n):
        window = data[i:i + n]
        if len(window) > 1:
            stddev = statistics.stdev(window)
            stddevs.append(round(stddev, 2))  # Round to two decimal places
    return stddevs