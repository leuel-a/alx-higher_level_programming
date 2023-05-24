#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const WedgeAntilliesURL = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const BodyResponse = JSON.parse(body).results;

  let count = 0;
  for (const movie of BodyResponse) {
    for (const actor of movie.characters) {
      if (actor === WedgeAntilliesURL) {
        count++;
      }
    }
  }
  console.log(count);
});
