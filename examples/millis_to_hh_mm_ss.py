import os


def print_time_hh_mm_ss(millis):
    seconds = (millis/1000) % 60
    seconds = int(seconds)
    minutes = (millis/(1000*60)) % 60
    minutes = int(minutes)
    hours = (millis/(1000*60*60))

    print("%02d:%02d:%02d" % (hours, minutes, seconds))

try:
    millis_per_doc = 20

    abs_file_path = os.path.join(os.path.dirname(__file__), "docs_to_index.txt")
    millisFile = open(abs_file_path, "r")

    for millis in millisFile:
        print_time_hh_mm_ss(int(millis.strip()) * millis_per_doc)

except IOError:
    print('cannot open millis.txt')
