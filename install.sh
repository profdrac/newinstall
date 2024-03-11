# run as sudo
cp -r new/* ~
cd ~
sudo pacman -S - < pkglist
pipx install pywal
pipx install pywalfox
pipx install prettytable
mv bashrc .bashrc
mv bash_profile .bash_profile
mv xinitrc .xinitrc
mv config .config
mv scripts .scripts
chmod +x .scripts/*.sh
chmod +x .config/polybar/launch.sh
mkdir ~/Documents/words
mkdir ~/.config/dunst
wal -i Pictures/twigs.jpg
ln -sf ~/.cache/wal/dunstrc ~/.config/dunst/dunstrc
#chmod +x ~/.scripts/Zathura-Pywal/install.sh
#sudo ~/.scripts/Zathura-Pywal/./install.sh
sudo pacman -S virtualbox-guest-utils
sudo systemctl enable vboxservice
sudo usermod -a -G vboxsf ashu
echo "All done! Reboot and enjoy!"
# install pywalfox plugin
