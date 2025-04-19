from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?compCluster=Google+India+Pvt+Ltd').text

soup = BeautifulSoup(html_text, 'lxml')
#print(soup.prettify())
jobs = soup.find('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    company_name = jobs.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    skills = job.find('span', class_='srp-skills').text.replace(' ', '')
    published_date = jobs.find('span', class_='sim-posted').span.text.replace(' ', '')

    print(f'''
    Company Name: {company_name}
    Required Skills: {skills}
    ''')

    print('')

#with open("home.html", "r") as html_file:
    #content = html_file.read()
    #soup = BeautifulSoup(content, "lxml")
    #courses_cards = soup.find_all('div', class_='card')
    