#!/bin/bash

# -------------------------------------------------------
# STEP 1: Ensure the archive directory exists
# The -d flag checks if it's a directory. If not, create it.
# -------------------------------------------------------
if [ ! -d "archive" ]; then
    mkdir archive
    echo "Created 'archive' directory."
fi

# -------------------------------------------------------
# STEP 2: Generate a timestamp string
# date +FORMAT — %Y=year, %m=month, %d=day, %H=hour,
# %M=minute, %S=second. Matches the example in the spec.
# -------------------------------------------------------
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# -------------------------------------------------------
# STEP 3: Define filenames
# -------------------------------------------------------
ORIGINAL="grades.csv"
ARCHIVED="grades_${TIMESTAMP}.csv"

# -------------------------------------------------------
# STEP 4: Archive the file (rename + move in one mv command)
# mv moves AND renames simultaneously.
# -------------------------------------------------------
if [ -f "$ORIGINAL" ]; then
    mv "$ORIGINAL" "archive/$ARCHIVED"
    echo "Moved '$ORIGINAL' to 'archive/$ARCHIVED'."
else
    echo "Warning: '$ORIGINAL' not found. Nothing to archive."
fi

# -------------------------------------------------------
# STEP 5: Create a fresh empty grades.csv
# The 'touch' command creates an empty file.
# -------------------------------------------------------
touch "$ORIGINAL"
echo "Created fresh empty '$ORIGINAL'."

# -------------------------------------------------------
# STEP 6: Log the operation to organizer.log
# >> appends to the file (>> creates it if it doesn't exist).
# Each run adds a new line so the log accumulates.
# -------------------------------------------------------
LOG_ENTRY="[${TIMESTAMP}] Archived: ${ORIGINAL} -> archive/${ARCHIVED}"
echo "$LOG_ENTRY" >> organizer.log
echo "Logged to organizer.log: $LOG_ENTRY"