#!/bin/bash

echo "---- URL Status Check ----"

while read url
do
    status=$(curl -o /dev/null -s -w "%{http_code}" $url)
    echo "$url -> $status"
done < urls.txt
