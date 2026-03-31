// 5-typed_arrays.js

/**
 * Creates a new ArrayBuffer with an Int8 value at a specific position.
 *
 * @param {number} length - The length of the ArrayBuffer.
 * @param {number} position - The position where the Int8 value should be added.
 * @param {number} value - The Int8 value to be added at the specified position.
 * @returns {DataView} - DataView object representing the modified ArrayBuffer.
 * @throws {Error} - Throws an error if adding the value is not possible.
 */
export default function createInt8TypedArray(length, position, value) {
  // 1. Create a new ArrayBuffer with the specified length
  const buffer = new ArrayBuffer(length);

  // 2. Create a DataView to manipulate the ArrayBuffer
  const dataView = new DataView(buffer);

  // 3. Check if the specified position is within the valid range
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // 4. Set the Int8 value at the specified position
  dataView.setInt8(position, value);

  // 5. Return the modified DataView
  return dataView;
}
