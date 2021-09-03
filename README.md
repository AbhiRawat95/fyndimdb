# fyndimdb
MINI IMDB -- Python/Django

Model Details 

All basic movie details are store in the movie master table (Movie). For every movie we have the functionality to store the cast details and the reviews about the movie stored in these tables, Cast and Movie Review table. 

Since the listing and search of movie is the most important aspect of this project and relates to the customer experience, I have used Elasticsearch to make the listing and listing fast, moreover in both these operations we don’t need have to hit the database.  

Search can be performed on the following parameters:  

Title 

Director  

Genre 

Rating 

Popularity 

Cast 

Search Indexes can be found in the following file: search_indexes.py  

 

API List 

The project consists of the following API to carry out the basic operation on the platform: 

The same info is available on the home page of the application via swagger.  

Bulk Insertion of movies API:  /movie/movie-create/insert_movie_data/ 

Addition of a single movie API: /movie/prodv1/add-new-movie/ 

Listing of All Movies API: /movie/prodv1/movies-list/ [ This API fetches the list of 20 movies in a single hit and also there is a throttle applied on this Api] 

Search API: /movie/prodv1/search/?q=”searchterm” 

Update and Delete Movie API: /movie/prodv1/update-movie/{id}/ 

 

All the APIs can be tried on the home page of the application. 
