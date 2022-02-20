import requests
from bs4 import BeautifulSoup
import pandas as pd

file = "~/universitas.csv"
universities = pd.read_csv(file, sep=',', header=None)
universities.columns = ['name']
universities['name_v2'] = universities['name'].replace(' ','+',regex=True).str.lower()
#print(universities)

def parse(univ):
    url = 'https://www.google.com/search?q={univ}&oq=uni&aqs=chrome.0.69i59j46i39j46i433i512j69i59j69i57j69i60l2j69i61.1193j0j7&sourceid=chrome&ie=UTF-8'.format(univ=univ)

    r = requests.get(url)
    html_doc = r.text

    soup = BeautifulSoup(html_doc)


    span = soup.find_all('span')

    class_addres = ['BNeawe', 'tAd8D', 'AP7Wnd']
    info = []
    for class_span in span:
        if class_span.get('class') == class_addres:
            info.append(class_span.text)

    return info

address = []
for univ in universities['name']:
     info = parse(univ)
     address.append(info[0])

universities['address'] = address
universities = universities.drop(columns=['name_v2'])
pd.set_option("display.max_rows", None, "display.max_columns", 500)
print(universities)
