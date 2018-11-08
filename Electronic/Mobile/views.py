from django.shortcuts import render
from Mobile.models import Mobile as mob

# Create your views here.

def test(request):

    msg="HI IN NEW THEEM"

    return render(request,'Mobile/mobile.html',{'form':msg})


def Mobile (request):



    if (request.method=='POST'):
        company=request.POST.get("company","")
        color = request.POST.get("color", "")
        modelno = request.POST.get("modelno", "")
        condition = request.POST.get("condition", "")
       # buy = request.POST.get("buydate", "")
        price = request.POST.get("price", "")

        datasave=mob(company=company,color=color,modelno=modelno,condition=condition,price=price)
        datasave.save()
        alldata = mob.objects.all()



        return render(request, 'Mobile/newmobile.html', {'data':alldata})

    else:
        mydata = mob.objects.all()




        return render(request,'Mobile/newmobile.html',{'data':mydata})