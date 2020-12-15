##################
## dependencies ##
##################
# pip install requests
# pip install playsound
##################

import requests
import time
from datetime import datetime
import urllib3
from playsound import playsound

urllib3.disable_warnings()
wavFile_status200 = "servers back online speech.wav"
wavFile_status500 = "error500.wav"
wavFile_status408 = "error408.wav"
wasOffline = False
wasOnline = True

def printTime(text, tag):
    print(datetime.now(), " [", tag, "] ", text)


def test_server_response(url, tag):
    global wasOffline
    global wasOnline

    try:
        r = requests.get(url, verify=False)
        printTime("status: " + str(r.status_code), tag)
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
        pass
    except requests.RequestException:
        printTime("timeout", tag)
        wasOffline = True
        if wasOnline:
            playsound(wavFile_status408)
            wasOnline = False
        pass


while True:
    test_server_response('https://DOMAIN_ME', "PRODUCTION")
    test_server_response('https://DOMAIN_ME', "TESTING")
    time.sleep(10)
