#!/bin/bash
set -e

if [ -z "$1" ]; then
  echo "Usage: $0 \"49. Group Anagrams\""
  exit 1
fi

# "49. Group Anagrams" -> "49-Group-Anagrams"
branch=$(echo "$1" | sed 's/\. /-/g; s/ /-/g')

git sw main && git pull
git sw -c "$branch"
cp -r template "$branch"

echo "Ready: $branch"
