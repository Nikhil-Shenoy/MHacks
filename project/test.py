from alchemyapi import AlchemyAPI
from encodings import hex_codec
from encodings import ascii
import httplib,urllib2
import json
import sys

alchemyapi = AlchemyAPI()

prompt = "> "
api_key = "83da2d0deaef076648b28972905d2f8c1f5e3c0f"
url = raw_input(prompt)

try:

	#Accessing Alchemy API to get the relevance
#	url2 = "http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?apikey=83da2d0deaef076648b28972905d2f8c1f5e3c0f&url=http://www.atpworldtour.com/&outputMode=json"

	# sample url: http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?apikey=83da2d0deaef076648b28972905d2f8c1f5e3c0f&url=http://www.google.com&outputMode=json 
#	json2 = urllib2.urlopen(url2).read()
	
	#Parsing the json payload MUST TO THIS TO CONVERT INTO JSON OBJECT 
#	my_data = eval(json2) 

#	print my_data

	#Retrieving relevance from the payload. SELECT THE DATA THAT YOU NEED USING THE TREE
#	print the_data ['keywords'][0]['relevance']

#	print the_data ['language']

  



	#Accessing Alchemy API to get the relevance
	url = "http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?apikey=%s&url=%s&outputMode=json" % (api_key,url)

	# sample url: http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?apikey=83da2d0deaef076648b28972905d2f8c1f5e3c0f&url=http://www.google.com&outputMode=json 
	json = urllib2.urlopen(url).read()
	
	#Parsing the json payload MUST TO THIS TO CONVERT INTO JSON OBJECT 
	the_data = eval(json) 

	#Retrieving relevance from the payload. SELECT THE DATA THAT YOU NEED USING THE TREE
#	print the_data ['keywords'][0]['relevance']

#	print the_data ['language']


#	for keyword in range(0,len(the_data['keywords'])):
	for keyword in range(0,3):
		print the_data['keywords'][keyword]['text']	
    

	
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.\r'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'Sorry! Looks like Klout doesn\'t have info on that soldier!\r'
        print 'Error code: ', e.code
