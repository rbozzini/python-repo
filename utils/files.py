import os


def walk_folder(path, func):
    # dirs non non lo utilizo, ma se lo metto e non lo utilizzo, ho un errore. Uso i segnaposto '_'.
    for root, _, files in os.walk(path):
        for file in files:
            func(os.path.join(root, file))


def scan_folder(path, func):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            func(file)
        else:
            scan_folder(os.path.join(path, file), func)


class Backupper(object):
    def __init__(self, source_root, dest_root):
        self.source_root = os.path.abspath(source_root)
        self.dest_root = os.path.abspath(dest_root)

    def backup_file(self, file_path):
        dest_file = self._build_dest_path(file_path)
        print("coping {}...".format(dest_file))

    def _build_dest_path(self, file_path):
        return os.path.join(self.dest_root, os.path.relpath(file_path, self.source_root))


if __name__ == "__main__":
    # scan_folder("/home/rbozzini/Documenti/Personali", print)
    # walk_folder("C:/Users/Rossella/Documents/Casa", print)

    bkp = Backupper("C:/Users/Rossella/Documents/Casa", "C:/Users/Rossella/Documents/CasaBkp")
    walk_folder("C:/Users/Rossella/Documents/Casa", bkp.backup_file)
