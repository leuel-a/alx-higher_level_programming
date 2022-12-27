#!/usr/bin/node

exports.converter = function (base) {
  return function convertNumtoBase (number) {
    return number.toString(base);
  };
};
