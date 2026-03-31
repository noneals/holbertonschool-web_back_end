// 1-get_list_student_ids.js

/**
 * Retrieves an array of student IDs from a list of student objects.
 * If the argument is not an array, returns an empty array.
 *
 * @param {Array} students - Array of student objects with id attribute.
 * @returns {Array} - Array of student IDs.
 */
function getListStudentIds(students) {
  // Check if the input is an array
  if (!Array.isArray(students)) {
    return [];
  }

  // Use the map function to extract and return an array of student IDs
  return students.map((student) => student.id);
}

// Export the function to make it accessible from other modules
export default getListStudentIds;
