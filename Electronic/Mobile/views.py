from django.shortcuts import render

# Create your views here.

def test(request):

    msg="HI IN NEW THEEM"

    return render(request,'Mobile/mobile.html',{'form':msg})