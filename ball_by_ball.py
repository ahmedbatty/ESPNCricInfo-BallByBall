# importing required packages
import urllib.request as urllib2
from bs4 import BeautifulSoup

# match innings link
# html_doc = "http://www.espncricinfo.com/series/8679/commentary/1128849/peshawar-zalmi-vs-quetta-gladiators-eliminator-1-psl-2017-18?innings=1"
# page = urllib2.urlopen(html_doc).read()

# soup = BeautifulSoup(page, 'html.parser')
# soup = BeautifulSoup('2018-03-20/Eliminator 1 (N), Pakistan Super League at Lahore, Mar 20 2018 | Match Commentary | ESPNCricinfo.html', 'html.parser')
# print(soup.prettify())

# opening html file with BeautifulSoup
# with open('2018-03-20/Eliminator 1 (N), Pakistan Super League at Lahore, Mar 20 2018 | Match Commentary | ESPNCricinfo.html') as fp:
#     soup = BeautifulSoup(fp, "html5lib")

with open('2018-03-21/2018-03-21-PSL-Innings2.html') as fp:
    soup = BeautifulSoup(fp, "html5lib")

# all_divs = soup.find_all("div", class_="commentary-item")
# print(len(all_divs))

# all_divs = soup.findAll('div', {'class': 'time-stamp'})
# print(all_divs.text)

ball_numbers = list()
ball_score = list()
ball_desc = list()

# for ball numbers
for div in soup.findAll('div', {'class': 'time-stamp'}):
    # ball_data[div.find('div').attrs['class'][0]] = div.text.strip()
    ball_numbers.append(div.text)
    # print(div.text)

# for score on each ball
for div in soup.findAll('div', {'class': 'over-circle'}):
    ball_score.append(div.text)
    # print(div.text)

# for description of each ball
for div in soup.findAll('div', {'class': 'description'}):
    ball_desc.append(div.text)
    # print(div.text)

# get each ball data in one row
tuples = list(zip(ball_numbers, ball_score, ball_desc))

print(tuples)

with open( "2018-03-21-innings2", 'w' ) as test_file:
    print(tuples, file = test_file)

# if __name__ == '__main__':
#     main()
