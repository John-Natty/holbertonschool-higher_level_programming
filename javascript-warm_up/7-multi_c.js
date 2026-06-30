#!/usr/bin/node

// Convert the first argument to an integer
const number = parseInt(process.argv[2], 10);

// If the argument is missing or cannot be converted to a number
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  // Print "C is fun" the requested number of times
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
