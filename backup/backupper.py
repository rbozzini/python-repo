import os
from shutil import copyfile


def walk_folder(path, func):
    # dirs non non lo utilizo, ma se lo metto e non lo utilizzo, ho un errore. Uso i segnaposto '_'.
    for root, _, files in os.walk(path):
        for file in files:
            func(os.path.join(root, file))


class Backupper(object):
    def __init__(self, source_root, dest_root):
        self.source_root = os.path.abspath(source_root)
        self.dest_root = os.path.abspath(dest_root)

    def backup_file(self, file_path):
        dest_file = self._build_dest_path(file_path)
        return dest_file

    def _build_dest_path(self, file_path):
        return os.path.join(self.dest_root, os.path.relpath(file_path, self.source_root))

    def backup(self):
        # dirs non non lo utilizo, ma se lo metto e non lo utilizzo, ho un errore. Uso i segnaposto '_'.
        for root, _, files in os.walk(self.source_root):
            for file in files:
                self.backup_file(os.path.join(root, file))


class CopyFile(Backupper):
    def __init__(self, rules):
        self.rules = rules

    def backup_file(self, file_path):
        # Leggo la regola per il file:
        rule = self.rules.get(os.path.splitext(file_path)[1])

        if not rule:
            return

        # Ricavo percorso file destinazione
        dest_file_path = super._build_dest_path(self, file_path)
        exists = os.path.isfile(dest_file_path)

        if not exists or rule == "always":
            self._copyfile(file_path, dest_file_path)

        elif rule == "changed":
            print("check if newer:")

    def _copyfile(self, file_path, dest_file_path):
        print("coping {} to {}...".format(file_path, dest_file_path))
        # Verifica se la cartella esiste, se non esiste la crea.
        # Copia il file

    bkp = Backupper("C:/Users/Rossella/Documents/Casa", "C:/Users/Rossella/Documents/CasaBkp")
    bkp.backup()
