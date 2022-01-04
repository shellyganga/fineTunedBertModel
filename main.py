import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
# format: "https://fangj.github.io/friends/season/0101.html"
df = pd.DataFrame(columns = ["speaker", "text"])
friend_list = ["Ross", "Monica", "Joey", "Rachel", "Chandler", "Phoebe"]

for x in range(1, 9):
    for i in range(1, 22):
        URL = ""
        if(len(str(i)) >= 2):
            URL = "https://fangj.github.io/friends/season/0"+str(x) + str(i) +".html"
        else:
            URL = "https://fangj.github.io/friends/season/0" +str(x)+ "0"+str(i) + ".html"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'lxml')
        rows = soup.find_all('p')
        for row in rows:
            text_data = row.text.split()
            if(len(text_data)==0):
                continue
            name = "".join(re.split("[^a-zA-Z]*", text_data[0]))
            text = ""
            for t in text_data[1:]:
                    text = text +t+ " "
            new_text = re.sub(r'\([^)]*\)', '', text)
            if(name in friend_list and ("(" and ")" and "[" and "]" not in new_text)):
                df = df.append({"speaker": name, "text": new_text}, ignore_index=True)
df.to_csv('/Users/shellyschwartz/Downloads/friends_lines.csv')

