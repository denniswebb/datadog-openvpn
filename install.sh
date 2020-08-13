#!/bin/sh

if [ -d /etc/dd-agent ]; then
  DIR="/etc/dd-agent"
elif [ -d /etc/datadog-agent ]; then
  DIR="/etc/datadog-agent"
else
  echo "Datadog not found."
  exit 1
fi


if [ -e /usr/local/openvpn_as/scripts/sacli ]; then
  cp openvpn.py $DIR/checks.d/openvpn.py
	cp openvpn.yaml $DIR/conf.d/openvpn.yaml

	echo 'dd-agent ALL=NOPASSWD: /usr/local/openvpn_as/scripts/sacli' | sudo EDITOR='tee -a' visudo

	/etc/init.d/datadog-agent restart

else
  echo "openvpn_as not found."
  exit 1
fi
