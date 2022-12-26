#!/usr/bin/node

// Importing the Square class
const PreviousSquare = require('./5-square');
const process = require('process');

class Square extends PreviousSquare {
  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
}

module.exports = Square;
