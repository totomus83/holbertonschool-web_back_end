import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const filePath = process.argv[2];

    readDatabase(filePath)
      .then((data) => {
        let response = 'This is the list of our students';
        const fields = Object.keys(data).sort(
          (a, b) => a.toLowerCase().localeCompare(b.toLowerCase()),
        );
        for (const field of fields) {
          const list = data[field];
          response += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
        }
        res.status(200).send(response);
      })
      .catch((err) => {
        res.status(500).send(err.message);
      });
  }

  static getAllStudentsByMajor(req, res) {
    const filePath = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(filePath)
      .then((data) => {
        const list = data[major];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch((err) => {
        res.status(500).send(err.message);
      });
  }
}

export default StudentsController;
