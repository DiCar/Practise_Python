# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:59:28 2015

@author: DiCar
"""

import urllib2
import json
import random

def madLibs(data):
    # Use the json library to load the string data into a directory
    theJSONWords = json.loads(data)
    # Now we can access the JSON data like a python object
    
    #define the adjective list
    adjectives = theJSONWords["adjective"]
    #count the adjective list length
    numberOfAdjectives = len(adjectives)
    #generate a random adjective from the list
    randomAdjective = adjectives[random.randrange(0, numberOfAdjectives-1)]
    #print the random adjective    
    
    #define the noun list
    nouns = theJSONWords["noun"]
    #count the noun list length
    numberOfNouns = len(nouns)
    #generate a random noun from the list
    randomNoun = nouns[random.randrange(0, numberOfNouns-1)]
    
    #define the adverb list
    adverbs = theJSONWords["adverb"]
    #count the adverb list length
    numberOfAdverbs = len(adverbs)
    #generate a random adverb from the list
    randomAdverb = adverbs[random.randrange(0, numberOfAdverbs-1)]
    
    #define the verb list
    verbs = theJSONWords["verb"]
    #count the verb list length
    numberOfVerbs = len(verbs)
    #generate a random verb from the list
    randomVerb = verbs[random.randrange(0, numberOfVerbs-1)]

    #define the location list
    locations = theJSONWords["location"]
    #count the adverb list length
    numberOfLocations = len(locations)
    #generate a random location from the list
    randomLocation = locations[random.randrange(0, numberOfLocations-1)]
    
    print "The %s %s %s %s %s" % (randomAdjective, randomNoun, randomAdverb, randomVerb, randomLocation)
    
#    print theJSONWords["adjective"]
    
def main():
    
    iNeedAPromptUrl = "http://www.ineedaprompt.com/dictionary.json"
    
    webUrl = urllib2.urlopen(iNeedAPromptUrl)
    if webUrl.getcode() == 200:
        data = webUrl.read()
        madLibs(data)
        
    else:
        print "Received an error from the server, cannot retreive the results, error:" + str(webUrl.getcode())
    
if __name__ == "__main__":
    main()
    