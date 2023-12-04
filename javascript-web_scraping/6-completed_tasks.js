#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, { json: true }, (error, response, todos) => {
  if (error) {
    console.error('An error has occurred');
  } else if (response.statusCode === 200) {
    const userTasksCompleted = {};

    const completedTasks = todos.filter(tasks => tasks.completed);

    completedTasks.forEach(tasks => {
      if (!userTasksCompleted[tasks.userId]) {
        userTasksCompleted[tasks.userId] = new Set([tasks.id]);
      } else {
        userTasksCompleted[tasks.userId].add(tasks.id);
      }
    });

    Object.keys(userTasksCompleted).forEach(userId => {
      console.log(`'${userId}': ${userTasksCompleted[userId].size}`);
    });
  } else {
    console.error(`${response.statusCode}`);
  }
});
