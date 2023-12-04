#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, { json: true }, (error, response, todos) => {
  if (error) {
    console.error('An error has occurred');
  } else if (response.statusCode === 200) {
    const userTasksDone = {};
    const tasksDone = todos.filter(tasks => tasks.done);

    tasksDone.forEach(tasks => {
      if (!userTasksDone[tasks.userId]) {
        userTasksDone[tasks.userId] = 1;
      } else {
        userTasksDone[tasks.userId]++;
      }
    });

    Object.keys(userTasksDone).forEach(userId => {
      console.log(`${userId}: ${userTasksDone[userId]}`);
    });
  } else {
    console.error(`${response.statusCode}`);
  }
});
