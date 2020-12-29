from logging import info
from bs4 import BeautifulSoup as bs
import requests
from requests.sessions import session
import urllib3
from urllib.request import unquote
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)        
import os
import time

nametype='view.php?id'
nametype1='?'
url='https://ourvle.mona.uwi.edu/login/index.php?authldap_skipntlmsso=1'
url_course=('https://ourvle.mona.uwi.edu/course/view.php?id=6230')
url_course1=('https://ourvle.mona.uwi.edu/course/view.php?id=5620')
url_course2=('https://ourvle.mona.uwi.edu/course/view.php?id=5618')
url_course3=('https://ourvle.mona.uwi.edu/course/view.php?id=5422')
url_course4=('https://ourvle.mona.uwi.edu/course/view.php?id=6983')

session_variable =requests.session()
payload={
    'username':'username',
    'password':'password'
}
response=session_variable.post(url,data=payload,verify=False) 

def courses(course_url,folder):
    directory = '/media/michel/External Drive/'+folder
    local=directory+'/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print("Folder Already Exists")

    parselink=bs(session_variable.get(course_url).text , 'html.parser')

    for data2 in parselink.find_all('li', attrs={'class','modtype_resource'}):
        for data in data2.find_all('a'):
            links=data.get('href')  
            contenturl=(session_variable.get(links,stream=True,verify=False))
            pdffiles=unquote(contenturl.url)
            filenames=pdffiles.rsplit('/', 1)[1]
            if nametype1 in filenames:
                filenames=filenames.rsplit('?', 1)[0]
            if not nametype in pdffiles:
                print(filenames)
                with open(local+filenames,'wb') as f:
                    f.write(contenturl.content)

courses(url_course,'Web_Dev')
courses(url_course4,'Stats')
courses(url_course2,'Swen')
courses(url_course3,'Net_Centric')
courses(url_course1,'Discrete_Math')
