#!/bin/bash
# Sends POST request with given variable parameters.
curl -X POST -F "email=test@gmail.com" -F "subject=I will always be here for PLD" "$1"
