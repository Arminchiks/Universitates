import requests
import json

result=requests.get("http://universities.hipolabs.com/search?country=NIGER")
universities=json.loads(result.content)

uni_list=[]

for uni in universities:
    uni_list.append(uni["name"])

uni_list=list(dict.fromkeys(uni_list))

uni_list.sort()

for uni in uni_list:
    print(uni)
