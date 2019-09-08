from selenium import webdriver
import csv
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
import re

chrome_path = "D:/Web Scraping tests/chromedriver"
driver = webdriver.Chrome(chrome_path)

url = "https://community.breastcancer.org/forum/83/topics/871428"
driver.get(url)

j = 0
k = 0

with open('data.csv', 'w', encoding="utf-8") as f:
    f.write("id,posted_time,joined_date,no_of_posts,name,comment\n")

    while True:
        driver.implicitly_wait(10);
        posted_time_moderator = driver.find_element_by_class_name('clearfix')
        joined_date = driver.find_elements_by_class_name('joined_date')
        no_of_posts = driver.find_elements_by_class_name('post_count')
        posted_time_member = driver.find_elements_by_class_name('post-time')
        names = driver.find_elements_by_xpath('//div[@class="user-info"]/a')
        comments = driver.find_elements_by_class_name('user-post')
        driver.execute_script("[...document.querySelectorAll('.reply')].map(el => el.parentNode.removeChild(el))")
        driver.execute_script("[...document.querySelectorAll('.signature')].map(el => el.parentNode.removeChild(el))")
        driver.execute_script("[...document.querySelectorAll('.user-entered-part')].map(el => el.parentNode.removeChild(el))")

        i = 0
        for comment in comments:
            comment_text = comment.text

            if i == 0 and j == 0:
                split1 = posted_time_moderator.text.split("on: ")
                print("posted time:")
                a = split1[1]
                print(a)

                split2 = joined_date[i].text.split("Joined: ")
                print("joined_date:")
                b = split2[1]
                print(b)

                split3 = no_of_posts[i].text.split("Posts: ")
                print("no_of_posts:")
                c = split3[1]
                print(c)

                split4 = comment_text.split("wrote:")
                print("name:")
                d = split4[0]
                print(d)
                print("comment:")
                e = split4[1]
                print(e)

                f.write(str(k) + "," + a.replace(',', '') + "," + b + "," + c.replace(' ', '').replace(',','') + "," + d + "," + e.lstrip().replace(',', '').replace('\n', ' ').replace('\r', '') + "\n")

            elif i == 0 and j != 0:
                print("a")

            else:
                split1 = posted_time_member[i - 1].text.split("M ")
                print("posted time:")
                a = split1[0]
                print(a)

                split2 = joined_date[i].text.split("Joined: ")
                print("joined_date:")
                b = split2[1]
                print(b)

                split3 = no_of_posts[i].text.split("Posts: ")
                print("no_of_posts:")
                c = split3[1]
                print(c)

                print("name")
                d = names[i - 1].text
                print(d)

                if ('wrote:' in comment_text):
                    split4 = comment_text.split("wrote:")
                    print("comment:")
                    e = split4[1]
                    print(e)

                else:
                    split4 = comment_text.split("by")
                    print("comment:")
                    e = split4[1]
                    print(e)

                f.write(str(k) + "," + a.replace(',', '') + "," + b + "," + c.replace(' ', '').replace(',','') + "," + d + "," + e.lstrip().replace(',', '').replace('\n', ' ').replace('\r', '') + "\n")
            i = i + 1
            k = k + 1

        j = j + 1

        try:
            next_page = driver.find_element_by_class_name('next_page')
            url = next_page.get_attribute('href')
            driver.get(url)
            print("****************************************************")
        except(InvalidArgumentException, NoSuchElementException):
            break

driver.close()