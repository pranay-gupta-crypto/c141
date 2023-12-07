from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_movies=movies_data[["original_title","poster_link","release_date", "runtime", "weighted_rating"]]


# variables to store data
liked_movies=[]
not_liked_movies=[]
did_not_watch=[]

# method to fetch data from database
def movie_details():
  m_data={
    "original_title":all_movies.iloc[0,0],
    "poster_link":all_movies.iloc[0,1],
    "release_date":all_movies.iloc[0,2],
    "duration":all_movies.iloc[0,3],
    "rating":all_movies.iloc[0,4]
  }
  return m_data

# /movies api
@app.route("/movies")
def get_movies():
  movie_data=movie_details()
  return jsonify({
    "data":movie_data,
    "status":"success"
    })

# /like api
@app.route("/like")
def liked_movie():
  global all_movies
  movies_data=movie_details()
  liked_movies.append(movies_data)
  all_movies.drop([0], inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify ({
    "status":"success"
  })
  
@app.route("/liked")
def like_movie():
  global liked_movies
  return jsonify({
    "data":liked_movies,
    "status":"success"
  })

# /dislike api
@app.route("/dislike")
def unliked_movie():
  global all_movies
  movies_data=movie_details()
  not_liked_movies.append(movies_data)
  all_movies.drop([0], inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify ({
    "status":"success"
  })

# /did_not_watch api
@app.route("/did_not_watch")
def did_not_watch_movie():
  global all_movies
  movies_data=movie_details()
  did_not_watch.append(movies_data)
  all_movies.drop([0], inplace=True)
  all_movies=all_movies.reset_index(drop=True)
  return jsonify ({
    "status":"success"
  })
  
  

if __name__ == "__main__":
  app.run()