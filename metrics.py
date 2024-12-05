import statistics
def window_max(data: list, n: int) -> list:
    maximums = []
    for i in range(0, len(data) - n + 1, n):
        window = data[i:i + n]
        maximums.append(max(window))
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
    for i in range(0, len(data) - n + 1, n):
        window = data[i:i + n]
        averages.append(statistics.mean(window))
    return averages

def window_stddev(data: list, n: int) -> list:
    stdevs = []
    for i in range(0, len(data) - n + 1, n):
        window = data[i:i + n]
        if len(window) > 1:
            stdev = statistics.stdev(window)
            stdevs.append(round(stdev, 2))  # Round to 2 decimal places
        else:
            stdevs.append([])
    return stdevs