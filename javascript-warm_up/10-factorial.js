#!/usr/bin/node

// Compute the factorial of a number recursively
function factorial (n) {
  // Factorial of NaN is 1, and factorial of 0 or 1 is 1
  if (isNaN(n) || n <= 1) {
    return 1;
  }

  // Recursive case: n! = n * (n - 1)!
  return n * factorial(n - 1);
}

// Convert the first argument to an integer
const number = parseInt(process.argv[2], 10);

// Print the factorial result
console.log(factorial(number));
