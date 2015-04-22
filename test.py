import sys
import os
import re
from bcloud import auth
from bcloud.RequestCookie import RequestCookie
from bcloud import util
from bcloud import pcs
from bcloud.magnet import magnet
from bcloud import net
import string
cookie = RequestCookie()
tokens = {}
def writeCookie(fileName, cookie):
	fileWrite = open(fileName, 'w')
	str = ''
	for key in cookie:
		str = str + key + '='
		str = str + cookie[key] + '; '
	fileWrite.write(str)
	fileWrite.close()
def readCookie():
	fileRead = open('cookie.txt', 'r')
	return fileRead.read()
def saveTokens(tokens):
	fileWrite = open('tokens.txt', 'w')
	for k in tokens:
		fileWrite.writelines(k + '\n')
		fileWrite.writelines(tokens[k] + '\n')
def readTokens():
	tokens = dict()
	fileRead = open('tokens.txt', 'r')
	flag = 0
	key = ''
	for line in fileRead:
		if (flag == 0):
			key = line[:-1]
			flag = 1
		else:
			tokens[key] = line[:-1]
			flag = 0
	return tokens


def login():
	global cookie
	global tokens
	if (os.path.exists('cookie.txt')):
		cookie.load(readCookie())
	if (os.path.exists('tokens.txt')):
		tokens = readTokens()
		return
	
	baiduid = auth.get_BAIDUID()
	cookie.load_list(baiduid)
	print(cookie)

	token = auth.get_token(cookie)
	print(token)

	hosupport, info = token
	tokens['token'] = info
	cookie.load_list(hosupport)
	cookie.load('cflag=65535%3A1; PANWEB=1;')
	print(tokens)
	print('cookie is ')
	print(cookie)
	ubi = auth.get_UBI(cookie, tokens)
	print(ubi)

	cookie.load_list(ubi)
	print(cookie)
	username = input('please input the name:')
	check_ret = auth.check_login(cookie, tokens, username)
	print(check_ret)


	ubi_cookie, status = check_ret
	cookie.load_list(ubi_cookie)
	codeString = status['data']['codeString']
	vcodetype = status['data']['vcodetype']
	if (codeString):
		print(codeString)
	key = auth.get_public_key(cookie, tokens)
	print(key)


	pubkey = key['pubkey']
	rsakey = key['key']
	password = input('please input the passwd:')
	password_enc = util.RSA_encrypt(pubkey, password)
	post_ret = auth.post_login(cookie, tokens, username, password_enc, rsakey, '', codeString)
	print(post_ret)
	
	errno, query = post_ret
	print(errno)
	print(cookie)

	if errno == 257:
		vcodetype = query['vcodetype']
		codeString = query['codeString']
		vcode = auth.get_signin_vcode(cookie, codeString)
		fileWrite = open('img', 'wb')
		print(type(vcode))
		fileWrite.write(vcode)
		fileWrite.close()
		os.system('display img')
		verifycode = input('please input the verifycode:\n')
		print(verifycode)
		post_ret = auth.post_login(cookie, tokens, username, password_enc, rsakey, verifycode, codeString)
		print (post_ret)
		
		errno, query = post_ret
	cookie.load_list(query)
	bdstoken = auth.get_bdstoken(cookie)
	print(bdstoken)
	tokens['bdstoken'] = bdstoken
	print('\n\n\n**********')
	print(type(cookie))
	print(type(cookie.output()))
	print(cookie)
	fileWrite = open('cookie.txt', 'w')
	fileWrite.write(str(cookie))
	fileWrite.close()
	print(type(tokens))
	print(tokens)
	print('*************\n\n\n')
	saveTokens(tokens)
	print(readTokens())
def addBTTask(source_url):
	global cookie
	global tokens
	save_path = '/'
	cloud_ret = pcs.cloud_query_magnetinfo(cookie, tokens, source_url, save_path)
	pattern = re.compile(r'\.(mp4|avi|rmvb|wmv|mkv)$', re.I)
	print(cloud_ret)
	if 'error_code' in cloud_ret:
		print('error_code')
		return False
	
	listCount = cloud_ret['total']
	selectList = []
	for i in range(listCount):
		patFind = pattern.search(cloud_ret['magnet_info'][i]['file_name'])
		if (patFind):
			selectList.append(i + 1)
	print(selectList)

	add_ret = pcs.cloud_add_bt_task(cookie, tokens, source_url, save_path, selectList, '')
	print(add_ret)
	if (not ('error_code' in add_ret)):
		return True
	while(add_ret['error_code'] == -19):
		req = net.urlopen(add_ret['img'], {'Cookie': cookie.header_output()})
		img_data = req.data
		fileWrite = open('btImg', 'wb')
		print(img_data)
		fileWrite.write(img_data)
		fileWrite.close()
		os.system('display btImg')
		vcode = input('please input the verifycode:\n')
		add_ret = pcs.cloud_add_bt_task(cookie, tokens, source_url, save_path, selectList, '', add_ret['vcode'], vcode)
		print(add_ret)
		if (not ('error_code' in add_ret)):
			return True
	return False
def print_task():
	global cookie
	global tokens
	list_task_ret = pcs.cloud_list_task(cookie, tokens)
	ids = []
	for i in list_task_ret['task_info']:
		ids.append(i['task_id'])
	task_info_ret = pcs.cloud_query_task(cookie, tokens, ids)
	task_info = task_info_ret['task_info']
	for i in task_info:
		print('\n')
		print(task_info[i]['task_name'])
		file_size = int(task_info[i]['file_size'])
		finish_size = int(task_info[i]['finished_size'])
		print(str(file_size / 1024 / 1024 / 1024) + 'GB')
		print(finish_size * 100 / file_size)
def printMag(magList, sizeList):
	for i in range(len(magList)):
		print(i)
		print(magList[i] + sizeList[i])
def addTaskSeq(magList, raw):
	for i in range(raw, len(magList)):
		if (addBTTask(magList[i])):
			return i + 1
	return 0
	
def main():
	login()
	magList = []
	sizeList = []
	downSeq = 0
	while(True):
		ret = input('please input the operation:')
		if (ret == 'q'):
			break
		elif (ret == 'pt'):
			print_task()
		elif (ret == 'pm'):
			printMag(magList, sizeList)

		elif (ret == 'c'):
			code = input('please input the code:')
			magList, sizeList = magnet.getAllMagnet(code)
		elif (ret == 'd'):
			raw = int(input('please input the raw:'))
			addBTTask(magList[raw])
		elif (ret == 's'):
			downSeq = addTaskSeq(magList, downSeq)
			print(downSeq)
		elif (ret == 'cs'):
			downSeq = 0

			
	
main()
