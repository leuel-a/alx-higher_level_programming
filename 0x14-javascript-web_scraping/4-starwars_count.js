#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const WedgeAntilliesURL = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const BodyResponse = JSON.parse(body)['results'];

  let count = 0;
  for (let movie of BodyResponse) {
    for (let actor of movie.characters) {
      if (actor.endsWith('18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
