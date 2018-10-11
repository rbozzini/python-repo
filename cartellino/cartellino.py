from datetime import datetime
from datetime import timedelta 
import time

try:
    marcatureFile = open("marcature.txt", "r")
    marcature = marcatureFile.readlines()
    entrata = marcature[0].strip()
    print('Orario di ingresso : ' + entrata)
    uscitaPP = marcature[1].strip()
    entrataPP = marcature[2].strip()
except IOError:
    print 'cannot open', "marcature.txt"    
finally:
    marcatureFile.close

ottoOre = int(8 * 60)

entrata_dt = datetime.strptime(entrata,'%H:%M');
uscitaPP_dt = datetime.strptime(uscitaPP,'%H:%M');
entrataPP_dt = datetime.strptime(entrataPP,'%H:%M');

uscitaPP_ts = time.mktime(uscitaPP_dt.timetuple())
entrataPP_ts = time.mktime(entrataPP_dt.timetuple())

durataPP = int(entrataPP_ts - uscitaPP_ts)/60
if (durataPP < 30):
    durataPP = 30
print('Durata pausa pranzo: ' + str(durataPP) + ' minuti')

durata_lavoro = ottoOre + durataPP

added_datetime = entrata_dt + timedelta(minutes=durata_lavoro)

print('Orario di uscita   : ' + datetime.strftime(added_datetime,'%H:%M'))
