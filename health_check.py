#Python script named health_check.py will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. 
#It checks the system statistics every 60 seconds
#Moreover, this Python script should send an email if there are problems, such as:

  #Report an error if CPU usage is over 80%
  #Report an error if available disk space is lower than 20%
  #Report an error if available memory is less than 500MB
  #Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"¨

import psutil
import shutil

summary = []

#TO DO: definovat funkce pro kontrolu všech veličin. Chybové hlášky uložit do proměnné
def cpu_check():
  cpu = psutil.cpu_percent(5)
  if cpu > 80:
    summary.append('Error - CPU usage is over 80 %')

#TO DO: zavolat všechny funkce. Každých 60 sekund

#TO DO pokud funkce najdou chybu, poslat email.



