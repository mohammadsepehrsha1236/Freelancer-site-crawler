from bs4 import BeautifulSoup
import requests
import re
from time import sleep

res = requests.get("https://www.freelancer.com/jobs/")
res1 = requests.get("https://www.freelancer.com/jobs/2/")
res2 = requests.get("https://www.freelancer.com/jobs/3/")
res3 = requests.get("https://www.freelancer.com/jobs/4/")
# ************************************************** #
soup = BeautifulSoup(res.content,"html.parser")
soup1 = BeautifulSoup(res1.content,"html.parser")
soup2 = BeautifulSoup(res2.content,"html.parser")
soup3 = BeautifulSoup(res3.content,"html.parser")
# ************************************************** #
we = soup.find_all("a",attrs={"class":"JobSearchCard-primary-heading-link"})
we1 = soup1.find_all("a",attrs={"class":"JobSearchCard-primary-heading-link"})
we2 = soup2.find_all("a",attrs={"class":"JobSearchCard-primary-heading-link"})
we3 = soup3.find_all("a",attrs={"class":"JobSearchCard-primary-heading-link"})
# ************************************************** #
wa = soup.find_all("div",attrs={"class":"JobSearchCard-primary-price"})
wa1 = soup1.find_all("div",attrs={"class":"JobSearchCard-primary-price"})
wa2 = soup2.find_all("div",attrs={"class":"JobSearchCard-primary-price"})
wa3 = soup3.find_all("div",attrs={"class":"JobSearchCard-primary-price"})
# **************we_list************** #
we_list = []
we_list2 = []
# **************wa_list************** #
wa_list = []
wa_list2 = []
# **************1************** #
for i in we:
    job = i.url
    we_list.append(job)
for e in wa:
    price = e.text
    wa_list.append(price.strip())
# **************2************** #
for i1 in we1:
    job1 = i1.text
    we_list.append(job1.strip())
for e1 in wa1:
    price1 = e1.text
    wa_list.append(price1.strip())
# **************3************** #
for i2 in we2:
    job2 = i2.text
    we_list.append(job2.strip())
for e2 in wa2:
    price2 = e2.text
    wa_list.append(price2.strip())
# **************3************** #
for i3 in we3:
    job3 = i3.text
    we_list2.append(job3.strip())
for e3 in wa3:
    price3 = e3.text
    wa_list2.append(price3.strip())
# **************1************** #
# list1 = []
# cco = 0
# while len(we_list) != cco:
#     list1.append([we_list[cco],wa_list[cco]])
#     cco+=1
# # **************2************** #
# list2 = []
# co = 0
# while len(we_list2) != co:
#     list2.append([we_list2[co],wa_list2[co]])
#     co+=1

# print(list1)
print(we_list)
# print("*********************************************************")
# print(list2)
# sleep(30)