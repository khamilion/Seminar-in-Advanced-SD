# This module used for web scraping the Olympic Database website for a variety statistics


from bs4 import BeautifulSoup
import requests


# This function makes a request to the server
def get_data(url):
    return requests.get(url).text


# list of 10 countries
country_list = ["USA", "CHN", "FRA", "JPN", "GBR", "AUS", "BRA", "GER", "ITA", "CAN"]


# dict holds all of the olympic events, countries, and medals
olympic_data = {}


# Get the list of countries
def get_countries(tables):
    # dictionary to hold countries and their medal counts
    medal_cnt = {}

    # loop through each country in the list
    for i in range(len(country_list)):
        name = country_list[i]

        medal_cnt.update(look_through_rows(tables, name))
    '''
    for c, m in medal_cnt.items():
        print(f"{c} : {m}\n")
    '''
    return medal_cnt


# Search the rows of the tables to find the needed data column
def look_through_rows(tables, name):
    participated = False  # determines whether the country participated in the olympics

    medal_count = {}  # dict holds the country as a key and medals as the value

    # loop through each table
    for data in tables:
        # get all of the rows from each table
        rows = data.find_all('tr')

        # loop through row and get each row matching the find_all
        for r in rows:
            td = r.find_all('td', height='25', width='12%')  # finds the td with the country names

            # if the table data does not have the matching attributes, skip the loop iteration
            if not td:
                continue
            else:
                # loop through resulting table data list to find the country name needed
                for country in td:
                    if country.text == name:
                        participated = True  # the country did participate in the olympics
                        medals = r.find_all('td', height='25',
                                            width='15%')  # find the medal counts in the corresponding row

                        medal_list = []  # list to hold the medals

                        # save the medals in the list
                        for m in medals:
                            medal_list.append(m.text)

                        # find the row with the countries position (1st, 2nd, 3rd)
                        p = r.find('td', height='35', align='left', width='8%')
                        # print(f"{country.text} rank: {pos.text}")

                        # the period and whitespace needs to be removed from the position
                        try:
                            # find the index of '.'
                            index = p.text.index('.')

                            # use slice notation to remove the '.'
                            pos = p.text[:index] + p.text[:len(p)-1]
                        except ValueError as ex:
                            print("No period in position")
                            print(ex)

                        # add the country and its medals to the dictionary
                        medal_count[country.text] = {"position": pos,
                                                     "gold": medal_list[0],
                                                     "silver": medal_list[1],
                                                     "bronze": medal_list[2],
                                                     "total": medal_list[3]}

                        return medal_count
    # if the country did not participate in the olympics
    if not participated:
        medal_count[name] = {"position": "NULL",
                             "gold": "NULL",
                             "silver": "NULL",
                             "bronze": "NULL",
                             "total": "NULL"}
        return medal_count


# get the specific olympic year
def get_olympic_year(tables):

    # get all of the rows from each table
    for d in tables:
        rows = d.find_all('tr')

        # loop through row and get each row matching the find_all
        for r in rows:
            td = r.find_all('td', height='30', align='right', colspan='8')  # find the row containing the olympic year

            # if the td is not found, skip this iteration
            if not td:
                continue
            else:
                # loop through resulting table data list to find name of the olympics
                for name in td:
                    current_olympics = name.text[2:-2]

                    # get the next olympics
                    next_olympics = name.a.next_sibling.next_sibling.next_sibling["href"]

                    return [current_olympics, next_olympics]


# entry point of the program
def main():

    # total number of olympics to collect information about
    num_of_olympics = 10  # TODO change back to 10 olympics
    i = 1

    # url for the medal list
    url = 'https://www.olympiandatabase.com/'
    next_olympics = 'index.php?id=20019&L=1'

    while i <= num_of_olympics:
        # Get the data from the server
        soup = BeautifulSoup(get_data(url + next_olympics), 'lxml')

        # Find the data needed for parsing
        main_c = soup.find('div', class_='main_container')
        tables = main_c.find_all('table', class_='frame_space')
        
        # get the current olympics and the next olympics
        current_olympics, next_olympics = get_olympic_year(tables)

        # gets all the olympic data
        olympic_data[current_olympics] = get_countries(tables)

        i += 1

    #for o, d in olympic_data.items():
        #print(f"\n{o}\n  {d}")


# __name__ takes a different value depend on how the file is executed.
# _name__==__main__ when file is executed from the command line or from python interpreter and not imported
# Alternatively, __name__ is equal to the name of the module if it's being imported
if __name__ == "__main__":
    main()
