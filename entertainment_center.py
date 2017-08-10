import media
import fresh_tomatoes

toy_story=media.Movie("Toystory",
                      "Toys that come to life",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar=media.Movie("Avatar",
                      "A marine on alien planet",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")

now_you_see_me=media.Movie("Now you see me",
                      "4 Magicians rocking the world",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Now_You_See_Me_Poster.jpg/220px-Now_You_See_Me_Poster.jpg",
                      "https://www.youtube.com/watch?v=KzJNYYkkhzc")

the_social_network=media.Movie("The Social Network",
                      "Story of facebook",
                      "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                      "https://www.youtube.com/watch?v=lB95KLmpLR4")

the_internship=media.Movie("The Internship",
                      "Story of Google Internship",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/e/ed/The-internship-poster.jpg/220px-The-internship-poster.jpg",
                      "https://www.youtube.com/watch?v=cdnoqCViqUo")

iron_man_3=media.Movie("Iron Man 3",
                      "Battle against world bad powers",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/d/d5/Iron_Man_3_theatrical_poster.jpg/220px-Iron_Man_3_theatrical_poster.jpg",
                      "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")


movies=[toy_story,avatar,now_you_see_me,the_social_network,the_internship,iron_man_3]
fresh_tomatoes.open_movies_page(movies)









