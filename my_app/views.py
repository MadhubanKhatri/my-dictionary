from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from bs4 import BeautifulSoup
import requests



# Create your views here.
def home(request):
	if request.method == "POST":
		word = request.POST['word']
		url = 'https://www.dictionary.com/browse/'+word
		r = requests.get(url)
		data = r.content
		soup = BeautifulSoup(data, 'html.parser')
		span = soup.find_all('span', {"class": "one-click-content"})

		param = {'text': span[0].text, 'word': word}
		return render(request, 'index.html', param)
	else:
		return render(request, 'index.html')