##################
## dependencies ##
##################
# pip install requests
# pip install playsound
##################

import requests
import time
import urllib3
from playsound import playsound

urllib3.disable_warnings()
wavFile_status200 = "servers back online speech.wav"
wavFile_status500 = "error500.wav"
wasOffline = False
wasOnline = False

while True:
    r = requests.get('https://DOMAIN_ME', verify=False)
    print(r.status_code)
    if r.status_code == 500:
        wasOffline = True
        if wasOnline:
            playsound(wavFile_status500)
            wasOnline = False
    else:
        wasOnline = True
        if wasOffline:
            playsound(wavFile_status200)
            wasOffline = False
    time.sleep(4)
