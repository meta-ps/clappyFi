from django.shortcuts import render,redirect

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
    
    
    return render(request,'userpage.html',{'WalletAddress':WalletAddress})

