import time
import pycurl

while True:
    c = pycurl.Curl()
    # Local network
    c.setopt(c.URL, 'https://git.scriptandgo.com/')
    # Internet
    # c.setopt(c.URL, 'https://www.docker.com/')
    # Docker instance
    # c.setopt(c.URL, 'https://web:5000/')
    c.perform()
    time.sleep(0.5)
