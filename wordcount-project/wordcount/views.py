from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')


def counted(request):
    fulltext = request.GET['fulltext']
    wordlist =fulltext.split()

    worddict = {}

    for word in wordlist:
        if word in worddict:
            # Increase count
            worddict[word] += 1
        else:
            # Add word to worddict
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'counted.html', {'fulltext': fulltext,
                  'count': len(wordlist), 'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')