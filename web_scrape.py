from bs4 import BeautifulSoup
import requests

# Not all countries are available from this source

response = requests.get(
    'https://codesubmit.io/blog/software-engineer-salary-by-country/'
)

print(response.status_code)