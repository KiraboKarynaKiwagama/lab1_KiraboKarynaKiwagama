#!/bin/bash

# checking to see the archive directory exists
if [ ! -d "archive" ]; then
    mkdir archive
    echo "Created 'archive' directory."
fi

#  Then we generate a timestamp string
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

#define the file names
ORIGINAL="grades.csv"
ARCHIVED="grades_${TIMESTAMP}.csv"

#  Archive the file (rename + move in one mv command)

if [ -f "$ORIGINAL" ]; then
    mv "$ORIGINAL" "archive/$ARCHIVED"
    echo "Moved '$ORIGINAL' to 'archive/$ARCHIVED'."
else
    echo "Warning: '$ORIGINAL' not found. Nothing to archive."
fi

# Create a fresh empty grades.csv
touch "$ORIGINAL"
echo "Created fresh empty '$ORIGINAL'."

#  Log the operation to organizer.log
# Each run adds a new line so the log accumulates.
LOG_ENTRY="[${TIMESTAMP}] Archived: ${ORIGINAL} -> archive/${ARCHIVED}"
echo "$LOG_ENTRY" >> organizer.log
echo "Logged to organizer.log: $LOG_ENTRY"