// 2-get_students_by_loc.js

/**
 * Retrieves an array of students who are located in a specific city.
 * It accepts a list of students and a city as parameters.
 * Uses the filter function on the array to get students in the specified city.
 *
 * @param {Array} students - Array of student objects with location attribute.
 * @param {string} city - The city to filter students by.
 * @returns {Array} - Array of student objects in the specified city.
 */
function getStudentsByLocation(students, city) {
  // Use the filter function to get students in the specified city
  const studentsInCity = students.filter((student) => student.location === city);

  // Return the array of students in the specified city
  return studentsInCity;
}

// Export the function to make it accessible from other modules
export default getStudentsByLocation;
