#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';


request(url + id, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  console.log(JSON.parse(body).title);
});
