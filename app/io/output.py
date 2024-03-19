

def output_text_to_console(data):
    """
    Function to output text to the console.

    Args:
        data (str): The text to be output to the console.
    """
    print(data)
    pass


def write_to_file_using_py(filename, data):
    """
    Function to write data to a file by using built-in capabilities.

    Args:
        filename (str): The name of the file to which data will be written.
        data (str): The data to be written to the file.
    """
    with open(filename, 'w') as file:
        file.write(data)
    pass