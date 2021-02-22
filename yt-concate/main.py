import requests
url = 'https://labchem-wako.fujifilm.com/jp/product/result/product.html?fw=1000340-34-0'
Html = requests.get(url)
print(Html.text)