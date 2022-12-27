#!/usr/bin/node

// Importing for '100-data.js' the list
const list = require('./100-data').list;
const newList = list.map(x => x * list.indexOf(x));

console.log(list);
console.log(newList);
