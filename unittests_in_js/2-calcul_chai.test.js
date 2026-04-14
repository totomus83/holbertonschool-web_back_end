const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function () {

  describe('SUM', function () {
    it('should add rounded numbers', function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should round both numbers', function () {
      expect(calculateNumber('SUM', 1.6, 4.4)).to.equal(6);
    });

    it('should handle negatives', function () {
      expect(calculateNumber('SUM', -1.2, -3.7)).to.equal(-5);
    });

    it('should handle mixed signs', function () {
      expect(calculateNumber('SUM', -1.2, 3.7)).to.equal(3);
    });
  });

  describe('SUBTRACT', function () {
    it('should subtract rounded numbers', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should handle mixed rounding', function () {
      expect(calculateNumber('SUBTRACT', 1.6, 4.4)).to.equal(-2);
    });

    it('should handle negatives', function () {
      expect(calculateNumber('SUBTRACT', -1.2, -3.7)).to.equal(3);
    });

    it('should handle mixed signs', function () {
      expect(calculateNumber('SUBTRACT', -1.2, 3.7)).to.equal(-5);
    });
  });

  describe('DIVIDE', function () {
    it('should divide rounded numbers', function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should handle division with rounding', function () {
      expect(calculateNumber('DIVIDE', 1.6, 4.4)).to.equal(0.5);
    });

    it('should return Error when dividing by 0', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return Error when rounded b is 0', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0.2)).to.equal('Error');
    });

    it('should handle negatives', function () {
      expect(calculateNumber('DIVIDE', -1.2, -3.7)).to.equal(0.25);
    });

    it('should handle mixed signs', function () {
      expect(calculateNumber('DIVIDE', -1.2, 3.7)).to.equal(-0.25);
    });
  });

});