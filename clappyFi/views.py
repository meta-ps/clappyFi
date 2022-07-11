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



def UserPage(request):
    WalletAddress = request.session['WalletAddress']
    all_unique_titles = set()
    converter = lambda x: x.replace(' ', '_')


    baseURL = 'https://eth-mainnet.g.alchemy.com/v2/<alchemy_api_key>'
    url = baseURL+'/getNFTs/?owner=0x8a502e0e3EDa70eAE505a6Fa0FA49eB29b85fe5B'
    x = requests.get(url)
    x = x.json()
    print('xxxxxxxxxxxxxxxxxxxxxx')
    # print(x)
    for i in x['ownedNfts']:
        all_unique_titles.add(i['title'])


    with open('personal.json', 'w') as json_file:
        json.dump(x, json_file)
        
    print(all_unique_titles)
    my_list = list(map(converter, all_unique_titles))


    
    return render(request,'userpage.html',{'WalletAddress':WalletAddress,'all_unique_titles':my_list})

