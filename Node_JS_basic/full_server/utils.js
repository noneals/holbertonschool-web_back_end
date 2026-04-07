const fs = require('fs');
const path = require('path');

function readDatabase(filepath) {
  return new Promise((resolve, reject) => {
    const absolutePath = path.resolve(filepath);
    fs.promises.readFile(absolutePath, 'utf-8')
      .then((data) => {
        const lines = data.split('\n').slice(1);
        const filteredLines = lines.filter((line) => line.trim() !== '');

        const students = {};
        filteredLines.forEach((line) => {
          const [firstname, , , field] = line.split(',');
          if (!students[field]) students[field] = [];
          students[field].push(firstname);
        });

        resolve(students);
      })
      .catch((Error) => {
        reject(new Error('Cannot load the database'));
      });
  });
}

module.exports = readDatabase;
