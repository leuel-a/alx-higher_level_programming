#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }

  // Check if the response does not contain a valid JSON
  try {
    body = JSON.parse(body);
  } catch (error) {
    return console.log(error);
  }

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
