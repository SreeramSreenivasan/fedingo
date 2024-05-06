# shell script to loop over lines of file
#!/bin/bash
while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p"
done < "$1"
