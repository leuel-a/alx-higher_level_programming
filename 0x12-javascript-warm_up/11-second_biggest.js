#!/usr/bin/node
/**
 * Searches the second biggest integer in the list of arguments.
 */

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  const nums = args.slice(2).sort();
  console.log(nums[nums.length - 2]);
}
