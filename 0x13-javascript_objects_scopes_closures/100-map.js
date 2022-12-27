#!/usr/bin/node

// Importing for '100-data.js' the list
const list = require('./100-data').list;

console.log(list);

// Create a new list by using a map
const newList = list.map(function(x, i) {
  return x * i;
})

console.log(newList);
