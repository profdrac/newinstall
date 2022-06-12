# run as sudo
mv new/* ~
rm new
cd ~
sudo pacman -S - < pkglist
sudo pip3 install pywal
sudo pip3 install pywalfox
sudo pywalfox install
mv bashrc .bashrc
mv xinitrc .xinitrc
mv config .config
mv scripts .scripts
chmod +x .scripts/*.sh
chmod +x .config/polybar/launch.sh
wal -i Pictures/sky.jpg
ln -sf ~/.cache/wal/dunstrc ~/.config/dunst/dunstrc
chmod +x ~/.scripts/Zathura-Pywal/install.sh
sudo ~/.scripts/Zathura-Pywal/./install.sh
sudo pacman -S virtualbox-guest-utils
sudo systemctl enable vboxservice
sudo usermod -a -G vboxsf ashu
echo "All done! Reboot, startx and enjoy!"
# install pywalfox plugin
