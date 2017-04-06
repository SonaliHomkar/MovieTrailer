import media
import fresh_tomatoes



zootopia = media.Movie("Zootopia",
                       "Welcome to the urban jungle. ",
                       "http://vignette4.wikia.nocookie.net/disney/images/2/2f/Zootopia_Poster.jpg/revision/latest?cb=20160615162624",
                       "https://www.youtube.com/watch?v=5nP9hU8eUfE")

tangled = media.Movie("Tangled",
                      "Get tangled up.",
                      "http://www.filmofilia.com/wp-content/uploads/2010/11/tangled_poster_nov.jpg",
                      "https://www.youtube.com/watch?v=ip_0CFKTO9E")



wallE = media.Movie("WallE",
                    "In Space, No One Can Hear You Clean",
                    "http://www.pixartalk.com/wp-content/uploads/2009/06/wallefinal.jpg",
                    "https://www.youtube.com/watch?v=alIq_wG9FNk")


finding_nemo = media.Movie("Finding Nemo",
                           "Sea it for the first time in 3D (2012 re-release)",
                           "https://d35fkdjhhgt99.cloudfront.net/static/use-media-items/17/16316/full-900x1300/56702cc2/pva6ds.jpeg?resolution=0",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

titanic = media.Movie("Titanic",
                      "Nothing On Earth Could Come Between Them.",
                      "http://www.impawards.com/1997/posters/titanic_ver2.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

jungle_book = media.Movie("Jungle Book",
                          "The legend will never be the same.",
                          "http://www.impawards.com/2016/posters/jungle_book_ver6_xlg.jpg",
                          "https://www.youtube.com/watch?v=HcgJRQWxKnw")

#jungle_book.show_trailer()

Movies = [zootopia,tangled,wallE,finding_nemo,titanic,jungle_book]

fresh_tomatoes.open_movies_page(Movies)
#tangled.show_trailer()
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__ + "\n NAme : " + media.Movie.__name__ + "\n Module " + media.Movie.__module__) 
