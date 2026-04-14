const sinon = require('sinon');
const assert = require('assert');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {

  it('should use stub and log correct message', function () {
    // Stub calculateNumber
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Spy console.log
    const spy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    // Check stub call
    assert.strictEqual(stub.calledOnce, true);
    assert.strictEqual(stub.calledWith('SUM', 100, 20), true);

    // Check console.log
    assert.strictEqual(spy.calledOnce, true);
    assert.strictEqual(spy.calledWith('The total is: 10'), true);

    // Restore
    stub.restore();
    spy.restore();
  });

});