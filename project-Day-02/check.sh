#!/bin/bash

# Simple URL Status Checker
# Loops through urls.txt and prints HTTP status code

while read url; do
    status=$(curl -o /dev/null -s -w "%{http_code}" $url)
    echo "$url -> $status"
done < urls.txt
