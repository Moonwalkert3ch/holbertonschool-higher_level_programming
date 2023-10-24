-- Lists all genres and displays number of shows linked
SELECT genres.name AS genre, COUNT(genres.id) AS number_of_shows
FROM genres JOIN tv_show_genre
ON tv_show_genre.genres_id = genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
