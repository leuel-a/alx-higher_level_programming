#!/usr/bin/node
/**
 * Searches the second biggest integer in the list of arguments.
 */

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let max = args[2] * 1; let secondMax = args[3] * 1;
  for (let i = 2; i < args.length; i++) {
    if ((args[i] * 1) > max) {
      secondMax = max;
      max = args[i] * 1;
    }
  }
  console.log(secondMax);
}
