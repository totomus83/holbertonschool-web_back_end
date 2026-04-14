const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {

  describe('SUM', function () {
    it('should add rounded numbers', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should round both numbers', function () {
      assert.strictEqual(calculateNumber('SUM', 1.6, 4.4), 6);
    });

    it('should handle negatives', function () {
      assert.strictEqual(calculateNumber('SUM', -1.2, -3.7), -5);
    });
  });

  describe('SUBTRACT', function () {
    it('should subtract rounded numbers', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should handle mixed rounding', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.6, 4.4), -2);
    });

    it('should handle negatives', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.2, -3.7), 3);
    });
  });

  describe('DIVIDE', function () {
    it('should divide rounded numbers', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should handle division with rounding', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.6, 4.4), 0.5);
    });

    it('should return Error when dividing by 0', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return Error when rounded b is 0', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.2), 'Error');
    });

    it('should handle negatives', function () {
      assert.strictEqual(calculateNumber('DIVIDE', -1.2, -3.7), 0.5);
    });
  });

});