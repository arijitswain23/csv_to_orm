from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import csv
from app.models import *
def insert_bank(self):
    with open('C:\\Users\\ARIJIT SWAIN\\Desktop\\DjangoProject\\arijit\\Scripts\\project45\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
    return HttpResponse('Bank data is inserted successfully')


def insert_branch(self):
    with open('C:\\Users\\ARIJIT SWAIN\\Desktop\\DjangoProject\\arijit\\Scripts\\project45\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                br=i[2]
                ad=i[3]
                co=i[4]
                ci=i[5]
                d=i[6]
                s=i[7]

                BRO=Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contact=co,city=ci,district=d,state=s)
                BRO.save()
    return HttpResponse('Branch data is inserted successfully')


def insert_business(self):
    with open('C:\\Users\\ARIJIT SWAIN\\Desktop\\DjangoProject\\arijit\\Scripts\\project45\\app\\Business-employment-data-september-2022-quarter-csv.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            sr=i[0]
            BO=Business.objects.filter(Series_reference=sr)
            if BO:
                sr=i[1]
                pe=i[2]
                dv=i[3]
                su=i[4]
                st=i[5]
                un=i[6]
                ma=i[7]
                s=i[8]
                g=i[9]
                st1=i[10]
                st2=i[11]
                st3=i[12]

                BSO=Branch(Series_reference=BO[0],Period=pe,Data_value=dv,Suppressed=su,STATUS=st,UNITS=un,Magnitude=ma,Subject=s,Group=g,Series_title_1=st1,Series_title_2=st2,Series_title_3=st3)
                BSO.save()
    return HttpResponse('Business data is inserted successfully')
            










