#!/bin/bash
TARGET=$1
DATE=$(date +%Y-%m-%d)
if [ -z "$TARGET" ]; then
    echo "Usage: ./port_report.sh <IP_ADDRESS>"
    exit 1
fi
OUTFILE="scan_${TARGET}_${DATE}.txt"
echo "--- Scan Results for $TARGET ---" > "$OUTFILE"

OPEN_COUNT=0

for PORT in 21 22 80 443 3306; do
    # Using /dev/tcp for a lightweight scan
    timeout 1 bash -c "echo > /dev/tcp/$TARGET/$PORT" 2>/dev/null
    
    if [ $? -eq 0 ]; then
        echo "Port $PORT: OPEN" >> "$OUTFILE"
        ((OPEN_COUNT++))
    else
        echo "Port $PORT: CLOSED" >> "$OUTFILE"
    fi
done

echo "Summary: Found $OPEN_COUNT open ports."
echo "Results saved to $OUTFILE"
