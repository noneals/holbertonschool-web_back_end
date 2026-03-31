// 8-clean_set.js

/**
 * Returns a string of set values that start with a specific string.
 *
 * @param {Set} aSet - The input Set to filter values from.
 * @param {string} startString - The specific string that values should start with.
 * @returns {string} - A string containing values from the set that start with the specified string.
 */
export default function cleanSet(aSet, startString) {
  // Initialize an empty array to store filtered values.
  const res = [];

  // Initialize an empty string to store the final result.
  let result = '';

  // Check if startString is provided and is a string.
  if (startString && typeof startString === 'string') {
    // Loop through each element in the set.
    for (const set of aSet) {
      // Check if the element starts with the specified string.
      if (set && set.startsWith(startString)) {
        // If it does, extract the substring after the startString.
        const temp = set.slice(startString.length);
        // Push the extracted substring into the result array.
        res.push(temp);
      }
    }

    // Join the result array using '-' as a separator to create the final string.
    result = res.join('-');
  }

  // Return the final result.
  return result;
}
