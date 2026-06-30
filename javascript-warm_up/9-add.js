#!/usr/bin/node

// Add two numbers and return the result
function add (a, b) {
  return a + b;
}

// Convert the first argument to an integer
const firstNumber = parseInt(process.argv[2], 10);

// Convert the second argument to an integer
const secondNumber = parseInt(process.argv[3], 10);

// Print the result of the addition
console.log(add(firstNumber, secondNumber));
