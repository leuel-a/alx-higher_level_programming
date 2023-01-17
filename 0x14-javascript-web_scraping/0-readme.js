#!/usr/bin/node
// Reads a file and prints the content of the file
const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
