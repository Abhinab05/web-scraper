First, I import requests and BeautifulSoup to fetch and parse the webpage.
Then I send a GET request to The Hindu's homepage and convert the HTML into a BeautifulSoup object.
I look for all <h3> tags with the class "title", since that’s where the headlines are.
Then I open a .txt file and write each headline into it using a numbered format.
Finally, I print a success message after saving all the headlines.# web-scraper
