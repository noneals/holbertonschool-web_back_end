// 10-update_uniq_items.js

/**
 * Updates unique items in a map.
 *
 * @param {Map} groceryMap - The map to be updated.
 * @throws {Error} Will throw an error if the argument is not a map.
 * @returns {Map} The updated map.
 */
export default function updateUniqueItems(groceryMap) {
  // Check if the argument is a Map
  if (!(groceryMap instanceof Map)) {
    throw Error('Cannot process');
  }

  // Iterate over the Map
  for (const item of groceryMap) {
    // Check if the quantity is 1
    if (item[1] === 1) {
      // Update the quantity to 100
      groceryMap.set(item[0], 100);
    }
  }

  // Return the updated Map
  return groceryMap;
}
