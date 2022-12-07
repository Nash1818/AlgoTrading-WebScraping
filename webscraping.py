import requests
from bs4 import BeautifulSoup
import time

print('put a difficult skill')
no_skill= input('>')
print(f'Unknown skill filtering: {no_skill}')

def find_jobs():
    html_test = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_test)
    soup= BeautifulSoup(html_test,'lxml')
    jobs=soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    #print(job)
    #Use enumerate to going through to the Index as well, for the advantage check the loop ahead...
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            comapny_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')  # We use replace to remove empty spaces....
            skills=job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            #print(published_date)
            #print(skills)
            #print(comapny_name)
            if no_skill not in skills:
                # Writing to files......
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'Company Name: {comapny_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'MoreInfo: {more_info}')
                    #print('')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'wait bruhhhh for {time_wait} minutes!')
        time.sleep(time_wait*60)