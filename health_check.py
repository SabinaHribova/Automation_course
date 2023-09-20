#Python script named health_check.py will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. 
#It checks the system statistics every 60 seconds
#Moreover, this Python script should send an email if there are problems, such as:

  #Report an error if CPU usage is over 80%
  #Report an error if available disk space is lower than 20%
  #Report an error if available memory is less than 500MB
  #Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"¨

import psutil
import shutil
#import emails
import time

cpu_message = 'Error - CPU usage is over 80 %'
mem_message = 'Error - Available memory is less than 500MB'
disk_message = 'Error - Available disk space is less than 20%'

summary = [cpu_message, mem_message, disk_message]

#TO DO: definovat funkce pro kontrolu všech veličin. Chybové hlášky uložit do proměnné
def cpu_check():
  cpu = psutil.cpu_percent(5)
  if cpu < 80:
    summary.remove(cpu_message)

def memory_check():
  mem = psutil.virtual_memory() #svmem(total=16349069312, available=5441630208, percent=66.7, used=10907439104, free=5441630208) in bytes
  if mem[1]/1000000 > 500:
    summary.remove(mem_message)

def disk_check():
  disk = psutil.disk_usage('/') #sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)
  if 100 - disk[3]  > 20:
    summary.remove(disk_message) 

def main():
  cpu_check()
  memory_check()
  disk_check() 

sender = "automation@example.com"
receiver = "username@example.com"
subject = '\n'.join(summary)
body = "Please check your system and resolve the issue as soon as possible."

starttime = time.time()

while True:
    print("tick")
    main ()
    print(summary)
    #if len(summary) >= 1:
      #message = emails.generate(sender, receiver, subject, body)
      #emails.send(message)
    # Remove the Time taken by code to execute
    time.sleep(20.0 - ((time.time() - starttime) % 20.0))
    summary = [cpu_message, mem_message, disk_message]




