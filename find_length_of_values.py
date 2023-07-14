def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    a = 0 
    for i in data.values():
        a += len(i)
    return a

data = {
    "x": "23",
    "3": "y", 
    "z": "5", 
    7:'a'
}
  
a = find_length_of_values(data)
print(a)