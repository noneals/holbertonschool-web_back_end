// 7-has_array_values.js

/**
 * Checks if all elements in the array exist within the set.
 *
 * @param {Set} set - The Set to check against.
 * @param {Array} array - The Array containing elements to check.
 * @returns {boolean} - True if all elements in the array exist in the set, otherwise false.
 */
function hasValuesFromArray(set, array) {
  // Using the every method to check if all elements in the array are present in the set
  const allValuesExist = array.every((element) => set.has(element));

  // Returning the result
  return allValuesExist;
}

// Exporting the function to make it available for other modules
export default hasValuesFromArray;
