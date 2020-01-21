import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path="C:/Users/multicampus/Downloads/chromedriver.exe", options=options)
browser.get("http://kmanifesto.or.kr/index.php/front/localList?mtype=assembly")
element = browser.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div[3]/div[1]/div")
element.click()
result = []
for r in range(8):
    people = browser.find_element_by_css_selector("#container").find_elements_by_tag_name("div.wrap")[r].find_elements_by_tag_name("div.district")[0].find_elements_by_tag_name("div.btnlocal")
    for k in range(1, len(people)+1):
        element = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[3]/div[{}]/div[2]/div[{}]".format(r+1, k))
        element.click()

        # time.sleep(10)
        # tag_names = browser.find_element_by_css_selector(".ptype").find_element_by_css_selector(".title").find_elements_by_tag_name("a")
        # tag_names = browser.find_elements_by_tag_name("div")[0].find_elements_by_tag_name("tbody")[0].find_elements_by_tag_name("tr")
        people = browser.find_element_by_css_selector(".title").text
        for j in range(len(people)):
            if people[j] == '(':
                print(people[j+1:-1])
                break
        for i in range(len(browser.find_elements_by_tag_name("div")[0].find_elements_by_tag_name("tbody"))):
            if i != 1:
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
                    else:
                        a = com.text
                    try:
                        print(a)
                    except UnicodeEncodeError as e:
                        result.append(e)
                        print(e)
        back_button = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div/input[2]")
        back_button.click()
print(result)
# /html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]
# /html/body/div/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]