// 3-get_ids_sum.js

/**
 * Calculates the sum of all the student IDs.
 * It accepts a list of students as a parameter and uses the reduce function on the array.
 *
 * @param {Array} students - Array of student objects with id attribute.
 * @returns {number} - The sum of all the student IDs.
 */
function getStudentIdsSum(students) {
  // Use the reduce function to accumulate the sum of student IDs
  const sumOfIds = students.reduce(
    (accumulator, student) => accumulator + student.id,
    0, // Initialize accumulator with 0
  );

  // Return the final sum of student IDs
  return sumOfIds;
}

// Export the function to make it accessible from other modules
export default getStudentIdsSum;
