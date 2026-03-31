// 0-promise.js

function getResponseFromAPI() {
  return new Promise((resolve) => {
    // Simulating a response from an API by resolving the promise immediately
    resolve('Simulated API response');
  });
}

export default getResponseFromAPI;
