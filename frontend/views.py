from django.http import HttpResponse

def home(request):
    if request.method =="POST":
        return HttpResponse("Hello Home!")
    else:
        return HttpResponse(request.method)



