from bs4 import BeautifulSoup
import requests
import os
os.chdir("/Users/parthkabade/Documents/Internships/Python_dev_intern/PyDev_Task_3/")

# 1. Fetch the target website content
url = "https://thehackernews.com/"
response = requests.get(url)


# 2. Initialize the parser and create a soup object
soup = BeautifulSoup(response.content, 'html.parser')

# 3. Target and extract data (Example: Get the first H1 heading text)
first_heading = soup.find_all('h2')


with open("myfile.txt", "w", encoding="utf-8") as file:
    for headline in first_heading:
        file.write(headline.text.strip()+"\n")
