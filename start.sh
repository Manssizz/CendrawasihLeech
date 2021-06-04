if [[ -n $RCLONE_CONFIG ]]; then
 echo "Rclone config detected"
 echo -e "$RCLONE_CONFIG" > /app/rclone.conf
fi
# Create homepage web page
python3 homepage.py &
python3 -m tobrot