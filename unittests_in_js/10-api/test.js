const request = require('request');
const { expect } = require('chai');

describe('API endpoints', () => {
  const baseUrl = 'http://localhost:7865';

  // ✅ Test /available_payments
  describe('GET /available_payments', () => {
    it('should return correct payment methods object', (done) => {
      request.get(`${baseUrl}/available_payments`, (err, res, body) => {
        expect(res.statusCode).to.equal(200);

        const parsed = JSON.parse(body);

        // Deep equality check
        expect(parsed).to.deep.equal({
          payment_methods: {
            credit_cards: true,
            paypal: false,
          },
        });

        done();
      });
    });
  });

  // ✅ Test /login
  describe('POST /login', () => {
    it('should return Welcome username', (done) => {
      request.post(
        {
          url: `${baseUrl}/login`,
          json: { userName: 'Betty' },
        },
        (err, res, body) => {
          expect(res.statusCode).to.equal(200);
          expect(body).to.equal('Welcome Betty');
          done();
        }
      );
    });
  });
});