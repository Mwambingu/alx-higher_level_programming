#!/bin/bash
# Sends JSON post request to url passed as arg and displays the body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
