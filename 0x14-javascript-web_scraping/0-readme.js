#!/usr/bin/node

const fs = require('fs');
const FileName = process.argv[2];

fs.readFile(FileName, 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString());
});
