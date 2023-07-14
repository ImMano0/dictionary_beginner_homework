def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    counter = 0
    for users in data:
        if users['job'] == job:
            counter += 1
    return counter

data=[
{
    'name': 'John', 
    'job': 'Developer'
}, 
{
    'name': 'Mary', 
    'job': 'Developer'
}
]

job = 'Developer'
print(count_jobs(data, job))