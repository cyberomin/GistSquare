#!/bin/sh

user=$(whoami)

cd /home/$user/TheMuse/

sudo ./manage.py celeryd -B --loglevel=INFO