from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

df.to_csv("Employees_data/Analytic_Data.csv")


driver.get("https://www.google.com/")

company = driver.find_element(By.ID, "APjFqb")
company.send_keys("Bumble Inc Salary levels.fy", Keys.ENTER)
time.sleep(5)


driver.find_element(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']").click()

time.sleep(5)
driver.find_element(By.XPATH, "//a[@class = 'action-button login']").click()

time.sleep(6)

email = driver.find_element(
    By.XPATH, "//input[@name='username']")

email.send_keys("akshanrajverma@gmail.com")

password = driver.find_element(
    By.XPATH, "//input[@name='password']")
password.send_keys("@Ekshan267", Keys.ENTER)

time.sleep(6)

driver.execute_script("window.scrollTo(0, 700);")
time.sleep(5)

driver.find_element(
    By.XPATH, "//button[@class = 'MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root salaries_viewDataAsTable__CCiWg css-280bow']").click()

time.sleep(5)

src = driver.page_source
soup = BeautifulSoup(src, "lxml")

table = soup.find('table', {'class': "table-modal_table__1D5g2"})

data = []
for row in table.find_all("tr"):
    rows = []
    for content in row.find_all(["td", "th"]):
        rows.append(content.get_text().strip())
    data.append(rows)

data1 = pd.DataFrame(data)
data1.to_csv("Employees_data/Salaries.csv")


driver.get("https://www.levels.fyi/companies/bumble/benefits")
time.sleep(5)

driver.find_element(
    By.XPATH, "//button[@class = 'MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root benefits_viewDataAsTable__5rhHq css-280bow']").click()

src = driver.page_source
soup1 = BeautifulSoup(src, "lxml")

table1 = soup1.find('table', {'class': "table-modal_table__1D5g2"})
data = []
for row in table1.find_all("tr"):
    rows = []
    for content in row.find_all(["td", "th"]):
        rows.append(content.get_text().strip())
    data.append(rows)

benefits = pd.DataFrame(data)
benefits.to_csv("Employees_data/benefits.csv")


driver.get("https://www.sec.gov/edgar/searchedgar/companysearch")

company = driver.find_element(By.ID, "edgar-company-person")
company.send_keys("Bumble Inc")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)
types = driver.find_element(By.ID, "type")
types.send_keys("10-K")

driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)
driver.find_element(By.ID, "interactiveDataBtn").click()

time.sleep(5)

driver.find_element(By.ID, "menu_cat3").click()

time.sleep(2)
driver.find_element(By.ID, "r2").click()

time.sleep(2)
src = driver.page_source
soup1 = BeautifulSoup(src, "lxml")

balance_sheet = soup1.find('table', {'class': "report"})

data = []
for row in balance_sheet.find_all("tr"):
    rows = []
    for content in row.find_all(["td", "th"]):
        rows.append(content.get_text().strip())
    data.append(rows)

balance = pd.DataFrame(data)
balance.to_csv('Financial_data/Balance_sheet.csv', index=False)


driver.find_element(By.ID, "r3").click()
time.sleep(2)
src = driver.page_source
soup2 = BeautifulSoup(src, "lxml")

balance_sheet_Parenthetical = soup2.find('table', {'class': "report"})
data = []
for row in balance_sheet_Parenthetical.find_all("tr"):
    rows = []
    for content in row.find_all(["td", "th"]):
        rows.append(content.get_text().strip())
    data.append(rows)

balance_p = pd.DataFrame(data)
balance_p.to_csv('Financial_data/Balance_sheet_Parenthetical.csv', index=False)


driver.find_element(By.ID, "r4").click()
time.sleep(2)
src = driver.page_source
soup3 = BeautifulSoup(src, "lxml")

statement_of_ops = soup3.find('table', {'class': "report"})
data = []
counts = 0
for row in statement_of_ops.find_all("tr"):
    rows = []
    counts += 1
    if counts == 2:
        rows.append(" ")
    for content in row.find_all(["td", "th"]):
        colspan = int(content.get("colspan", 1))
        rows.extend([content.get_text().strip()]*colspan)

    data.append(rows)

SoOP = pd.DataFrame(data)
SoOP.to_csv('Financial_data/statement_of_ops.csv', index=False)

driver.find_element(By.ID, "r5").click()
time.sleep(2)
src = driver.page_source
soup4 = BeautifulSoup(src, "lxml")

statement_of_Coops = soup4.find('table', {'class': "report"})
data = []
counts = 0
for row in statement_of_Coops.find_all("tr"):
    rows = []
    counts += 1
    if counts == 2:
        rows.append(" ")
    for content in row.find_all(["td", "th"]):
        colspan = int(content.get("colspan", 1))
        rows.extend([content.get_text().strip()]*colspan)

    data.append(rows)

SoCOOP = pd.DataFrame(data)
SoCOOP.to_csv('Financial_data/statement_of_Coops.csv', index=False)

driver.find_element(By.ID, "r6").click()
time.sleep(2)
src = driver.page_source
soup5 = BeautifulSoup(src, "lxml")

statement_of_change_in_equity = soup5.find(
    'table', {'class': "report"})
data = []
for row in statement_of_change_in_equity.find_all("tr"):
    rows = []
    for content in row.find_all(["td", "th"]):
        rows.append(content.get_text().strip())
    data.append(rows)

SoCiE = pd.DataFrame(data)
SoCiE.to_csv('Financial_data/statements_of_change_in_equity.csv', index=False)

driver.find_element(By.ID, "r7").click()
time.sleep(2)
src = driver.page_source
soup6 = BeautifulSoup(src, "lxml")

cash_flows = soup6.find('table', {'class': "report"})
data = []
counts = 0
for row in cash_flows.find_all("tr"):
    rows = []
    counts += 1
    if counts == 2:
        rows.append(" ")
    for content in row.find_all(["td", "th"]):
        colspan = int(content.get("colspan", 1))
        rows.extend([content.get_text().strip()]*colspan)

    data.append(rows)

Cf = pd.DataFrame(data)
Cf.to_csv('Financial_data/statements_of_Cash_flows.csv', index=False)
