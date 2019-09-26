from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scraper():
    browser = init_browser()
    rests = []
    rest_dict = {}
    #Urls
    url1="https://www.findmeglutenfree.com/search?lat=35.1982836&lng=-111.65130199999999&q=&a=flagstaff%2C+az&local=t"
    
   # url2= "https://twitter.com/marswxreport?lang=en"
    
    
    #Mars NASA
    
    
    browser.visit(url1)
    html1 = browser.html
    soup = BeautifulSoup(html1, 'html.parser')
    results = soup.find_all('li', class_='mt-4')
    links=[]
    for result in results:
        try: 
            Name = result.find('a', class_='align-middle').text
            Address = result.find('span' , class_='sl-addr mt-2').text
            link = "https://www.findmeglutenfree.com" + result.a['href']
            links.append(link)
        
        #for link in links:
            
            response_ = requests.get(link)
            soup_ = BeautifulSoup(response_.text, 'lxml')
            phone = soup_.find('div', class_='mt-3 font-weight-bold').text
            web = soup_.find('div', class_='mt-3 mr-3').text
            

            #to print results (terminal)
            #print('-------------')
            #print(Name)
            #print(Address)
            #print(link)
            #print(phone)
            #print(web)
            rests.append(results)           
        

        # Dictionary to be inserted as a MongoDB document
            post = {
                            'Name': Name,
                            'Address': Address, 
                            'url': link,
                            'phone number': phone,
                            'website': web
                
                            }

            
        except Exception as e:
            print(e)      
    
    #df = pd.DataFrame.from_dict(rest_dict)
    #myhtml=df.to_html()     

    rest_dict["Name"] = Name
    rest_dict["Address"] = Address
    rest_dict["URL"]= link
    rest_dict["phone number"]=phone  
    rest_dict["website"]= web
    return rest_dict