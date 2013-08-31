''' 
Goals:
Provide easy interface to ANB search API (a. user-entered parameters; b. auto generate from authors list in SQL)
Automate parsing of search results and downloading of relavent biographies
Analyze biographies in NER and visualize links (see degrees of francis bacon project?)
(???)

Components:
[]input taker (user input prompt) > parameters: 
[]autoinput taker (sql/csv)
[]webpage grabber (search page)
[]biographical link collector (allow manual user parsing of authors? resolve name sharers)
[]webpage grabber (biographies)
[]text cleaner
'''

import requests
from bs4 import BeautifulSoup


#ANB Specific
def ANBseek(parameters):
    '''
    search api translator for Oxford ANB with ND proxy info.
    available search parameters: fulltext, name, gender, Y birth Start, Y birth End, birth state, birth country
    '''
    if type(parameters) != dict:
        return 0
    else:
        if parameters["birthstate"] != "":
            parameters["birthplace"] = parameters["birthstate"]
        elif parameters["birthcountry"] != "":
            parameters["birthplace"] = parameters["birthcountry"]
        else:
            parameters["birthplace"] = ""
        if parameters["StartYear"] != "":
            parameters["startday"] = "1"
            parameters["startmonth"] = "1"
        else: 
            parameters["startday"] = ""
            parameters["startmonth"] = ""
        if parameters["EndYear"] != "":
            parameters["endday"] = "31"
            parameters["endmonth"] = "12"
        else:
            parameters["endday"] = ""
            parameters["endmonth"] = ""
        url = "http://www.anb.org.proxy.library.nd.edu/articles/bin/search.cgi?func=advanced_search&fulltext={0}&idxa=-at&idxb=-bib&field-Name={1}&field-gender={2}&realms_top=Writing+and+Publishing&field-Realm=Writing+and+Publishing&date-m-birthS={3}&date-d-birthS={4}&date-y-birthS={5}&date-m-birthE={6}&date-d-birthE={7}&date-y-birthE={8}&date-m-deathS=&date-d-deathS=&date-y-deathS=&date-m-deathE=&date-d-deathE=&date-y-deathE=&field-BirthPlace={9}&bp_state={10}&bp_country={11}&field-Contrib=&meta-dc=500".format("+".join(parameters["fulltext"].split()), "+".join(parameters["name"].split()), parameters["gender"], parameters["startmonth"], parameters["startday"], parameters["StartYear"], parameters["endmonth"], parameters["endday"], parameters["EndYear"], "+".join(parameters["birthplace"].split()), "+".join(parameters["birthstate"].split()), "+".join(parameters["birthcountry"].split())) 
        #download search page and read its contents.  
        #using Requests module since Oxford requires cookies to be accepted         
        page = requests.get(url)
        searchtext = page.text
        yummyloc = searchtext.find("Search Results List") + 27
        nomoreyummy = searchtext.find("<!--back to the top-->")
        washedtext = searchtext[yummyloc:nomoreyummy]
        #TODO: count the number of results to determine whether there's more than one page of data
        soup = BeautifulSoup(washedtext)



        goodstuff = soup.ol.find_all("a")
        link_list = []        
        for href in goodstuff:
            link_list.append(href['href'])
        count = 0 #trying to be cheap and write over link_list variable onto itself
        for x in link_list:
            if x.find("?") != -1:
                stoppoint = x.find("?")-5
            else:
                stoppoint = len(x)-5
            link_list[count] = "http://www.anb.org.proxy.library.nd.edu/articles/"+x[3:stoppoint]+"-print.html"
            count += 1
        return link_list
        
def ANBreap(victim):
    writefile = ""
    soupfile = requests.get(victim).text
    yummyloc = soupfile.find("</TD>")+11
    nomoreyummy = soupfile.find("<HR>")-15
    soupfile = soupfile[yummyloc:nomoreyummy]
    soup = BeautifulSoup(soupfile)
    soupfile = soup.find_all("p")
    for x in soupfile:
        writefile += str(x)+"\n"
    return writefile

def ANBredeemer(soul):
    soup = BeautifulSoup(soul.replace("\n", " "))
    repeat = len(soup.find_all("p"))
    count = 0
    while (count < repeat):
        soup.p.append("\n")
        soup.p.unwrap()
        count += 1
    return soup.get_text()
#End ANB Specific
    
def seeker(site):
    '''collects search results from specified site and returns a list of links, then prints basic overview info to screen
    '''
    #test
    parameters = {"name":"", "StartYear":"1790", "EndYear":"1900", "gender":"m", "birthstate":"Alabama", "birthcountry":"", "fulltext":""}
    #this leaves room for other sites to be added later
    if site == "ANB":
        return ANBseek(parameters)
    #not a problem now since user's being prompted to enter parameters, but might come in handy when we automate input to check for correct type of input
    else: 
        print "input must be in the form of a dictionary"
        return 0

def reaper(victims, site):
    if site == "ANB":
        return ANBreap(victims)
        
def baptist(goat, site):
    if site == "ANB":
        return ANBredeemer(goat)
    
#--------------------------execute--------------------------        
if __name__ == "__main__":
    bookoflife = seeker("ANB") 
    if bookoflife == 0:
        print "exited with error"
    else:  #if the program has made it this far, the data should have been massaged into an appropriate format already, so no longer checking for errors (famous last words?)
        repeat = len(bookoflife)  
        count = 0
        while (count < repeat):
            gold = baptist(reaper(bookoflife[count], "ANB"), "ANB") #got lazy
            f = open("bio{0}.txt".format(str(count + 1)), 'w')
            f.write(gold)
            count += 1
            
