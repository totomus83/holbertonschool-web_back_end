const request = require('request');
const { expect } = require('chai');

describe('Index page', function () {
  const url = 'http://localhost:7865';

  it('correct status code?', function (done) {
    request.get(url, function (err, res, body) {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('correct result?', function (done) {
    request.get(url, function (err, res, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', function () {
  const url = 'http://localhost:7865';

  it('correct status code for number id?', function (done) {
    request.get(`${url}/cart/12`, function (err, res, body) {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('correct status code for non-number id?', function (done) {
    request.get(`${url}/cart/hello`, function (err, res, body) {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});