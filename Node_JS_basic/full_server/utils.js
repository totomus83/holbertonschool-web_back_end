import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      if (lines.length < 2) {
        resolve({});
        return;
      }

      const students = {};
      for (let i = 1; i < lines.length; i += 1) {
        const line = lines[i].trim();
        if (line) {
          const parts = line.split(',');
          const field = parts[3];
          const firstname = parts[0];

          if (!students[field]) students[field] = [];
          students[field].push(firstname);
        }
      }

      resolve(students);
    });
  });
}

export default readDatabase;
