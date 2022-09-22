#!/bin/bash
# Script to show allowed methods on url
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
