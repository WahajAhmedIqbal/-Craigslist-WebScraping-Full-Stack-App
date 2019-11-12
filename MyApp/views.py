import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models

BASE_CRAIGLIST_URL = 'https://pakistan.craigslist.org/search/jjj?query={}'

def home(request):
    return render(request ,'base.html')
 
def new_search(request):
    search = request.POST.get('search')
    models.search.objects.create(search=search)
    # models.Search.object.create(search=search)
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data , features='html.parser')
    post_listings = soup.find_all('li',{'class' : 'result-row'})

    final_postings = []

    for post  in post_listings:
        post_title = post.find(class_ = 'result-title').text
        post_url = post.find('a').get('href')
        post_price = post.find(class_ = 'result-price').text

        final_postings.append((post_title, post_url ,post_price))


    stuff_for_frontend = {
        'search' : search,
        'final_postings': final_postings,
    }
    return render(request, 'new_search.html ' , stuff_for_frontend  )