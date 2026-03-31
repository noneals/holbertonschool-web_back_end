// 6-set.js

/**
 * Creates a Set from an array of elements.
 *
 * @param {Array} array - The input array.
 * @returns {Set} - A Set containing unique elements from the array.
 */
function setFromArray(array) {
  // Using the Set constructor to create a new Set from the input array
  const uniqueSet = new Set(array);

  // Returning the created Set
  return uniqueSet;
}

// Exporting the function to make it available for other modules
export default setFromArray;
