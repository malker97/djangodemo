#!/usr/bin/env bash
# start-server.sh
(cd src; gunicorn djangodemo.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"