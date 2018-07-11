# import required packages
import urllib.request as urllib2
import pandas as pd
from bs4 import BeautifulSoup

def main():
    # opening html file with BeautifulSoup
    with open('2018-03-21/2018-03-21-PSL-Innings2.html') as fp:
        innings_soup = BeautifulSoup(fp, "html5lib")
    
    # create an empty dataframe
    ball_df = pd.DataFrame(columns=['ball', 'score', 'commentary'])

    # create empty lists for each of the data you want
    ball_numbers = list()
    ball_score = list()
    ball_desc = list()

    # get data from div classes
    # for ball numbers
    for div in innings_soup.findAll('div', {'class': 'time-stamp'}):
        # ball_data[div.find('div').attrs['class'][0]] = div.text.strip()
        ball_numbers.append(div.text)

    # for score on each ball
    for div in innings_soup.findAll('div', {'class': 'over-circle'}):
        ball_score.append(div.text)

    # for description of each ball
    for div in innings_soup.findAll('div', {'class': 'description'}):
        ball_desc.append(div.text)
    
    # save lists in respective dataframe columns
    ball_df.ball = ball_numbers
    ball_df.score = ball_score
    ball_df.commentary = ball_desc
    
    # save dataframe as csv or json
    ball_df.to_csv("2018-03-21-innings2.csv", sep=',', index=False)
    ball_df.to_json("2018-03-21-innings2.json", orient='records')

if __name__ == '__main__':
    main()
