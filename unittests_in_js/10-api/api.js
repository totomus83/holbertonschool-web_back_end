const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 7865;

// Middleware to parse JSON
app.use(bodyParser.json());

// Root endpoint (if already exists)
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// ✅ GET /available_payments
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

// ✅ POST /login
app.post('/login', (req, res) => {
  const { userName } = req.body;
  res.send(`Welcome ${userName}`);
});

// Start server
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app; // important for testing