FILE=/home/ashu/.scripts/psrid
if [ "$1" = "on" ]; then
	if test -f "$FILE"; then
		dunstify -u low "  Watcher is already on!"
	else
		python ~/.scripts/psr.py & echo $! > /home/ashu/.scripts/psrid
		dunstify -u low "  : ON"
	fi
else
	if test -f "$FILE"; then
		kill -9 $(</home/ashu/.scripts/psrid)
		dunstify -u low "  : OFF"
		rm /home/ashu/.scripts/psrid
	else
		dunstify -u low "  Watcher is already off!"
	fi
fi
