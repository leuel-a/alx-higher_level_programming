#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }

  // Check if the response does not contain a valid JSON
  const todos = JSON.parse(body);

  const result = {};
  todos.forEach(todo => {
    if (todo.completed && result[todo.userId] === undefined) {
      result[todo.userId] = 1;
    } else if (todo.completed) {
      result[todo.userId] += 1;
    }
  });
  console.log(result);
});
