export default class Currency {
  constructor(code, name) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._name = name;
    this._code = code;
  }

  get code() {
    return this._code;
  }

  set code(newcode) {
    if (typeof newcode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = newcode;
  }

  get name() {
    return this._name;
  }

  set name(newname) {
    if (typeof newname !== 'string') {
      throw new TypeError('Name must be a string');
				    }
    this._name = newname;
		      }
  displayFullCurrency(name,code) {
    return `${this._name} (${this._code})`;
  }
}
