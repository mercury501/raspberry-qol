#! /bin/bash
sudo mv listen-for-shutdown.py /usr/local/bin/
sudo mv listen-for-shutdown.sh /etc/init.d/




sudo chmod +x /usr/local/bin/listen-for-shutdown.py
sudo chmod +x /etc/init.d/listen-for-shutdown.sh


sudo update-rc.d listen-for-shutdown.sh defaults

sudo /etc/init.d/listen-for-shutdown.sh start
