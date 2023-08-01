# file_handling.py

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return "File write successful."
    except IOError:
        return f"Error: Unable to write to file '{filename}'."

