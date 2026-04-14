const sinon = require('sinon');
const assert = require('assert');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function () {

  let spy;

  beforeEach(function () {
    spy = sinon.spy(console, 'log');
  });

  afterEach(function () {
    spy.restore();
  });

  it('should log 120 for (100, 20)', function () {
    sendPaymentRequestToApi(100, 20);

    assert.strictEqual(spy.calledOnce, true);
    assert.strictEqual(spy.calledWith('The total is: 120'), true);
  });

  it('should log 20 for (10, 10)', function () {
    sendPaymentRequestToApi(10, 10);

    assert.strictEqual(spy.calledOnce, true);
    assert.strictEqual(spy.calledWith('The total is: 20'), true);
  });

});