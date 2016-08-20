"""Example of Python client calling Knowledge Graph Search API.
   https://developers.google.com/knowledge-graph/"""
import json
import urllib.request, urllib.parse
from nlp import quote

api_key = open('.google_api_key').read()
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'

def query(term, vocal = True):
    params = {
        'query': term,
        'limit': 10,
        'indent': True,
        'key': api_key,
    }
    url = service_url + '?' + urllib.parse.urlencode(params)
    if vocal: print(url)
    response = urllib.request.urlopen(url).read().decode('ascii')
    response = json.loads(response)
    
    ignore = ["image","detailedDescription"]
    def r_process(name, d):
        out = []
        if isinstance(d, dict):
            d = d.items()
        for k, v in d:
            if k in ignore:
                continue
            if isinstance(v, dict):
                out += r_process(name, v)
            if isinstance(v, list):
                out += r_process(name, [(k,i) for i in v])
            else:
                out.append("<(*,{},{}) --> {}>.".format(str(name),quote(v),quote(k)))
        return out
        
    out = []
    for element in response['itemListElement']:
        q = "q\"{}\"".format(element['result']['@id'])  # Name of query response
        e = "<(*,{},{}) --> qRESULT>.".format(term, q)              # Chance that term is same as query response
        out.append(e)
        out += r_process(q, element['result'])
        if 'detailedDescription' in element['result']:
            out += r_process(q, element['result']['detailedDescription'])
    return out

    
if __name__=="__main__":
    inx = input("SEARCH: ")
    for x in query(inx):
        print(x)
    