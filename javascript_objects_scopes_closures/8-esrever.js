#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    const valueAtIndex = list[i];
    reversedList.push(valueAtIndex);
  }
  return reversedList;
};
