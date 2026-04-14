function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({
      data: 'Successful response from the API'
    });
  }

  // undefined otherwise (no return)
}

module.exports = getPaymentTokenFromAPI;