#!/usr/bin/node
const secondBiggest = () => {
  const args = process.argv.slice(2);
  if (args.length < 2) {
    console.log(0);
    return;
  }
  let max = Number.MIN_SAFE_INTEGER;
  let secondMax = Number.MIN_SAFE_INTEGER;
  for (let i = 0; i < args.length; i++) {
    if (Number(args[i]) > max) {
      secondMax = max;
      max = Number(args[i]);
    } else if (Number(args[i]) > secondMax) {
      secondMax = Number(args[i]);
    }
  }
  console.log(secondMax);
};
secondBiggest();
