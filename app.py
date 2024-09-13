import httpx
import json
import pandas as pd

# Set the geographical location to the United States

geo_location = "CA"

# Add the API URLs
topics_url = f"https://trends.google.com/trends/api/widgetdata/relatedsearches?hl=en-US&tz=240&req=%7B%22restriction%22:%7B%22geo%22:%7B%22country%22:%22CA%22%7D,%22time%22:%222024-09-12T18%5C%5C:05%5C%5C:57+2024-09-13T18%5C%5C:05%5C%5C:57%22,%22originalTimeRangeForExploreUrl%22:%22now+1-d%22,%22complexKeywordsRestriction%22:%7B%22keyword%22:%5B%7B%22type%22:%22BROAD%22,%22value%22:%22programming%22%7D%5D%7D%7D,%22keywordType%22:%22ENTITY%22,%22metric%22:%5B%22TOP%22,%22RISING%22%5D,%22trendinessSettings%22:%7B%22compareTime%22:%222024-09-11T18%5C%5C:05%5C%5C:57+2024-09-12T18%5C%5C:05%5C%5C:57%22%7D,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22CM%22,%22category%22:0%7D,%22language%22:%22en%22,%22userCountryCode%22:%22CA%22,%22userConfig%22:%7B%22userType%22:%22USER_TYPE_LEGIT_USER%22%7D%7D&token=APP6_UEAAAAAZuXQhcOGUPuW6AsOipJBkyUfkQjfuYgk"

queries_url = f"https://trends.google.com/trends/api/widgetdata/relatedsearches?hl=en-US&tz=240&req=%7B%22restriction%22:%7B%22geo%22:%7B%22country%22:%22CA%22%7D,%22time%22:%222024-09-12T18%5C%5C:05%5C%5C:57+2024-09-13T18%5C%5C:05%5C%5C:57%22,%22originalTimeRangeForExploreUrl%22:%22now+1-d%22,%22complexKeywordsRestriction%22:%7B%22keyword%22:%5B%7B%22type%22:%22BROAD%22,%22value%22:%22programming%22%7D%5D%7D%7D,%22keywordType%22:%22QUERY%22,%22metric%22:%5B%22TOP%22,%22RISING%22%5D,%22trendinessSettings%22:%7B%22compareTime%22:%222024-09-11T18%5C%5C:05%5C%5C:57+2024-09-12T18%5C%5C:05%5C%5C:57%22%7D,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22CM%22,%22category%22:0%7D,%22language%22:%22en%22,%22userCountryCode%22:%22CA%22,%22userConfig%22:%7B%22userType%22:%22USER_TYPE_LEGIT_USER%22%7D%7D&token=APP6_UEAAAAAZuXQhdFr9kwhcYtatVcsQ2f0ELPYNdUo"

# Get the data from the API URLs
topics_response = httpx.get(url=topics_url)
queries_response = httpx.get(url=queries_url)

# Remove the extra symbols and add the data into JSON objects
topics_data = json.loads(topics_response.text.replace(")]}',", ""))
queries_data = json.loads(queries_response.text.replace(")]}',", ""))

result = []

# Prase the topics data and the data into the result list
for topic in topics_data["default"]["rankedList"][1]["rankedKeyword"]:
    topic_object = {
        "Title": topic["topic"]["title"],
        "Search Volume": topic["value"],
        "Link": "https://trends.google.com/" + topic["link"],
        "Geo Location": geo_location,
        "Type": "search_topic",
    }
    result.append(topic_object)

# Prase the querires data and the data into the result list
for query in queries_data["default"]["rankedList"][1]["rankedKeyword"]:
    query_object = {
        "Title": query["query"],
        "Search Volume": query["value"],
        "Link": "https://trends.google.com/" + query["link"],
        "Geo Location": geo_location,
        "Type": "search_query",
    }
    result.append(query_object)

print(result)

# Create a Pandas dataframe and save the data into CSV
df = pd.DataFrame(result)
df.to_csv("keywords.csv", index=False)