#!/usr/bin/node
/**
 * Prints 3 lines by using an array of string and a loop
 *
 * Output ->>
 *  $ ./6-multi_languages_loop.js
 *  C is fun
 *  Python is cool
 *  JavaScript is amazing
 */

const myArr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (let i = 0; i < myArr.length; i++) {
  console.log(myArr[i]);
}
