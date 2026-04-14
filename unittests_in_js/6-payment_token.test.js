const assert = require('assert');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {

  it('should return correct data when success is true', function (done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        assert.deepStrictEqual(response, {
          data: 'Successful response from the API'
        });
        done();
      })
      .catch((err) => done(err));
  });

});