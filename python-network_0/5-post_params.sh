#!/bin/bash
# Curl sends POST req to URL, display response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
