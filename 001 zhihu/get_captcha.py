#coding:utf-8
import requests
import cookielib
import time
from PIL import Image

# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

for i in range(1,2):
	session = requests.session()
	t = str(int(time.time() * 1000))
	captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login&lang=cn"
	r = session.get(captcha_url, headers=headers)
	with open('captcha' +str(i) +'.png','wb') as f:
		f.write(r.content)
		f.close()
		#im=Image.open('captcha' +str(i) +'.png')
		#im.save('captcha' +str(i) +'.png')

