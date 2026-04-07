const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n');
      const rows = lines.slice(1).filter((row) => row.trim() !== '' && row.split(',').length === 4);

      const fields = {};
      rows.forEach((row) => {
        const columns = row.split(',');
        const firstName = columns[0].trim();
        const field = columns[3].trim();

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      });

      console.log(`Number of students: ${rows.length}`);
      for (const [field, students] of Object.entries(fields)) {
        console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
      }

      resolve(); // Résout la promesse
    });
  });
}

module.exports = countStudents;
