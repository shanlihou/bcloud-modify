#import urllib2 
import urllib.request
import re
import sys
class magnet:
	def getUrlList(urlPath):
		response = urllib.request.urlopen(urlPath)
		html = response.read()
		html = html.decode('utf-8')
		pattern = re.compile(r'http://www\.btspread\.com/magnet/detail/hash/[A-F0-9]+')
		sizePat = re.compile(r'</td> <td class="files\-size">([0-9A-Z\.]+)</td>')
		patFind = pattern.search(html)
		if (patFind):
			matchList = pattern.findall(html)
			sizeList = sizePat.findall(html)
			return matchList, sizeList
			
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
		List, sizeList = magnet.getUrlList('http://www.btspread.com/search/' + code)
		listFlag = []
		magList = []
		if (List != None):
			for url in List:
				sameFlag = 0
				for i in listFlag:
					if (url == i):
						sameFlag = 1
						break;
				if (sameFlag == 1):
					continue
				listFlag.append(url)
				magList.append(magnet.getMagnet(url))
		return magList, sizeList
#if (len(sys.argv) == 2):
#	getAllMagnet(sys.argv[1])
#magnet.getAllMagnet(sys.argv[1])
