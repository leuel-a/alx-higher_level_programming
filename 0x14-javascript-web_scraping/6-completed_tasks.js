#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }

  body = JSON.parse(body);
  const result = {};
  for (const task of body) {
    if (task.userId in result === false) {
      result[task.userId] = 0;
    }

    if (task.completed === true) {
      result[task.userId]++;
    }
  }
  console.log(result);
});
