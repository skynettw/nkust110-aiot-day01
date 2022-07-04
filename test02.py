import requests
url = "https://www.nkust.edu.tw/p/406-1000-8221,r1363.php"
html = requests.get(url).text
print(html)