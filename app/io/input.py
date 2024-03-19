import pandas as pd


def input_text_from_console():
    """
    Function to input text from the console.

    Returns:
        str: The text that was input from the console.
    """
    return input("Enter text: ")


def read_from_file_using_py(filename):
    """
    Function to read data from a file by using built-in capabilities.

    Args:
        filename (str): The name of the file from which data will be read.

    Returns:
        str: The data that will be read from the file.
    """
    with open(filename, 'r') as file:
        return file.read()


def read_from_file_using_pandas(filename):
    """
    Function to read data from a file by using the pandas library.

    Args:
        filename (str): The name of the file from which data will be read.

    Returns:
        DataFrame: The data that will be read from the filee as a pandas DataFrame.
    """
    return pd.read_csv(filename)