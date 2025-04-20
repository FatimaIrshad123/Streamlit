from bs4 import BeautifulSoup
import requests
import time


print('Put the name of the skill you want to search for:')
unfamiliar_skill = input('>')
print(f'Filtering jobs for {unfamiliar_skill}...')

def find_jobs():
    html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?compCluster=Google+India+Pvt+Ltd').text
    soup = BeautifulSoup(html_text, 'lxml')
    #print(soup.prettify())
    jobs = soup.find('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = jobs.find('span', class_='sim-posted').span.text.replace(' ', '')
        if 'few' in published_date:
            company_name = jobs.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href'] 
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More Info: {more_info} \n')
                    print(f'Company Name: {company_name.strip()}')
                    print(f'Required Skills: {skills.strip()}')
                    print(f'More Info: {more_info}')
                print(f'File saved: {index}.txt')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

#with open("home.html", "r") as html_file:
    #content = html_file.read()
    #soup = BeautifulSoup(content, "lxml")
    #courses_cards = soup.find_all('div', class_='card')
    