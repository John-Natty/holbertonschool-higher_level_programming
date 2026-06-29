#!/usr/bin/node

// Get the first argument passed to the script
const firstArgument = process.argv[2];

// Convert the first argument to an integer
const number = parseInt(firstArgument, 10);

// Check if the conversion failed
if (isNaN(number)) {
  console.log('Not a number');
} else {
  // Print the converted integer
  console.log('My number: ' + number);
}
