from django.shortcuts import render
from Mobile.models import Mobile as mob

# Create your views here.

def test(request):

    msg="HI IN NEW THEEM"

    return render(request,'Mobile/mobile.html',{'form':msg})


def Mobile (request):



    if (request.method=='POST'):

        return render(request, 'Mobile/newmobile.html', {})

    else:
        mydata = mob.objects.all()




        return render(request,'Mobile/newmobile.html',{'data':mydata})