# ESPNCricInfo BallByBall Data Scraper
This small Python program can be used to scrape **ball by ball data** of a cricket match from **ESPNCricInfo** and save it as csv or json.

### Prerequisites
- Python 3
- BeautifulSoup
- Downloaded ESPNCricInfo webpage containing the ball by ball data of a specific cricket match

### How to Use This Code
- Download the ESPNCricInfo webpage containing the ball by ball data of a specific cricket match.
- Place the folder next to the Python script.
- Edit the script to include and open the respective `html` file.
- In the terminal, run: `python3 ball_by_ball.py`

### Future Work
- Allow command line arguments rather than changing the code everytime for giving path to an html page.
- Scrape data from the webpage without downloading the webpage. (need to check possibility)
- Add functionality to remove HTML tags and garbage text from the commentary.
- (https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)]()
