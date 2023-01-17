#!/usr/bin/node
// Writes a string to a file
const fs = require('fs');
const args = process.argv;

fs.writeFile(args[2], args[3], {
  encoding: 'utf-8'
}, err => {
  if (err) {
    console.log(err);
  }
});
