cp openvpn.py /etc/dd-agent/checks.d/openvpn.py
cp openvpn.yaml /etc/dd-agent/conf.d/openvpn.yaml

echo 'dd-agent ALL=NOPASSWD: /usr/local/openvpn_as/scripts/sacli' | sudo EDITOR='tee -a' visudo

/etc/init.d/datadog-agent restart
