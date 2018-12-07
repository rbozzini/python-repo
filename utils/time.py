def print_time_hh_mm_ss(millis):
    seconds = (millis/1000) % 60
    seconds = int(seconds)
    minutes = (millis/(1000*60)) % 60
    minutes = int(minutes)
    hours = (millis/(1000*60*60))

    print("%02d:%02d:%02d" % (hours, minutes, seconds))

if __name__ == "__main__":
    print_time_hh_mm_ss(60788660)
