def write_file(file_name, content):
    file_path = f"{file_name}.txt"
    with open(file_path, "w") as f:
        f.write(content)


def append_file(file_name, content):
    file_path = f"{file_name}.txt"
    with open(file_path, "a") as f:
        f.write(content)


def read_file(file_name):
    file_path = f"{file_name}.txt"
    with open(file_path, "r") as f:
        return f.read()
