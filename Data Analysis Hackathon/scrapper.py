from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd


driver = webdriver.Chrome()
driver.get(r"C:\Users\91626\Downloads\chromedriver\chromedriver")
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys("ch20btech11012@iith.ac.in")

pword = driver.find_element(By.ID, "password")

pword.send_keys("@267Ekshan")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.maximize_window()
url = "https://www.linkedin.com/company/bumbleinc/people/"

start = time.time()
driver.get(url)

x = 0
y = 500
driver.execute_script(
    f"window.scrollTo({x},{y})")

time.sleep(5)

src = driver.page_source

soup = BeautifulSoup(src, 'lxml')
show_more = driver.find_element(
    By.XPATH, "//button[@aria-label='Show more people filters']")
show_more.click()
time.sleep(5)
info = soup.find(
    'div', {'class': 'org-grid__content-height-enforcer'})
total_loc = info.find("h2")
total_emp = total_loc.get_text().strip()
infom = info.find('div', {'class': "org-people__insights-container"})
info_c = infom.find('div', {'class': "artdeco-carousel__content"})
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


insights3 = info_c.find('li', {'data-item-index': "2"})
info_roles = insights3.find('div', {
                            'class': "insight-container"})

roles_count = []
roles = []
for num in info_roles.find_all("strong"):
    roles_count.append(num.get_text().strip())
for role in info_roles.find_all("span", {'class': "org-people-bar-graph-element__category"}):
    roles.append(role.get_text().strip())


element = driver.find_element(By.XPATH, "//button[@aria-label= 'Next']")
driver.execute_script("arguments[0].click();", element)
time.sleep(5)


driver.execute_script("arguments[0].click();", element)
time.sleep(5)

src1 = driver.page_source
soup1 = BeautifulSoup(src1, 'lxml')
info = soup1.find(
    'div', {'class': 'org-grid__content-height-enforcer'})
infom = info.find('div', {'class': "org-people__insights-container"})
info_c = infom.find('div', {'class': "artdeco-carousel__content"})


insights4 = info_c.find('li', {'data-item-index': "3"})
info_skills = insights4.find('div', {
                             'class': "insight-container"})
skills_count = []
skills = []
for num in info_skills.find_all("strong"):
    skills_count.append(num.get_text().strip())

for skill in info_skills.find_all("span", {'class': "org-people-bar-graph-element__category"}):
    skills.append(skill.get_text().strip())


driver.execute_script("arguments[0].click();", element)
time.sleep(5)

src2 = driver.page_source
soup1 = BeautifulSoup(src2, 'lxml')
info = soup1.find(
    'div', {'class': 'org-grid__content-height-enforcer'})
infom = info.find('div', {'class': "org-people__insights-container"})
info_c = infom.find('div', {'class': "artdeco-carousel__content"})


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
          "Field of Study": studied, "Counts of Employees for those fields": studied_count, "Total_Employees": total_emp}

df = pd.DataFrame(fields)

df.to_csv("Analytic_Data.csv")
