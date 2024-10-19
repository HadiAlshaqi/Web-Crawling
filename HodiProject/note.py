import requests 
from bs4 import BeautifulSoup
import csv
import pandas as pd
import openpyxl
import os


date = input("please enter a number of page in the following format N: ")
page = requests.get(f"https://muqawil.org/en/contractors?page={date}#")

def main(page):

    print("Processing ... take some time!")

    src = page.content
    soup = BeautifulSoup(src, "lxml")
    companies_details = []

    # companies = soup.find_all("div", {'class': 'section-card has-action has-membership platinum-membership'})
    companies = soup.find_all("div", {'class': 'has-membership'})
    # print(len(companies))
    # print(companies[19])
 
    # print(companies)

    def get_match_info(companies):

        # get company url
        company_url = companies.contents[1].find("a")["href"]
        # print(company_url)

        company_page = requests.get(f"{company_url}")
        src_page = company_page.content
        soup_page = BeautifulSoup(src_page, "lxml")
        company_section = soup_page.find_all("div", {'class': 'section-card'})
        # print(len(company_section))

        # get company name
        company_name = company_section[0].contents[1].find("h3").text.strip()
        # print(company_name)

        # all sections
        sections_card = company_section[0].contents[1].find("div", {'class': 'row'})

        # get company membership number
        company_membership_number = sections_card.contents[1].find("div", {'class': 'info-value'}).text.strip()
        # print(company_membership_number)

        # get company phone 
        company_phone = sections_card.contents[11].find("div", {'class': 'info-value'}).text.strip()
        # print(company_phone)

        # get company email
        company_email = sections_card.contents[13].find("div", {'class': 'info-value'})
        company_email_encode = company_email.find("span")["data-cfemail"]
        # print(company_email_encode)
        def decode_cf_email(encoded_email):
            email = ""
            key = int(encoded_email[:2], 16)
            encoded_part = encoded_email[2:]

            for i in range(0, len(encoded_part), 2):
                char_code = int(encoded_part[i:i+2], 16) ^ key
                email += chr(char_code)

            return email
        company_email_decode = decode_cf_email(company_email_encode)

        # get company city
        company_city = sections_card.contents[15].find("div", {'class': 'info-value'}).text.strip()
        # print(company_city)

        # get company activities
        company_activities = company_section[len(company_section) - 2].contents[3].find_all("li", {'class': 'list-item'})
        company_activities_format = company_activities
        number_of_activities = len(company_activities)
        for i in range(number_of_activities):
            company_activities_format[i] = company_activities[i].text.strip()
            # print(company_activities[i].text.strip())

        # add match info to match_details
        companies_details.append({"Name" : company_name,
                                    "Membership" : company_membership_number,
                                        "Phone" : company_phone,
                                            "Email" : company_email_decode,
                                                "City" : company_city,
                                                    "Activities" : company_activities_format
                                                        })

    # for i in range(len(companies) - 1):
    #     get_match_info(companies[i]) #companies[0] = Awared General Contracting Company , companies[1] = Gulf Pioneers Trading Company

    get_match_info(companies[0])
                   
    df = pd.DataFrame(companies_details)
    excel_file_path = "/Users/hadialshaqi/Desktop/test1.xlsx"
    df.to_excel(excel_file_path, index=False)
    print(f"Data successfully saved to {excel_file_path}")

main(page)