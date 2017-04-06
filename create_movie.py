from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from MovieDatabase_setup import Base,Movie

engine = create_engine('sqlite:///moviedatabase.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# create a new entry in movie table

zootopia = Movie(title="Zootopia",tagline="Welcome to the urban jungle. ",
                 img_url="http://vignette4.wikia.nocookie.net/disney/images/2/2f/Zootopia_Poster.jpg/revision/latest?cb=20160615162624",
                 trailer="https://www.youtube.com/watch?v=5nP9hU8eUfE")
session.add(zootopia)
session.commit()

tangled = Movie(title="Tangled",tagline="Get tangled up.",
                img_url="http://www.filmofilia.com/wp-content/uploads/2010/11/tangled_poster_nov.jpg",
                trailer="https://www.youtube.com/watch?v=ip_0CFKTO9E")
session.add(tangled)
session.commit()
print("done tangled")


wallE = Movie(title="WallE",tagline="In Space, No One Can Hear You Clean",
              img_url="http://www.pixartalk.com/wp-content/uploads/2009/06/wallefinal.jpg",
              trailer="https://www.youtube.com/watch?v=alIq_wG9FNk")
session.add(wallE)
session.commit()

print("done wallE")

finding_nemo = Movie(title="Finding Nemo",tagline="Sea it for the first time in 3D (2012 re-release)",
                     img_url="https://d35fkdjhhgt99.cloudfront.net/static/use-media-items/17/16316/full-900x1300/56702cc2/pva6ds.jpeg?resolution=0",
                     trailer="https://www.youtube.com/watch?v=wZdpNglLbt8")
session.add(finding_nemo)
session.commit()

print("done finding_nemo")

titanic = Movie(title="Titanic",tagline="Nothing On Earth Could Come Between Them.",
                img_url="http://www.impawards.com/1997/posters/titanic_ver2.jpg",
                trailer="https://www.youtube.com/watch?v=zCy5WQ9S4c0")
session.add(titanic)
session.commit()

print("done titanic")

jungle_book = Movie(title="Jungle Book",tagline="The legend will never be the same.",
                    img_url="http://www.impawards.com/2016/posters/jungle_book_ver6_xlg.jpg",
                    trailer="https://www.youtube.com/watch?v=HcgJRQWxKnw")

session.add(jungle_book)
session.commit()
print("done jungle_book")





# read first entry from database
firstresult = session.query(Movie).first()
print("Name : " +  firstresult.title)
print("done")
