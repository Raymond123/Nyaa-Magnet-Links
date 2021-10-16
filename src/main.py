from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import httplib2
from bs4 import BeautifulSoup, SoupStrainer

with open("../bin/titles.md") as fp:
    for title in fp:
        urlTitle = title.replace(" ", "+");
        # print(urlTitle);
        searchUrlTest = "https://nyaa.si/?f=0&c=0_0&q=subsplease+1080+" + urlTitle;
        try:
            searchPage = requests.get(searchUrlTest)
            searchSoup = BeautifulSoup(searchPage.content, 'html.parser')
            search = searchSoup.find_all('i', class_="fa-magnet")

            wf = open("../bin/d-links.md", "w")
            wf.write(title + ":\n")
            for searchResults in search:
                # print(searchResults)
                # print(searchResults.parent['href'])
                wf.write(searchResults.parent['href'] + "\n")
            wf.write("\n")
            wf.close();

        except Exception as ex:
            print("Error: " + format(ex))
            pass
