#!/usr/bin/node
/**
 * Converts the first argument passed to it to an integer
 * and prints to the stdout
 *
 * Format: My number: <first argument converted in integer>
 *
 * Example:
 *  $ ./5-to_integer.js 89
 *  $ 89
 */

const argv = process.argv;
if (isNaN(argv[2] * 1)) {
  console.log('Not a number');
} else {
  console.log(argv[2] * 1);
}
