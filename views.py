from django.shortcuts import render
import requests
from .models import product
from weather.forms import PriceForm
def adds(request):
    if(request.method=='POST'):
        form=PriceForm(request.POST)
        if(form.is_valid()):
            city=request.POST.get('city','')
            a=product(city=city)
            a.save()
            return render(request,'climate/index.html')
    else:
        form=PriceForm()
    return render(request,'climate/index.html',{'form':form})
def index(request):
    url= 'https://api.spoonacular.com/recipes/{69095}/tasteWidget.json'
    example=product.objects.all()
    l=[]
    for i in example:
        city=i.city
        r=requests.get(url.format(city)).json()
        a={
        'description':r['weather'][0]['description'],
        'temp':r['main']['temp'],
        'city':city,
        'img':r['weather'][0]['icon']
        }
        l.append(a)
    d={'l':l}
    return render(request,'climate/result.html',d)
