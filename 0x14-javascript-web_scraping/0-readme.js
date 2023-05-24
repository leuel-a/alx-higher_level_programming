#!/usr/bin/node

const fs = require('fs');
const file_name = process.argv[2];

fs.readFile(file_name, function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString());
});
