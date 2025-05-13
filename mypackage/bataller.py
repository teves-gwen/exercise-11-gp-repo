import numpy as np

def generate_random_integers(count, low, high):
   
    numbers = np.random.randint(low, high, count) 
    mean = np.mean(numbers)  
    median = np.median(numbers) 
    stddev = np.std(numbers)  

    return numbers, mean, median, stddev
