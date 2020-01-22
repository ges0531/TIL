import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import pymysql


con= pymysql.connect(host="70.12.247.60", user="root",password="root",db="sakila",charset="utf8")
cursor = db.cursor()

sql = '''
CREATE TABLE commitment (
    p_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    p_name VARCHAR(200) NOT NULL,
    p_district VARCHAR(200) NOT NULL,
    p_commitment VARCHAR(200) NOT NULL,
    PRIMARY KEY(p_id)
);
'''
cursor.execute(sql)

db.commit()
db.close()


options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path="C:/Users/multicampus/Downloads/chromedriver.exe", options=options)
browser.get("http://kmanifesto.or.kr/index.php/front/localList?mtype=assembly")
element = browser.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div[3]/div[1]/div")
element.click()
result = []
for r in range(1):
    people = browser.find_element_by_css_selector("#container").find_elements_by_tag_name("div.wrap")[r].find_elements_by_tag_name("div.district")[0].find_elements_by_tag_name("div.btnlocal")
    for k in range(1, len(people)+1):
        element = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[3]/div[{}]/div[2]/div[{}]".format(r+1, k))
        element.click()
        people = browser.find_element_by_css_selector(".title").text
        for j in range(len(people)):
            if people[j] == '(':
                if '/' in people:
                    people = people.replace('/', '')
                if '서울특별시' in people:
                    people = people.replace('특별시', '')
                elif '광역시' in people:
                    people = people.replace('광역시', '')
                elif '충청북도' in people:
                    people = people.replace('충청북도', '충북')
                elif '충청남도' in people:
                    people = people.replace('충청남도', '충남')
                elif '전라북도' in people:
                    people = people.replace('전라북도', '전북')
                elif '전라남도' in people:
                    people = people.replace('전라남도', '전남')
                elif '경상북도' in people:
                    people = people.replace('경상북도', '경북')
                elif '경상남도' in people:
                    people = people.replace('경상남도', '경남')
                elif '경기도' in people:
                    people = people.replace('경기도', '경기')
                elif '강원도' in people:
                    people = people.replace('강원도', '강원')
                elif '제주특별자치도 ' in people:
                    people = people.replace('제주특별자치도', '제주')
                print(people[0:3]+' '+people[j+1:-1])
                break
        page = int(browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[4]/div[3]/div/span/font").text)//20
        for k in range(page+1):
            for i in range(len(browser.find_elements_by_tag_name("div")[0].find_elements_by_tag_name("tbody"))):
                if i == 2:
                    commitment = browser.find_elements_by_tag_name("div")[0].find_elements_by_tag_name("tbody")[i].find_elements_by_tag_name("tr")
                    for com in commitment:
                        if '\u2024' in com.text:
                            a = com.text.split('\u2024')
                            a = ''.join(a)
                        elif '\u2022' in com.text:
                            a = com.text.split('\u2022')
                            a = ''.join(a)
                        elif '\u2027' in com.text:
                            a = com.text.split('\u2027')
                            a = ''.join(a)
                        elif '\u2219' in com.text:
                            a = com.text.split('\u2219')
                            a = ''.join(a)
                        elif '\u2981' in com.text:
                            a = com.text.split('\u2981')
                            a = ''.join(a)
                        elif '\u30fb' in com.text:
                            a = com.text.split('\u30fb')
                            a = ''.join(a)
                        elif '\u24b6' in com.text:
                            a = com.text.split('\u24b6')
                            a = ''.join(a)
                        elif '\u1173' in com.text:
                            a = com.text.split('\u1173')
                            a = ''.join(a)
                        elif '\u301c' in com.text:
                            a = com.text.split('\u301c')
                            a = ''.join(a)
                        elif '\u2473' in com.text:
                            a = com.text.split('\u301c')
                            a = ''.join(a)
                        elif '\u2472' in com.text:
                            a = com.text.split('\u301c')
                            a = ''.join(a)
                        elif '\u2471' in com.text:
                            a = com.text.split('\u301c')
                            a = ''.join(a)
                        elif '\u2470' in com.text:
                            a = com.text.split('\u301c')
                            a = ''.join(a)
                        elif '\u246f' in com.text:
                            a = com.text.split('\u301c')
                            a = ''.join(a)
                        elif '\u2013' in com.text:
                            a = com.text.split('\u2013')
                            a = ''.join(a)
                        else:
                            a = com.text
                        print(a[:-3])
                        # except UnicodeEncodeError as e:
                        #     result.append(e)
                        #     print(e)
            browser.get("{}&page={}".format(browser.current_url, k+2))
        button = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div/input[2]")
        button.click()
print(result)
# \u301c, \u2473, \u2472, \u2471, \u2470, \u246f, \u2013