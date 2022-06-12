#!/usr/bin/env bash
#------------------------
#   POLYBAR :: POWERMENU
#------------------------

# :: Main

dir="$HOME/.config/rofi"
rofi_command="rofi -theme $dir/barmenu.rasi"

shutdown=""
reboot=""
logout=""

options="$shutdown\n$reboot\n$logout"

chosen="$(echo -e "$options" | $rofi_command -dmenu)"
case $chosen in
	$shutdown)
		systemctl poweroff
        ;;
	$reboot)
		systemctl reboot
        ;;
	$logout)
		i3-msg exit
        ;;
esac
