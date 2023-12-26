from django.shortcuts import render

# Create your views here.
def get_sweetspot(request):
    return render(request, 'SweetSpot/base.html')