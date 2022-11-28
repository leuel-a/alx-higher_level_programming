#!/usr/bin/node
/**
 * Computes and prints the factorial of a number
 */

function findFactorial (number) {
  if (number === 1 || isNaN(number)) {
    return (1);
  }
  return (number * findFactorial(number - 1));
}

const args = process.argv;
console.log(findFactorial(args[2] * 1));
