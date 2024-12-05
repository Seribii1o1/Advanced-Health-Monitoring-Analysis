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

def filter_outliers(data: list) -> list:
    filtered_data = []
    for heart_rate in data:
      if 30 < heart_rate < 250:
         filtered_data.append(heart_rate)
    return filtered_data
"""Filters out heart rate samples that are less than 30 or greater than 250.

  Args:
    data: A list of integer heart rate samples.

  Returns:
    A new list containing only the filtered heart rate samples.
  """