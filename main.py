import requests
from bs4 import BeautifulSoup as bs
#Getting the external IP <Start>
choice = input('Do you want the script to automatically detect your IP Address or Do you want to enter a custom IP Address? (auto/custom): ')
external_ip = requests.get('http://checkip.dyndns.com/')
tempsoup = bs(external_ip.content, 'html.parser')
body = str(tempsoup.find('body').text).replace('Current IP Address: ', '')

'''external_ip = os.popen('nslookup myip.opendns.com resolver1.opendns.com').read()
external_ip = external_ip.split('myip.opendns.com')
address = external_ip[1].split('Address: ')
external_ip = address[1]
external_ip = external_ip.replace(" ", "")
external_ip = external_ip.replace("\n", "")'''

if choice == "auto":
    pass
elif choice == "custom":
    body = input('Please enter the custom IP Address: ')
#<End>

#Getting IP Location by scraping ipinfo.io <Start>

link = "https://ipinfo.io/" + body + "/json"
content = requests.get(link).content

soup = bs(content, 'html.parser')
information = soup.find('pre')
soup = str(soup)
soup = soup.replace('{', '').replace('}' , '').replace('"readme": "https://ipinfo.io/missingauth"', '')
location = soup.split(',')
location[4] = location[4].replace('"loc": "', '').replace('"', '').replace('\n', '').replace(' ', '') +',' + location[5] 
test = soup.split('\n')
test.pop(10)
test.pop(9)
soup = ''
for x in test:
    print(x)
print('  "link to loc": "https://google.com/maps/search/' + location[4])
#<End>
