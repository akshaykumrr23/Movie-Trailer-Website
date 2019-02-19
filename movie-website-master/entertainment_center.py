# importing python modules for using their functions in our code
import fresh_tomatoes
import media
# moviename=(movie title,movie storyline,poster url,youtube url)
rangdb = media.movie("Rang de Basanti", "The story of six young Indians " +
                     "who assist an English Woman to film a documentary " +
                     "on the extremist " +
                     "freedom fighters from their past and the events that lead them to " +
                     "relive the long forgotten saga of freedom.",
                     "http://www.gstatic.com/tv/thumb/movieposters/160770/p160770_p_v8_aa.jpg",
                     "https://www.youtube.com/watch?v=l-BTOTtcGmk")
# moviename=(movie title,movie storyline,poster url,youtube url)
guru = media.movie("Guru", "A villager, Gurukant Desai, arrives in Bombay 1958 " +
                   "and rises from its streets to become the GURU, the biggest tycoon in " +
                   "Indian history.",
                   "http://media.glamsham.com/download/poster/images/guru/guru_01.jpg",
                   "https://www.youtube.com/watch?v=D1eE-lCKcxI")
# moviename=(movie title,movie storyline,poster url,youtube url)
attacks = media.movie("The attacks of 26/11", "The 2008 Mumbai attacks" +
                      "(also referred to as 26/11) were a group of terrorist attacks that " +
                      "took place in November 2008, when 10 members of Lashkar-e-Taiba, " +
                      "An Islamic terrorist organisation based in Pakistan, carried out a " +
                      "series of 12 coordinated shooting and bombing attacks lasting four " +
                      "days across Mumbai.",
                      "https://i.ytimg.com/vi/gv70tdtOO5k/movieposter.jpg",
                      "https://www.youtube.com/watch?v=20v_DINmWXo")
# moviename=(movie title,movie storyline,poster url,youtube url)
holiday = media.movie("Holiday-An officer is never off duty", "A military officer uses his " +
                      "intellect and fighting skills to hunt and knock down a terrorist " +
                      "aiming to rip apart Mumbai via the sleeper cells under his command.",
                      "http://t2.gstatic.com/images?q=tbn:ANd9GcS2clCe4icHqs7oeHoxWZoUoJws1botHH-S9SpUOrqFLkc38Ej9",
                      "https://www.youtube.com/watch?v=oZ3r-m7RH_8")
# moviename=(movie title,movie storyline,poster url,youtube url)
singh = media.movie("bhaag milkha bhaag", "The truth behind the ascension of Milkha " +
                    "The Flying Sikh Singh who was scarred because of the India-Pakistan " +
                    "partition.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/Bhaag_Milkha_Bhaag_poster.jpg/220px-Bhaag_Milkha_Bhaag_poster.jpg",
                    "https://www.youtube.com/watch?v=u71swQ4ksgI")
# moviename=(movie title,movie storyline,poster url,youtube url)
barfi = media.movie("Bareili ki Barfi", "Set in the small-town of Bareilly," +
                    "Bitti is a free-spirited young girl who lives life on her own terms and " +
                    "refuses to be pressured into getting married.",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcSiHuA7DeOgLXJj_l5LeslSR33q4pcJgiiOV9xWs_xr9mzfPU99",
                    "https://www.youtube.com/watch?v=Ds2JXPKZB6s")
movies = [rangdb, guru, attacks, holiday, singh, barfi]
# passing movies to the media file for storing movies
fresh_tomatoes.open_movies_page(movies)
# fresh_tomatoes is the html page that opens movie
# page in the webbrowser
