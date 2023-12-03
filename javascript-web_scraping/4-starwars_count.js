#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
    if (error) {
        console.error(`An error has occurred`);
    } else if (response.statusCode === 200) {
        const filmsResponse = JSON.parse(body);
        const wedgeFilms = filmsResponse.results.filter(movie =>
            movie.characters.includes('https://swapi-api.hbtn.io/api/people/18')
        );
        console.log(`${wedgeFilms.length}`);
    } else {
        console.error(`error code: ${response.statusCode}`);
    }
});
