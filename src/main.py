# Import the Extractions the logic
import extractions

# Import the package
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests


# Get number of films
n_films = int(input("Introduce el número de pelícuas a obtener: "))
film_range = range(1,n_films,250)

# Create the lists
titles = []
duration = []
genre = []
year = []
rating = []
gross = []
votes = []
directors = []
actors = []

dur = len(film_range)

# Just initialice the url
url_to_get = "https://www.imdb.com/search/title/?title_type=feature&release_date=,2022-12-31&sort=release_date,desc&count=250&start=0"

# Get the slice of films
for n in film_range:
    
    #Map the html to beautiful soup
    page = BeautifulSoup(requests.get(url_to_get).content,features="html.parser")
    
    # Freeze the code
    time.sleep(4)
    
    # Get data from the file
    soup = page.find_all('div', class_='lister-item mode-advanced')
    
    for e in range(250):
        #Get title
        titles.append(extractions.get_title(soup, e))
        #Get duratation
        genre.append(extractions.get_genre(soup, e))
        #Get genre
        duration.append(extractions.get_duration(soup, e))
        #Get year
        year.append(extractions.get_year(soup,e))
        #Get rating
        rating.append(extractions.get_rating(soup,e))
        #Get Gross
        gross.append(extractions.get_gross(soup,e))
        #Get votes
        votes.append(extractions.get_votes(soup,e))
        #Get Director/Directors
        directors.append(extractions.get_directors(soup,e))
        #Get Actors
        actors.append(extractions.get_actors(soup,e))
    
    # Get new url
    url_to_get = extractions.get_url(page)

    # Show the status
    print("Remaning web download", dur)
    dur = dur - 1
    
# Join all data in dataset
data = pd.DataFrame(list(zip(titles,
                             duration,
                             genre,
                             year,
                             rating, 
                             gross, 
                             directors,
                             actors)),
                    
                    columns=['titulo', 
                             'duracion', 
                             'genero', 
                             'year',
                             'rating', 
                             'gross', 
                             'directors', 
                             'actors'])

data.to_csv("datos.csv", index=False, sep=";")