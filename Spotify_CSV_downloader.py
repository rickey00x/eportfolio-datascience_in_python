import subprocess
import time

print("Achtung, dieses Programm kann einige Zeit in Anspruch nehmen!")

day = int(input("Enter the begining day you want to download: "))

month = int(input("Enter the starting month you want to download: "))
uptomonth = int(input("Enter the  ending month you want to download: "))
year = int(input("Enter the year you want to download: "))
if uptomonth <= 12:
    uptomonth = uptomonth
else:
    uptomonth = 12
while(month <= uptomonth):
    bashCommand = "C:\Program Files\Google\Chrome\Application\chrome.exe https://spotifycharts.com/regional/de/daily/" + str(year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2) + "/download"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    day = day + 1
    if(day > 31):
        day = 1
        month = month + 1
    time.sleep(0.1)