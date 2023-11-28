#!/bin/bash
# A bash script that makes request to a certain ip
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: HolbertonSchool" -d "user_id=98"
