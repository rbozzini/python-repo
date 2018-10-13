from datetime import datetime, timedelta

# Lettura marcature dal file marcature.txt
try:
    marcatureFile = open("marcature.txt", "r")
    marcature = marcatureFile.readlines()
    entrata = marcature[0].strip()
    print('Orario di ingresso : ' + entrata)
    uscitaPP = marcature[1].strip()
    entrataPP = marcature[2].strip()
except IOError:
    print ('cannot open marcature.txt')    
finally:
    marcatureFile.close()

ottoOre = int(8 * 60)

# Conversione degli orari in datetime:
entrata_dt = datetime.strptime(entrata,'%H:%M')
uscitaPP_dt = datetime.strptime(uscitaPP,'%H:%M')
entrataPP_dt = datetime.strptime(entrataPP,'%H:%M')

durataPP = max(30, round(int((entrataPP_dt - uscitaPP_dt).total_seconds()/60)))

print('Durata pausa pranzo: %d minuti' % durataPP)

added_datetime = entrata_dt + timedelta(minutes=ottoOre + durataPP)

print('Orario di uscita   : ' + datetime.strftime(added_datetime, '%H:%M'))
