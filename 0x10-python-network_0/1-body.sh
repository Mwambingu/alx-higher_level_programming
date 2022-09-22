#!/usr/bin/bash
#Script to Get usr body response with status 200
curl -sfL "$1" -X GET
