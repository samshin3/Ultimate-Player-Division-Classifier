import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

def frisbee_scraper(root="https://play.usaultimate.org", url=None, level="", gender=""):
    req = requests.get(url=url)
    soup = BeautifulSoup(req.text, "html.parser")
    list_soup = soup.find_all('table', {"class": "global_table"})

    team_urls = {}

    for pool in list_soup:
        team_links = pool.find_all('a', href=True)
        for link in team_links:
            team = re.sub(r'\s*\(\d+\)$', '', link.text)
            team_urls.update({team: link['href']})

    list_of_df = []
    for team_name in team_urls:
        link = root + team_urls[team_name]
        read = pd.read_html(link)
        team_df = read[0]
        team_df['team_name'] = team_name
        list_of_df.append(team_df)

    del list_of_df[-1]

    df = pd.concat(list_of_df)
    df.reset_index(drop=True)
    df['level'] = level
    df['gender'] = gender
    df['division'] = level + " " + gender

    return df

if __name__ == "__main__":
    events = {
        "level": ["Division 1", "Division 1", "Division 3", "Division 3"],
        "gender": ["Men", "Women", "Men", "Women"],
        "link": ["https://play.usaultimate.org/events/2025-USA-Ultimate-College-Championships/schedule/Men/CollegeMen",
        "https://play.usaultimate.org/events/2025-USA-Ultimate-College-Championships/schedule/Women/CollegeWomen",
        "https://play.usaultimate.org/events/2025-USA-Ultimate-D3-College-Championships/schedule/Men/CollegeMen",
        "https://play.usaultimate.org/events/2025-USA-Ultimate-D3-College-Championships/schedule/Women/CollegeWomen"]
    }
    links =pd.DataFrame(events)
    scraped_data = []
    for index, row in links.iterrows():
        df = frisbee_scraper(url=row['link'], level=row['level'], gender=row['gender'])
        scraped_data.append(df)

    df = pd.concat(scraped_data)
    df.to_csv("2025 Database.csv")
    print("Scraping successful!")