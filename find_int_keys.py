def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    l = []
    for i in data:
        if type(i) == int or type(key):
          l.append(i)

    return l

data = [
{
    'name': 'John', 
    'age': 35
},
{
    'name':'Mary', 
    'age': 20
}
] 

a = find_int_keys(data)
print(a)