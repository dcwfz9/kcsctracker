__author__ = 'Derek'

import requests
from bs4 import BeautifulSoup

def getstopinfo(dir):
    if dir.lower() == 'north':
        direction = north
    elif dir.lower() == 'south':
        direction = south
    r = requests.get(LINK + '?r=' + str(sc) + '&d=' + str(direction))
    soup = BeautifulSoup(r.text)
    myStops = soup.findAll("a", {"class" : "adalink"})

    stopList = []
    #go to each link and save data
    for s in myStops:
        stop = Stop(s['title'])
        stop.direction = direction
        req =  requests.get(LINK + s['href'])
        bs = BeautifulSoup(req.text)
        myTimes = bs.findAll("a", {"class" : "adatime"})

        for t in myTimes:
            stop.times.append(t['title'])

        stopList.append(stop)
    return stopList

class Stop:
    def __init__(self, name):
        self.times = []
        self.name = name
        self.direction = ""

#search for all coordinates under North. Save number, lat, long and next stop

north = 14
south = 15
sc = 100
#http://www.kc-metro.com/tmwebwatch/LiveAdaArrivalTimesMobile?r=100&d=15
LINK = 'http://www.kc-metro.com/tmwebwatch/LiveAdaArrivalTimesMobile'

