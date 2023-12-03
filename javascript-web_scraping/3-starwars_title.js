#!/usr/bin/node

const { error } = require('console');
const request = require('request');
const movieId = process.argv[2];
const apiURL = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request.get(apiURL, (error, response, body) => {
    if (error) {
        console.error(`An error has occurred`);
    } else if (response.statusCode !== 200) {
        console.error(`Error code: ${response.statusCode}`);
    } else {
        const movieContent = JSON.parse(body);
        console.log(`${movieContent.title}`);
    }
});
