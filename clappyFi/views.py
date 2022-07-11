from dataclasses import replace
from django.shortcuts import render,redirect
import requests
import os
import json

# Create your views here.
def home(request):

    return render(request,'home.html')


def Login(request):
    request.session['WalletAddress'] = "xxx"
    if request.POST:
        WalletAddress = request.POST.get('WalletAddress')
        request.session['WalletAddress'] = WalletAddress

        print(WalletAddress)
        return redirect('userpage')
    else:
        return redirect('home')


def cleandata(xx):
    temp=""
    for i in xx:
        if i.isnumeric():
            break
    
        temp+=i
    
    temp=temp.replace(' ','_')

    return temp


def UserPage(request):
    WalletAddress = request.session['WalletAddress']
    all_unique_titles = []
    # converter = lambda x: x.replace(' ', '_')


    baseURL = 'https://eth-mainnet.g.alchemy.com/v2/<API_KEY>'
    url = baseURL+'/getNFTs/?owner=0x8a502e0e3EDa70eAE505a6Fa0FA49eB29b85fe5B'
    x = requests.get(url)
    x = x.json()
    print('xxxxxxxxxxxxxxxxxxxxxx')
    # print(x)

    with open('personal.json', 'w') as json_file:
        json.dump(x, json_file)

    for i in x['ownedNfts']:
        try:
            all_unique_titles.append([cleandata(i['title']),i['metadata']['image']])
        except:
            print('format wrong')
    
        
    print(all_unique_titles)
 
    return render(request,'userpage.html',{'WalletAddress':WalletAddress,'all_unique_titles':all_unique_titles})


def Refer(request,zzz):


    return render(request,'refer.html',{'zzz':zzz})