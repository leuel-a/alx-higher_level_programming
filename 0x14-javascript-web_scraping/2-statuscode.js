#!/usr/bin/node
// Display the status code of a GET request
const request = require('request');
const args = process.argv;

request(args[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code: ' + response.statusCode);
});
