#!/usr/bin/node
const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let prints = '';
    for (let xx = 0; xx < this.height; xx++) {
      for (let yy = 0; yy < this.width; yy++) {
        prints = prints + 'X';
      }
      console.log(prints);
      prints = '';
    }
  }
};
module.exports = Rectangle;
