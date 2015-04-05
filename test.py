import sys
import os
from bcloud import auth
from bcloud.RequestCookie import RequestCookie
from bcloud import util
from bcloud import pcs
def login():
	baiduid = auth.get_BAIDUID()
	cookie = RequestCookie()
	cookie.load_list(baiduid)
	print(cookie)

	token = auth.get_token(cookie)
	print(token)

	tokens = {}
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
	username = '分是否收费'
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
	password = '410015216'
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

	source_url = input('please input the url:\n')
	save_path = '/'
	cloud_ret = pcs.cloud_query_magnetinfo(cookie, tokens, source_url, save_path)
	print(cloud_ret)
	
	listCount = cloud_ret['total']
	selectList = [i for i in range(1, listCount + 1)]
	print(selectList)


	add_ret = pcs.cloud_add_bt_task(cookie, tokens, source_url, save_path, selectList, '')
	print(add_ret)
login()

