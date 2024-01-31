#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) return null;
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
