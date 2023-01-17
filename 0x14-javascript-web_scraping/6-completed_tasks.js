#!/usr/bin/node
// Computes the number of tasks completed by user id.
const args = process.argv;
const request = require('request');

request(args[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const completedTasks = {};
  const result = JSON.parse(body);
  for (let i = 0; i < result.length; i++) {
    const completed = result[i].completed;
    const key = result[i].userId.toString();
    if (completed === true) {
      if (completedTasks[key]) {
        completedTasks[key]++;
      } else {
        completedTasks[key] = 1;
      }
    }
  }
  console.log(completedTasks);
});
