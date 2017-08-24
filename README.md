# OpenVPN DataDog Agent

Adds OpenVPN licensing stats to DataDog.

![](../master/screenshot.png)

## Installation

### Automated

The included [install.sh](install.sh) script will copy the files to the correct locations, give `dd-agent` permissions to interact with OpenVPN, and restart the agent.

### Manual

1. Copy [openvpn.py](openvpn.py) to `/etc/dd-agent/checks.d`
2. Copy [openvpn.yaml](openvpn.yaml) to `/etc/dd-agent/conf.d`
3. Add `dd-agent ALL=NOPASSWD: /usr/local/openvpn_as/scripts/sacli` to `/etc/sudoers` using `visudo`
4. Restart the agent with `/etc/init.d/datadog-agent restart`
