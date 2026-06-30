#!/usr/bin/node

// Convert all command line arguments to numbers
const args = process.argv.slice(2).map(Number);

// If there are less than 2 arguments, print 0
if (args.length < 2) {
  console.log(0);
} else {
  // Sort numbers from biggest to smallest
  args.sort((a, b) => b - a);

  // Print the second biggest number
  console.log(args[1]);
}
