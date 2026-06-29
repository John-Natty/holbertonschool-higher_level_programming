#!/usr/bin/node

// Count only the real arguments passed by the user
const argumentCount = process.argv.length - 2;

// If no argument is passed
if (argumentCount === 0) {
  console.log('No argument');

// If exactly one argument is passed
} else if (argumentCount === 1) {
  console.log('Argument found');

// If two or more arguments are passed
} else {
  console.log('Arguments found');
}
