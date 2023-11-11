// Create another file named read-directory.js.

// In read-directory.js, use the fs module to read the list of files in a specified directory and display their names in the terminal.

// Open a terminal in the file-explorer directory.

// Run node copy-file.js to copy the content from source.txt to destination.txt.

// Run node read-directory.js to list the files in the directory.

import fs from "fs";

const path = './';

fs.readdir(path, (err, files) => {
  if (err) {
    console.log("error!");
  }

  console.log("The following files are in the directory:");
  files.forEach(file => {
    console.log(file);
  });
});
