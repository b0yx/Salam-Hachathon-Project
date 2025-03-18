from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request, 'registration/Login.html')

def signup(request):
    return render(request, 'registration/signup.html')
