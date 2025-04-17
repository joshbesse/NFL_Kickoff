import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_kickoff_data():
    # initialize DataFrame and years time frame
    df = pd.DataFrame()
    years = range(2014, 2025)

    # scrape NFL.com for year, team, number of kickoffs, number of touchbacks, and number of returns data
    for year in years:
        current_year = [year] * 32
        teams = []
        kickoffs = []
        touchbacks = []
        returns = []
        return_avg = []

        url = f"https://www.nfl.com/stats/team-stats/special-teams/kickoffs/{year}/reg/all"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        table_rows = soup.find_all("tr")

        for row in table_rows[1:]:
            cells = row.find_all("td")
            teams.append(cells[0].text.split()[0])
            kickoffs.append(cells[1].text.split()[0])
            touchbacks.append(cells[3].text.split()[0])
            returns.append(cells[5].text.split()[0])
            return_avg.append(cells[6].text.split()[0])
        current_df = pd.DataFrame({"year": current_year, "team": teams, "kickoffs": kickoffs, "touchbacks": touchbacks, "returns": returns, "return_avg": return_avg})
        df = pd.concat([df, current_df])
    
    return df

def scrape_return_data():
    # initialize DataFrame and years time frame
    df = pd.DataFrame()
    years = range(2014, 2025)

    # scrape NFL.com for year, team, number of returned touchdowns, number of 20+ yard returns, and number of 40+ yard returns
    for year in years:
        current_year = [year] * 32
        teams = []
        return_td = []
        return_20 = []
        return_40 = []

        url = f"https://www.nfl.com/stats/team-stats/special-teams/kickoff-returns/{year}/reg/all"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        table_rows = soup.find_all("tr")

        for row in table_rows[1:]:
            cells = row.find_all("td")
            teams.append(cells[0].text.split()[0])
            return_td.append(cells[4].text.split()[0])
            return_20.append(cells[5].text.split()[0])
            return_40.append(cells[6].text.split()[0])
        current_df = pd.DataFrame({"year": current_year, "team": teams, "return_tds": return_td, "return_20+": return_20, "return_40+": return_40})
        df = pd.concat([df, current_df])
    
    return df

# scrape NFL.com for kickoff data (year, team, number of kickoffs, number of touchbacks, and number of returns data)
kickoff_df = scrape_kickoff_data()

# convert kickoffs, touchbacks, and returns columns to numeric from str for calculations
kickoff_df[["kickoffs", "touchbacks", "returns", "return_avg"]] = kickoff_df[["kickoffs", "touchbacks", "returns", "return_avg"]].apply(pd.to_numeric)

# calculate return rate and touchback rate
kickoff_df["return_rate"] = (kickoff_df["returns"] / kickoff_df["kickoffs"] * 100)
kickoff_df["touchback_rate"] = (kickoff_df["touchbacks"]/ kickoff_df["kickoffs"] * 100)

# calculate average return rate, return yards, and touchback rate per year
average_return_rate = kickoff_df.groupby("year")["return_rate"].mean().round(1).reset_index()
average_return_yards = kickoff_df.groupby("year")["return_avg"].mean().round(1).reset_index()
average_touchback_rate = kickoff_df.groupby("year")["touchback_rate"].mean().round(1).reset_index()

# save average return rate and touchback rate DataFrames
average_return_rate.to_pickle("./data/avg_return_rate.pkl")
print("Saved average return rate df.")
average_return_yards.to_pickle("./data/avg_return_yds.pkl")
print("Saved average return yards df.")
average_touchback_rate.to_pickle("./data/avg_touchback_rate.pkl")
print("Saved average touchback rate df.")

# scrape NFL.com for return data (year, team, number of returned touchdowns, number of 20+ yard returns, and number of 40+ yard returns)
return_df = scrape_return_data()

# convert return_tds, return_20+, and return_40+ to numeric from str for calculations
return_df[["return_tds", "return_20+", "return_40+"]] = return_df[["return_tds", "return_20+", "return_40+"]].apply(pd.to_numeric)

# calculate total returned touchdowns, returns of 20+ yards, and returns of 40+ yards per year
returned_touchdowns = return_df.groupby("year")["return_tds"].sum().reset_index()
returned_20 = return_df.groupby("year")["return_20+"].sum().reset_index()
returned_40 = return_df.groupby("year")["return_40+"].sum().reset_index()

# save returned touchdowns, returned 20+ yards, and returned 40+ yards DataFrames
returned_touchdowns.to_pickle("./data/returned_touchdowns.pkl")
print("Saved returned touchdowns df.")
returned_20.to_pickle("./data/returned_20.pkl")
print("Saved returned 20+ yards df.")
returned_40.to_pickle("./data/returned_40.pkl")
print("Saved returned 40+ yards df.")