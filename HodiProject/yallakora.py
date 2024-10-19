import requests 
from bs4 import BeautifulSoup
import csv

date = input("please enter a date in the following format mm/dd/yyyy: ")
page = requests.get(f"https://www.yallakora.com/match-center/مركز-المباريات?date={date}#")

def main(page):

    src = page.content
    soup = BeautifulSoup(src, "lxml")
    matches_details = []

    championships = soup.find_all("div", {'class': 'matchCard'})
    # print(championships)

    def get_match_info(championships):

        championship_title = championships.contents[1].find("h2").text.strip()
        # print(championship_title)
        
        all_matches = championships.contents[3].find_all("div", {'class': 'item finish liItem'})
        number_of_matches = len(all_matches)
        # print(number_of_matches)
        # print(all_matches)

        for i in range(number_of_matches):
            # get teams names
            team_A = all_matches[i].find("div", {'class': 'teamA'}).text.strip()
            team_B = all_matches[i].find("div", {'class': 'teamB'}).text.strip()

            # get match score
            match_result =  all_matches[i].find("div", {'class': 'MResult'}).find_all("span", {'class': 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"

            # get mutch time
            match_time =  all_matches[i].find("div", {'class': 'MResult'}).find("span", {'class': 'time'}).text.strip()

            # add match info to match_details
            matches_details.append({"نوع البطولة" : championship_title,
                                     "الفريق الأول" : team_A,
                                       "الفريق الثاني" : team_B,
                                        "ميعاد المبارة" : match_time,
                                         "النتيجة" : score})
            
    for i in range(len(championships)):
     get_match_info(championships[i]) #championships[0] = تصفيات امم افريقيا ، championships[1] = بطولة افريقيا كرة اليد 
     
    keys = matches_details[0].keys()
    with open('/Users/hadialshaqi/Desktop/matches-details.csv', 'w') as outpur_file:
       dict_writer = csv.DictWriter(outpur_file, keys)
       dict_writer.writeheader()
       dict_writer.writerows(matches_details)
       print("file created")

main(page)