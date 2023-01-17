#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file.
const args = process.argv;
const fs = require('fs');
const request = require('request');

request(args[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(args[3], body, {
    encoding: 'utf-8'
  }, err => {
    if (err) {
      console.log(err);
    }
  });
});
