import pandas as pd

def load_input(filename):
    df = pd.read_csv(filename, sep='\s+', header=None)
    return df