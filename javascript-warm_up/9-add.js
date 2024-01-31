#!/usr/bin/node
const add = (a, b) => {
  const res = Number(a) + Number(b);
  console.log(res);
};

const first = process.argv[2];
const second = process.argv[3];

add(first, second);
