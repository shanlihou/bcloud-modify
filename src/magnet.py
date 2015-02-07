#import urllib2 
import urllib.request
import re
import sys
def getUrlList(urlPath):
	response = urllib.request.urlopen(urlPath)
	html = response.read()
	html = html.decode('utf-8')
	pattern = re.compile(r'http://www\.btspread\.com/magnet/detail/hash/[A-F0-9]+')
	patFind = pattern.search(html)
	if (patFind):
		matchList = pattern.findall(html)
		return matchList
	return None

def getMagnet(urlPath):
	response = urllib.request.urlopen(urlPath)
	html = response.read()
	html = html.decode('utf-8')
	pattern = re.compile(r'(magnet:\?xt=urn:btih:[^"\']+)" class=')
	patFind = pattern.search(html)
	if (patFind):
		print(patFind.group(1) + '\n')
		return patFind.group(1) + '\n'
	return None

def getAllMagnet(code):
	print('hello')
	List = getUrlList('http://www.btspread.com/search/' + code)
	if (List != None):
		magList = [None] * len(List)
		for i in range(len(List)):
			magList[i] = getMagnet(List[i])
		print('hello')
		print(magList)
		return magList
	return None

#if (len(sys.argv) == 2):
#	getAllMagnet(sys.argv[1])
