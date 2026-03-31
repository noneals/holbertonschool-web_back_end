// 9-groceries_list.js

/**
 * Returns a map of groceries with specified items and quantities.
 *
 * @returns {Map} - A map containing groceries with items and quantities.
 */
export default function groceriesList() {
  // Create a new Map to store groceries with items and quantities.
  const groceryMap = new Map();

  // Define the list of groceries with items and quantities.
  const groceryItems = [
    { name: 'Apples', quantity: 10 },
    { name: 'Tomatoes', quantity: 10 },
    { name: 'Pasta', quantity: 1 },
    { name: 'Rice', quantity: 1 },
    { name: 'Banana', quantity: 5 },
  ];

  // Iterate through the groceryItems list and add each item to the groceryMap.
  groceryItems.forEach((item) => {
    // Destructure item to get name and quantity.
    const { name, quantity } = item;

    // Add the item and its quantity to the groceryMap.
    groceryMap.set(name, quantity);
  });

  // Return the final groceryMap.
  return groceryMap;
}
