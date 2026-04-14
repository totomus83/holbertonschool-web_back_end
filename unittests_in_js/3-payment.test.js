const sinon = require('sinon');
const assert = require('assert');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {

  it('should call Utils.calculateNumber with SUM, 100, 20', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    assert.strictEqual(spy.calledOnce, true);
    assert.strictEqual(spy.calledWith('SUM', 100, 20), true);

    spy.restore();
  });

});