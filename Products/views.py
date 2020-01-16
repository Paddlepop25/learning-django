from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World!")
    
def xyz(request):
    return render(request, 'index.template.html')