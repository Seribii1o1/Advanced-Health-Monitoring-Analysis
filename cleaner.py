def filter_nondigits(data: list) -> list:
    filtered_data = []
    for item in data:
        # Remove newline characters
        item = item.strip('\n')

        # Check if the string consists only of digits
        if item.isdigit():
            filtered_data.append(int(item))
    return filtered_data
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    pass

def filter_outliers(data: list) -> list:
    pass
