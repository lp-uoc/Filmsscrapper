# PRueba
# Import the package re
import re

def get_url(page):
    # Build the url to get
    
    # Get url next page
    data = str(page.find_all('a', class_="lister-page-next next-page")[0])

    # Get and Build the new url
    url = "https://www.imdb.com/" + str(re.search(r'"\/(.|\n)*"', data)[0].replace('"',''))    
    
    return url
    
    

def get_title(soup, number):

    # Get the title from the text and with the number of element
    # text: soup with the list of divs with movie information
    # number: nº of element to check

    try:
        return soup[number].find('h3', class_='lister-item-header').a.string
    
    except:
        return 'N/A'
                      

def get_duration(soup, number):

    # Get the duration from the text and with the number of element
    # text: soup with the list of divs with movie information
    # number: nº of element to check
    
    try:
        return soup[number].find('span', class_='runtime').string

    except:
        return "N/A"


def get_genre(soup, number):

    # Get the genre from the text and with the number of element
    # text: soup with the list of divs with movie information
    # number: nº of element to check
    
    try:
        return soup[number].find('span', class_='genre').string.replace("\n", "")

    except:
        return "N/A"
    
    
def get_year(soup, number):
    
    # Get the year from the text and with the number of element
    # text: soup with the list of divs with movie information
    # number: nº of element to check
    
    try:
        return soup[number].find('span', class_='lister-item-year text-muted unbold').get_text()
    
    except:
        return "N/A"
    
def get_rating(soup, number):
    
    # Get the rating from the text and with the number of element
    # text: soup with the list of divs with movie information
    # number: nº of element to check
    
    try:
        return soup[number].find('div', class_='inline-block ratings-imdb-rating').get_text().replace("\n", "")
    
    except:
        return"N/A"
    

def get_gross(soup, number):

    # Get the gross from the text and with the number of element
    # text: soup with the list of divs with movie information
    # number: nº of element to check

    try:
        # Get all data from the div
        values = soup[number].find("p", {"class": "sort-num_votes-visible"})

        #Extract with regex
        gross = re.search(r'Gross.*\n.* name=' ,str(values))[0]

        # Save the value
        if gross != None:
            return re.search(r'\"([0-9]|,){2,}\"' ,str(gross))[0]
        else:
            return 'N/A'

    except:
        return"N/A"

    
def get_votes(soup, number):
    
    # Get the votes from the text and with the number of element
    # text: soup with the list of divs with movie information
    # number: nº of element to check
    
    try:
        # Get all data from the div
        values = soup[number].find("p", {"class": "sort-num_votes-visible"})
        
        #Extract with regex
        votes = re.search(r'Votes.*\n.* name=' ,str(values))[0]
        
        # Save the value
        if votes != None:
            return votes[0]
        else:
            return 'N/A'
        
    except:
        return"N/A"

def get_directors(soup, number):
    
    # Get the director o directors from the text and with the number of element
    # text: soup with the list of divs with movie information
    # number: nº of element to check
    
    try:
        # Get all data from the div
        values = soup[number].find_all('p', class_="")
        
        #Extract with regex
        directors = re.search(r'Director((.|\n)*)\>\|\<',str(values))[0]
        
        # Save the value
        if directors != None:
            return re.findall(r'\>.*\<',directors)
        else:
            return 'N/A'
        
    except:
        return"N/A"
    
def get_actors(soup, number):
    
    # Get the actors from the text and with the number of element
    # text: soup with the list of divs with movie information
    # number: nº of element to check
    
    try:
        # Get all data from the div
        values = soup[number].find_all('p', class_="")
        
        #Extract with regex
        actors = re.search(r'Star((.|\n)*)\<\/p\>\]',str(values))[0]
        
        # Save the value
        if actors != None:
            return re.findall(r'\>.*\<',actors)
        else:
            return 'N/A'
        
    except:
        return"N/A"
