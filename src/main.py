import requests


### lines
# http://newsapi.org/v2/everything?
# http://newsapi.org/v2/top-headlines?



### parameters
# sources=bbc-news&
# from=2020-12-02&
# sortBy=popularity& relevancy
# q=Apple&
# country=br&
# category



url = ('http://newsapi.org/v2/top-headlines?'
       'country=br&'
       'apiKey=00c2a287a719499b88d1402073612edd')

response = requests.get(url)
print(response.json())


