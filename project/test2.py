from alchemyapi import AlchemyAPI
from encodings import hex_codec
from encodings import ascii
import httplib,urllib2
import json
import sys

alchemyapi = AlchemyAPI()

prompt = " "
api_key = "83da2d0deaef076648b28972905d2f8c1f5e3c0f"
url = raw_input(prompt)
# url ="www.google.com"

try:
	#Accessing Alchemy API to get the relevance
	url = "http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?apikey=%s&url=%s&outputMode=json" % (api_key,url)
	json = urllib2.urlopen(url).read()
	
	#Parsing the json payload
	the_data = eval(json)
	
	#Retrieving relenace from the payload
	print the_data ['keywords'][0]['relevance']
    

	
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.\r'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'Sorry! Looks like Klout doesn\'t have info on that soldier!\r'
        print 'Error code: ', e.code
