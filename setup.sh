#!/bin/bash

mongoimport --upsert -d odgcdb -c courses --file ./src/test_courses.json
export EVE_SETTINGS=`pwd`/src/settings.py
./src/api.py
