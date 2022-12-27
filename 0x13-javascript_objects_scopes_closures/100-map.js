#!/usr/bin/node

// Importing for '100-data.js' the list
const list = require('./100-data').list;

console.log(list);

// Create a new list by using a map
let i = 0;
const newList = list.map(function (x) {
  return x * i++;
});

console.log(newList);
