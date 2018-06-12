# import required packages
import urllib.request as urllib2
from bs4 import BeautifulSoup

# opening html file with BeautifulSoup
with open('2018-03-21/2018-03-21-PSL-Innings2.html') as fp:
    soup = BeautifulSoup(fp, "html5lib")

# declare empty lists for each of the data you want
ball_numbers = list()
ball_score = list()
ball_desc = list()

# get data from div classes
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

# print(tuples)

# write the tuples to a file
with open( "2018-03-21-innings2", 'w' ) as test_file:
    print(tuples, file = test_file)

# if __name__ == '__main__':
#     main()
