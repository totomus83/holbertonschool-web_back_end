// Display welcome message
console.log("Welcome to Holberton School, what is your name?");

// Set up input listener
process.stdin.setEncoding('utf8');

process.stdin.on('data', (data) => {
  const name = data.trim(); // Remove newline/whitespace
  console.log(`Your name is: ${name}`);
});

// Handle program exit
process.on('exit', () => {
  console.log("This important software is now closing");
});
