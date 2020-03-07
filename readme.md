# Historical Weather Data Web Scraper

This is a web scraper written in Python that scrapes historical weather data from [Time and Date website]("https://timeanddate.com")
It gets data for every state in Nigeria for every available month from 2011 till December 2019 and stores it in a CSV file.
I have also taken the liberty to clean the data so you do not have to, you can work with CSV file as is.
The exact data gotten is:

- average temperature
- average humidity
- average pressure

## How to use:

### Using with PyCharm

Assuming you have Python and PyCharm already install, do the follow:
In the terminal run:

- pip install pandas
- pip install numpy
- pip install requests
- pip install beautifulsoup4

### Using with VSCode

- [Download Python]("https://www.python.org/downloads/")
- [Download Python VS Code Extension]("https://marketplace.visualstudio.com/items?itemName=ms-python.python")
- [Download Anaconda for VS Code]("https://marketplace.visualstudio.com/items?itemName=ms-python.anaconda-extension-pack")
- open the folder in VS Code
- In the terminal run:

1. pip install pandas
2. pip install numpy
3. pip install requests
4. pip install beautifulsoup4

- Press the play button at the top right corner

## I don't need all those states

Navigate to the states checklist.txt file, there, is the list of all states with their special IDs.
Go into url.py and simply remove all the urls in the list that match the ID

**Please note: Endeavour to read all the comments in the code**
