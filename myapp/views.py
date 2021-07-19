from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dic = PyDictionary()
    meaning = dic.meaning(search)
    synonyms = dic.synonym(search)
    antonyms = dic.antonym(search)
    data = {
        'meaning':meaning['Verb'][0],
        'synonyms':synonyms,
        'antonyms':antonyms,
    }
    return render(request,"word.html",data)