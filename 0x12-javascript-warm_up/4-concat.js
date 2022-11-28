#!/usr/bin/node
/**
 * Prints two arguments passed to it, in the following format: “ is ”
 *  ->> Example: $ ./4-concat.js c cool
 *               $ c is cool
 */

const args = process.argv;
console.log(args[2] + ' is ' + args[3]);
