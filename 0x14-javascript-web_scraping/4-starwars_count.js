#!/usr/bin/node
// Prints the number of movies where the
// character “Wedge Antilles” is present.
const args = process.argv;
const request = require('request');

request(args[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  let count = 0;
  const results = JSON.parse(body).results;
  for (let i = 0; i < results.length; i++) {
    const characters = results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j].endsWith('18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
