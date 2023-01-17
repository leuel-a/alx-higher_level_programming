#!/usr/bin/node
// Computes the number of tasks completed by user id.
const args = process.argv;
const request = require('request');

request(args[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  let count = 0;
  const completedTasks = {};
  const result = JSON.parse(body);
  for (let i = 1; i <= 10; i++) {
    for (let j = 0; j < result.length; j++) {
      if (result[j].userId === i) {
        if (result[j].completed === true) {
          count++;
        }
      }
    }
    completedTasks[i] = count;
    if (count !== 0) {
      count = 0;
    }
  }
  console.log(completedTasks);
});
