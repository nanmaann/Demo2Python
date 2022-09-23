from django.shortcuts import render
from .models import destinations
from .models import profile
# Create your views here.
def demo(request):
    obj=destinations.objects.all()
    pic=profile.objects.all()
    return render(request,'index.html', {'result':obj,'picture':pic})