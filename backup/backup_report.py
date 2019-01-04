import json


class BackupReport(object):

    def __init__(self):
        self.added_files = []
        self.updated_files = []
        self.deleted_files = []
        self.no_ruled_files = []

    def add_added_file(self, file):
        self.added_files.append(file)

    def add_updated_file(self, file):
        self.updated_files.append(file)

    def add_deleted_file(self, file):
        self.deleted_files.append(file)

    def add_no_ruled_file(self, file):
        self.no_ruled_files.append(file)

    def to_json(self):
        report = {}
        report['added_files'] = self.added_files
        report['updated_files'] = self.updated_files
        report['deleted_files'] = self.deleted_files
        report['no_ruled_files'] = self.no_ruled_files
        return json.dumps(report)


if __name__ == "__main__":
    report = BackupReport()
    report.add_added_file("added_file_1")
    report.add_added_file("added_file_2")
    report.add_added_file("added_file_3")
    report.add_updated_file("updated_file_1")
    report.add_updated_file("updated_file_2")
    report.add_deleted_file("deleted_file_1")
    report.add_no_ruled_file("no_ruled_file_1")
    report.add_no_ruled_file("no_ruled_file_1")
    print(report.to_json())
