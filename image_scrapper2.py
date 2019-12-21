from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import time
import os
import json
import ssl

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36")
driver = webdriver.Chrome('chromedriver', options=options)


def download_image():
    while True:
        keyword = input("데이터 확보를 종료하려면 exit를 입력하세요\n검색할 이미지를 입력하세요 : ")
        if keyword == 'exit':
            break
        if ' ' in keyword:
            url_keyword = keyword.split(' ')
            url_keyword = "+".join(url_keyword)
        else:
            url_keyword = keyword
        url = 'https://www.google.com/search?q=' + url_keyword + '&source=lnms&tbm=isch'

        header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"}
        down_counter = 0
        succounter = 0
        try:
            driver.get(url)
            i = 0
            while i < 6:
                i += 1
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(0.5)

            for x in driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
                down_counter = down_counter + 1
                print("Total Count:", down_counter)
                print("Succsessful Count:", succounter)
                print("URL:", json.loads(x.get_attribute('innerHTML'))["ou"])

                img = json.loads(x.get_attribute('innerHTML'))["ou"]
                imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
                try:
                    context = ssl._create_unverified_context()
                    req = urllib.request.Request(img, headers=header)
                    raw_img = urllib.request.urlopen(req, context=context).read()
                    if not os.path.isdir("../original_test_image/" + keyword + "/"):
                        os.mkdir("../original_test_image/" + keyword + "/")
                    file = open(os.path.join("../original_test_image/" + keyword, keyword + "_" + str(down_counter) +
                                             "." + imgtype), "wb")
                    file.write(raw_img)
                    file.close()
                    succounter = succounter + 1
                except :
                    print("can't get img")
        except urllib.request.HTTPError:
            print('error')
        print('다운받은 이미지 개수 : ' + str(succounter))


if __name__ == '__main__':
    download_image()
