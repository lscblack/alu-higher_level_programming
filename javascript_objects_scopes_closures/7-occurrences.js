#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  list.forEach(element => {
    if (element === searchElement) {
      num += 1;
    }
  });
  return num;
};
