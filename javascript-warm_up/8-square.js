#!/usr/bin/node

// Convert the first argument to an integer
const size = parseInt(process.argv[2], 10);

// If the argument is missing or cannot be converted to a number
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // Print one line of X, size times
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
