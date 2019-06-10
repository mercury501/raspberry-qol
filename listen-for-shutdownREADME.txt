README

sudo mv listen-for-shutdown.py /usr/local/bin/
sudo mv listen-for-shutdown.sh /etc/init.d/




sudo chmod +x /usr/local/bin/listen-for-shutdown.py
sudo chmod +x /etc/init.d/listen-for-shutdown.sh


sudo update-rc.d listen-for-shutdown.sh defaults


TO START IMMEDIATELY

sudo /etc/init.d/listen-for-shutdown.sh start


or just put everything in a folder and run install.sh