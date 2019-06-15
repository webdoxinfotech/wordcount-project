from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
	return render(request, 'home.html', {'color1':'red', 'color2': 'green'})


def eggs(request):
	return HttpResponse('Eggs are Great!')


def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			worddictionary[word] += 1
		else:
			worddictionary[word] = 1
	worddictionary = sorted(worddictionary.items(), key=operator.itemgetter(0), reverse=True)
	return render(request, 'count.html', \
		{'fulltext': fulltext, 'wordlist':len(wordlist), 'worddictionary': worddictionary})