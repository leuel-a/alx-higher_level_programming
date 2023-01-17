#!/usr/bin/node
// Prints the title of a Star Wars movie
// where the episode number matches a given integer.
const request = require('request');
const args = process.argv;

const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
