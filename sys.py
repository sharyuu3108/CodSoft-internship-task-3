import pandas as pd # type: ignore    

# Set of same movies and their genres
film_data = {
    'film_title': ['Phir Hera Pheri', 'Dhamal', 'Golmaal', 'Stree', 'Welcome','Munjya','Entertainment','Dream Girl',
                   'Bhool Bhulaiya','Khichdi:The Movie','Hungama','Roohi','Fukrey','Bhoot Police','Hera Pheri'],
    'film_genres': ['Comedy|Thriller', 'Comedy|Thriller', 'Comedy|Family', 'Comedy|Horror', 'Comedy|Drama','Comedy|Horror','Comedy|Drama','Comedy|Drama',
                    'Comedy|Horror','Comedy|Drama','Comedy|Family','Comedy|Horror','Comedy|Thriller','Comedy|Horror','Comedy|Thriller']
}

film_df = pd.DataFrame(film_data)

# defining a funtion to find genre similarity
def genre_similarity(genres1, genres2):
    genres1_set = set(genres1.split('|'))
    genres2_set = set(genres2.split('|'))
    intersection = genres1_set.intersection(genres2_set)
    union = genres1_set.union(genres2_set)
    return len(intersection) / len(union) if len(union) > 0 else 0

#Movies not found similar to dataset
def recommend_movies(movie_title, film_df, top_n=4):
    if movie_title not in film_df['film_title'].values:
        return "Movie not found in the dataset."
    
    # to compute similarity scores
    movie_genres = film_df[film_df['film_title'] == movie_title]['film_genres'].values[0]
    film_df['Similarity'] = film_df['film_genres'].apply(lambda x: genre_similarity(movie_genres, x))
    
    # get recommendations of other movies
    film_recommendations = film_df[film_df['film_title'] != movie_title].sort_values(by='Similarity', ascending=False).head(top_n)
    
    # Return only the movie titles
    return film_recommendations['film_title'].tolist()

# taking user input in main function
def main():
    movie_title = input("Please enter movie of your choice: ")
    film_recommendations = recommend_movies(movie_title,film_df)
    
    if isinstance(film_recommendations, str):
        print(film_recommendations) 
    else:
        if film_recommendations:
            print(f"We have some recommendations that you may like based on the movie '{movie_title}':")
            for title in film_recommendations:
                print(f"- {title}")
        else:
            print(f"No recommendations found based on the movie '{movie_title}'.")

if __name__ == "__main__":
    main()