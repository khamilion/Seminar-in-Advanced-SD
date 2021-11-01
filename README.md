# Seminar-in-Advanced-SD
Packages: 

        bs4 (Beautiful Soup), SQL Lite, SQl Studio, requests
        
      - import requests for HTTP requets
      - Web scrape with Beautiful soup package, 
      - Save the data to the 'olympics' table within the SQLite database
      
The main.py module webscrapes olympicdatabase.com and saves the information in a nested dictionary.

main.py:
    
    Methods:
    
         -  main(): 
              Entry point of the program. Start here. All other functions are called from main().

         -  get_data(url):
              Uses the url paramater to make a request to the website with requets package
              
              returns: returns the text off of the page from the url
              
         - get_olympic_year(tables):
               (table) paramater is a list holding the web scraped information from the table on the website using bs4.
               
               This method loops through the the (table) list to find the text stating the name of the olympic event, such as "Tokyo 2020" (using Beautiful soup).
               
               returns: two variables holding the name of the olympic event and the name of the next olympic event.
               
          - get_countries(tables):
               (table) paramater is a list holding the scraped information from the table on the website using bs4.
               
               This method uses beautiful soup to parse the (table) parameter for the 10 specific countries participating in the olympics and their medals. 
               It holds this information in a dictionary.
               
          - look_through_rows(tables, name):
              (table) paramater is a list holding the scraped information from the table on the website using bs4.
              
              (name) paramater holds the name of the specified country 
              
              This method is called from within get_countries() as an assistant method. It loops through the tables parameter to find the medal
              count for the (name) parameter holding the country name.
              
The olympic_db file saves the dictionary holding the olympic data in a databse with SQLite.


olympic_db:
    
    - Imports the main.py module.
    
    - Uses for loops to loop through the nested dictionary and query the data.
    
    
   <img width="934" alt="Screen Shot 2021-10-31 at 2 05 20 PM" src="https://user-images.githubusercontent.com/70460601/139597884-aa2a9678-677c-4d89-8305-0898e81efea4.png">

   
      
