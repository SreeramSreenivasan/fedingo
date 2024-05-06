# shell script to loop through files in directory
#!/bin/bash

FILES="$1/*"
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  # perform some operation with the file
done
