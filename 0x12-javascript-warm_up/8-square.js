#!/usr/bin/node
/**
 * Prints a square to stdout
 *  ->> The character 'X' is used to print the square
 */

const args = process.argv;

if (isNaN(args[2] * 1)) {
  console.log('Missing size');
} else {
  const size = args[2] * 1;
  let square = '';
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    if (i !== (size - 1)) {
      square += '\n';
    }
  }
  console.log(square);
}
