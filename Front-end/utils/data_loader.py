import pandas as pd

def load_data(file_path):
    """Load dataset from a given file path."""
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise Exception(f"File not found at {file_path}")
