from django.shortcuts import redirect, render, HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import Link




# Create your views here.
def homePage(request):
    data = Link.objects.all()

    if request.method == 'POST':
        site = request.POST.get('site', '')

        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            print(link_address)

            Link.objects.create(link=link_address, name=link_text)

            return redirect('home')

    return render(request, 'base/index.html', {'data': data})



def clear(request):
    Link.objects.all().delete()
    return redirect('home')