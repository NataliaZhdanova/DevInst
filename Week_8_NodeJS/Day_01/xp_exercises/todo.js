// 🌟 Exercise 4: Todo List Using ES6 Module Syntax
// Instructions
// Create a directory named todoApp.

// Inside the todoApp directory, create two files: todo.js and app.js.

// In todo.js, define an ES6 module that exports a TodoList class.

// The TodoList class should have methods to add tasks, mark tasks as complete, and list all tasks.

// Export the TodoList class.

// In app.js, import the TodoList class from the todo.js module.

// Create an instance of the TodoList class.

// Add a few tasks, mark some as complete, and list all tasks.

// Run app.js and verify that the todo list operations are working correctly.


class TodoList {
	constructor() {
		this.taskList = [];
	}
	addTask(task) {
		this.taskList.push({ task, completed: false });
	}
    completeTask(task) {
        const foundTask = this.taskList.find(item => item.task === task);
        if (foundTask) {
            foundTask.completed = true;
        } else {
            console.error(`The task: "${task}" - was not found.`);
        }
    }
    allTasks() {
        console.log("My tasks:");
        this.taskList.forEach((item, index) => {
          const status = item.completed ? 'Completed' : 'Incomplete';
          console.log(`${index + 1}. ${item.task} - ${status}`);
        });
      }
}


export default TodoList;
