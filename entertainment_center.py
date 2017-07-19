import media
import fresh_tomatoes


get_out = media.Movie(
    "Get Out", "Boyfriend visits girlfriend's parents for "
    "the weekend and finds disturbing and horrifying family secrets",
    "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",  # NOQA
    "https://www.youtube.com/watch?v=sRfnevzM9kQ"
    )


beauty_and_the_beast = media.Movie(
   "Beauty and the Beast",
    "A young woman is taken prisoner by a beast, and eventually marries the"
    "beast.",
    "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=OvW_L8sTu5E"
    )

juno = media.Movie(
    "Juno",
    "A story about a teenage girl and her pregnancy",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgxMjgyMTcyNF5BMl5BanBnXkFtZTcwMDg1MTU1MQ@@._V1_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=K0SKf0K3bxg"
    )

ip_man = media.Movie(
    "Ip Man", "A story about a Kung Fu master in Foshan and his refusal of"
    "the Japanese",
    "https://upload.wikimedia.org/wikipedia/en/3/38/The_Legend_is_Born_%E2%80%93_Ip_Man_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1AJxXQ7xojE"
    )

fox_and_the_hound = media.Movie(
    "Fox and the Hound", "A story about two unlikely friends",
    "https://upload.wikimedia.org/wikipedia/en/7/70/The_Fox_and_the_Hound.jpg",
    "https://www.youtube.com/watch?v=XFwPyqQy9K0"
    )

hunger_games = media.Movie(
    "Hunger Games",
    "The children are forced to play deadly games for food",
    "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",   # NOQA
    "https://www.youtube.com/watch?v=4S9a5V9ODuY"
    )

movies = [get_out, beauty_and_the_beast, juno, ip_man, fox_and_the_hound, hunger_games]


fresh_tomatoes.open_movies_page(movies)
