#!/bin/bash
if pgrep -x "picom" > /dev/null
then
	killall picom
	polybar-msg hook pic 1
else
	picom -b --config ~/.config/picom/picom.conf
	polybar-msg hook pic 2
fi
