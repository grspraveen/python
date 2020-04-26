#lets see data operations

import pandas as pd 

df_movie_rating = pd.DataFrame({'movie 1':[5,4,3,3,2,1],
                              'movie 2':[4,3,5,2,5,4]},
                              index = ['Tom','Jeff','Peter','Ram','Ted','Paul'])

print(df_movie_rating)

#now lets change the rating to values to string 

def movie_grade(rating):
    if (movie_grade==5):
        return "amazing"
    elif (movie_grade==4):
        return "Good"
    else:
        return "average and poor"

df_modifed_mov_rating = df_movie_rating.applymap(movie_grade)

    