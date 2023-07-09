from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time
import pandas as pd


driver = webdriver.Chrome()
driver.get(r"C:\Users\91626\Downloads\chromedriver\chromedriver")
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys("ch***********@iith.ac.in")

pword = driver.find_element(By.ID, "password")

pword.send_keys("*********")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

url = "https://www.linkedin.com/company/bumbleinc/people/"

start = time.time()
driver.get(url)

x = 0
y = 800
driver.execute_script(
    f"window.scrollTo({x},{y})")

time.sleep(10)

src = driver.page_source

soup = BeautifulSoup(src, 'lxml')
info = soup.find(
    'div', {'class': 'org-grid__content-height-enforcer'})
total_loc = info.find("h2")
total_emp = total_loc.get_text().strip()
info_c = info.find('div', {'class': 'artdeco-carousel__content'})
insights1 = info_c.find('li', {'data-item-index': "0"})
info_loc = insights1.find('div', {
                          'class': "insight-container"})
loc_count = []
loc = []
for num in info_loc.find_all("strong"):
    loc_count.append(num.get_text().strip())

for locs in info_loc.find_all("span", {'class': "org-people-bar-graph-element__category"}):
    loc.append(locs.get_text().strip())

insights2 = info_c.find('li', {'data-item-index': "1"})
info_clg = insights2.find('div', {
                          'class': "insight-container"})
clg_count = []
clg = []
for num in info_clg.find_all("strong"):
    clg_count.append(num.get_text().strip())
for clgs in info_clg.find_all("span", {'class': "org-people-bar-graph-element__category"}):
    clg.append(clgs.get_text().strip())

element = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
element.click()


insights3 = info_c.find('li', {'data-item-index': "2"})
info_roles = insights3.find('div', {
                            'class': "insight-container"})

roles_count = []
roles = []
for num in info_roles.find_all("strong"):
    roles_count.append(num.get_text().strip())
for role in info_roles.find_all("span", {'class': "org-people-bar-graph-element__category"}):
    roles.append(role.get_text().strip())

insights4 = info_c.find('li', {'data-item-index': "3"})
info_skills = insights4.find('div', {
                             'class': "insight-container"})
skills_count = []
skills = []
for num in info_skills.find_all("strong"):
    skills_count.append(num.get_text().strip())

for skill in info_skills.find_all("span", {'class': "org-people-bar-graph-element__category"}):
    skills.append(skill.get_text().strip())

element.click()


insights5 = info_c.find('li', {'data-item-index': "4"})
info_studied = insights5.find('div', {
                              'class': "insight-container"})

studied_count = []
studied = []
for num in info_studied.find_all("strong"):
    studied_count.append(num.get_text().strip())

for study in info_studied.find_all("span", {'class': "org-people-bar-graph-element__category"}):
    studied.append(study.get_text().strip())


fields = {"Location": loc, "Counts of Employees at Location": loc_count, "Universities/Clg": clg, "Counts of Employees at Clg": clg_count,
          "Roles": roles, "Counts of Employees for Roles": roles_count, "Skills": skills, "Counts of Employees for Skills": skills_count,
          "Field of Study": studied, "Counts of Employees for those fields": studied_count}

df = pd.DataFrame(fields)

df.to_csv("Analytic_Data.csv")
