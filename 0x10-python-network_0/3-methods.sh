#!/bin/bash
# Script to show allowed methods on url
curl -s "$1" -X OPTIONS
