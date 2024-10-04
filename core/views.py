from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'live/football.html')

def start_football(request):
    if request.method == "POST":
        pass
    return render(request, 'live/football.html')