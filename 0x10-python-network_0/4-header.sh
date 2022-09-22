#!/bin/bash
# Send GET request with header variable "X-School-User-Id" with a value of "98"
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
