from django.http import HttpResponse

def home(request):
    my_html_code
    return HttpResponse("<html><h1>Hello World! This is Home Page</h1></html>")

def about(request):
    return HttpResponse ("I am learning Python Django at Skillshikshya")
    
def vlog(request):
    return HttpResponse ("GenZ Protest")

def contact(request):
    return HttpResponse("Contact me through : 938837617")
#about,my blog,contact, resume