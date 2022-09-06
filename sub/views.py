from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    ct = request.session.get('count',0)
    newcount = ct + 1
    request.session['count'] = newcount
    if newcount<=150:
        return render(request,'index.html',{'c':newcount})
    else:
        return HttpResponse('you are reached!!!!!!!')