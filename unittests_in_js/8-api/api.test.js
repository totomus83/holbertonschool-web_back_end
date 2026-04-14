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

  it('other?', function (done) {
    request.get(url, function (err, res, body) {
      expect(res.headers['content-type']).to.contain('text/html');
      done();
    });
  });
});