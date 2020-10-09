import requests
import os
from bs4 import BeautifulSoup
import csv



def getcompany():#Make a request and get data
    url = "http://3.95.249.159:8000/random_company"
    response = requests.request("GET", url)
    print(response.text)

def namepurpose(html):#Get name and purpose
    soup = BeautifulSoup(html, 'html.parser')
    soupall = soup.find_all('li')
    for soup in soupall:
        if 'Name' in soup.text:
            name = soup.text[soup.text.find('Name') + 6:]
        elif 'Purpose' in soup.text:
            purpose = soup.text[soup.text.find('Purpose') + 9:]
    return name, purpose


def repeat():
    lst = []
    isExists = os.path.exists('data')
    if not isExists:
        os.makedirs('data')
    for i in range(50):#Repeat 50 times
        url = "http://3.95.249.159:8000/random_company"
        response = requests.request("GET", url)
        txt = str(response.text)
        open('data/%d.html' % i, 'w').write(txt)
        name, purpose = namepurpose(txt)
        lst.append([name, purpose])
    return lst


def output(lst):#Create a csv file
    f = open('result.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['name', 'purpose'])
    for name, purpose in lst:
        csv_writer.writerow([name, purpose])
    f.close()

if __name__ == '__main__':
    getcompany()
    lst = repeat()
    output(lst)

