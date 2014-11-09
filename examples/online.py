from PIL import Image
import mechanize,cookielib
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
from StringIO import StringIO
import json, timeit
from CaptchaParser import CaptchaParser

br= mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

print "Fetching Captcha"

r=br.open('https://academics.vit.ac.in/parent/parent_login.asp')
html=r.read()
soup=BeautifulSoup(html)
im = soup.find('img', id='imgCaptcha')
image_response = br.open_novisit(im['src'])
img=Image.open(StringIO(image_response.read()))
imgcpy=img.copy()
starttime = timeit.default_timer()
parser=CaptchaParser()
captcha=parser.getCaptcha(img)
stoptime = timeit.default_timer()

print "Recognized Captcha:"+str(captcha)+" in "+str(stoptime-starttime)
br.select_form('parent_login')

regno=raw_input("Registration Number:")
dob=raw_input("Date of Birth:")

br.form['wdregno']=regno
br.form['vrfcd']=str(captcha)
br.form['wdpswd'] = dob

print "Logging in User:"+str(regno)

response=br.submit()

if(response.geturl()=="https://academics.vit.ac.in/parent/home.asp"):
	print"Success!"

else:
	print "Failed :("