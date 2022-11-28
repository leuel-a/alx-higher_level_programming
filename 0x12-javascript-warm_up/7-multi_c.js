#!/usr/bin/node
/**
 * Prints x times “C is fun”
 *  ->> Where x is the first argument of the script
 *  ->> If the first argument can’t be converted to an integer, print “Missing number of occurrences”
 */

const args = process.argv;

if (isNaN(args[2] * 1)) {
  console.log('Missing number of occurrences');
} else {
  const numOfOccurence = args[2] * 1;
  for (let i = 0; i < numOfOccurence; i++) {
    console.log('C is fun');
  }
}
