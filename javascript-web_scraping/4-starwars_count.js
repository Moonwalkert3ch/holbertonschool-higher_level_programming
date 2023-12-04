#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
    if (error) {
        console.error(`error code: ${response.statusCode}`);
    } else if (response.statusCode === 200) {
        const results = JSON.parse(body).results;
        const count = results.reduce(function (occurrence, film) {
            if (film.characters.find(function (character) {
                return character.endsWith('/18/');
            })) {
                occurrence = occurrence + 1;
            }
            return occurrence;
        }, 0);

        console.log(count);
    } else {
        console.error('Error code:', response.statusCode);
    }
});
