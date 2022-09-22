#Bash script to get the size of the body of the response.
#!/usr/bin/env bash
curl -s $1 | wc -c
