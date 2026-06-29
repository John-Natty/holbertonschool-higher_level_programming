#!/usr/bin/node

// Store the first argument passed to the script
const firstArgument = process.argv[2];

// If no argument was passed, the value is undefined
if (firstArgument === undefined) {
  console.log('No argument');
} else {
  // Otherwise, print the first argument
  console.log(firstArgument);
}
