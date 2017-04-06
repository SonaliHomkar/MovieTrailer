from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from MovieDatabase_setup import Base,Movie
import media
import fresh_tomatoes

engine = create_engine('sqlite:///moviedatabase.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


movielist = session.query(Movie).all()
arrMovie = []
for movie in movielist:
    print("title : " + movie.title)
    objmovie = media.Movie(movie.title,movie.tagline,movie.img_url,movie.trailer)
    arrMovie.append(objmovie)
    print(objmovie.storyline)
    



fresh_tomatoes.open_movies_page(arrMovie)
