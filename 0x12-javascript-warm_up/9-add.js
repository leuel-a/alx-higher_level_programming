#!/usr/bin/node
/**
 * Prints the addition of 2 integers
 */

const args = process.argv;
function add (a, b) {
  return (a + b);
}

const num1 = args[2] * 1;
const num2 = args[3] * 1;
console.log(add(num1, num2));
