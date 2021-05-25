# Tollywood-movie-recommendation--api

Demo website : https://movierecommender-telugu.herokuapp.com/

# api endpoints: 
## /recommend 
    
    enter movie names
    example 

    * C/o Kancharapalem
    * Jersey
    * World Famous Lover
    * Dear Comrade
    * example request for this list of movies is like:
    * C/o Kancharapalem,Jersey,World Famous Lover,Dear Comrade
    * url    https://movierecommender-telugu.herokuapp.com/recommend?movie=C/o Kancharapalem,Jersey,World Famous Lover,Dear Comrade&number=100
    * number  number default is 10 if u want more than or less than that u can specify with number in url
    
### Example Response
## For Url  
<https://movierecommender-telugu.herokuapp.com/recommend?movie=C/o%20Kancharapalem,Jersey,World%20Famous%20Lover,Dear%20Comrade&number=10>
 
                 [
                  {
                    "link": "https://www.imdb.com/title/tt5991672/",
                    "percentage": 47.04987696586325,
                    "title": "Yuddam"
                  },
                  {
                    "link": "https://www.imdb.com/title/tt10506490/",
                    "percentage": 27.935622389399946,
                    "title": "Kousalya Krishnamurthy"
                  },
                  {
                    "link": "https://www.imdb.com/title/tt7317482/",
                    "percentage": 25.0145006447368,
                    "title": "Pailwaan"
                  }
                ]
## /genres
  * enter any only one genre 
  * where api response will contain all telugu movies from imdb based on given genre
![alt text](https://png.pngtree.com/png-clipart/20200805/ourmid/pngtree-black-exclamation-mark-warning-sign-on-yellow-triangle-png-image_2316977.png "Logo Title Text 1")






