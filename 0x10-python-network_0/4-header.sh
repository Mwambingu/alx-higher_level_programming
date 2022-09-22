#!/bin/bash
# Send GET request with header variable "X-School-User-Id" with a value of "98"
curl -sH "X-School-User-Id: 98" "$1"
