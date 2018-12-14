import os


def scan_folder(path, func):
    for file in os.listdir(path):
        if os.path.isfile((os.path.join(path, file))):
            func(file)

        elif os.path.isdir((os.path.join(path, file))):
            scan_folder(os.path.join(path, file), func)


if __name__ == "__main__":
    scan_folder("/home/rbozzini/Documenti/Personali", print)
