const express = require('express');
const fs = require('fs');

const countStudents = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter((line) => line.trim() !== '');
    const result = [];

    result.push(`Number of students: ${students.length}`);

    const fields = {};
    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    Object.entries(fields).forEach(([field, names]) => {
      result.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    });

    resolve({ total: students.length, fields, output: result.join('\n') });
  });
});

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = process.argv[2];
  countStudents(databasePath)
    .then(({ output }) => {
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((error) => {
      res.send(`This is the list of our students\n${error.message}`);
    });
});

app.get('/students/:major', (req, res) => {
  const { major } = req.params;

  if (major !== 'CS' && major !== 'SWE') {
    res.status(500).send('Major parameter must be CS or SWE');
    return;
  }

  const databasePath = process.argv[2];
  countStudents(databasePath)
    .then(({ fields }) => {
      const names = fields[major] || [];
      res.send(`List: ${names.join(', ')}`);
    })
    .catch((error) => {
      res.status(500).send(error.message);
    });
});

app.listen(1245);

module.exports = app;
