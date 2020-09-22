from django.shortcuts import render
import os #اوامر النظام
import platform #مواصفات النظام
from datetime import datetime,date


# Create your views here.


def home(request):#the word "request " between the parentheses is a parametere
    time=datetime.now()
    x=[1,2,3,4,5,6,7,8,9,10,11]
    y=['one','tow','three']
    user='abdulhaleem alsalahi'
    z='file:///C:/Users/mhf/Desktop/WEB/HTML/HTML/www.w3schools.com/html/html_colors.html'
    line=date(2020,9,9)
    remainingtime=datetime(2020,9,25,10,10,12)

    return render(request,'Happ/index.html ',{
        #'dir':os.getcwd(),#متغير يعطينا المسار ابذي نعمل عليه حاليا
        #'dir1':platform.platform, #متغير يعطينا معلومات النظام
        #'name':False, #قيمة فارغة
        #'age':24, #قيمة محددة للمتغير
        #'city':'', #قيمة  فارغة لن يتم تعويضها بالقيمة التلقائية انظر الى ملف الهوتمل
        #'num':1234567891011,
        #'number':10,
        #'Father_name':'ali',
        #'greetings':'hello',
        'created':time,#date filter
        'ran':x,#randum and slice filters
        #'username':user,#slugify filter
        #'timeline':line, #timesince filter
        #'remainedtime':remainingtime,#timeuntil filter
        'product':'data analysis report',#turncatewords and turncatecharch filters
        'list':y, #unorder_list filter
        'urls':z,#urlize filter
    })