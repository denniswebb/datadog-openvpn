try:
    from datadog_checks.base import AgentCheck
except ImportError:
    from checks import AgentCheck
from datadog_checks.utils.subprocess_output import get_subprocess_output


class OpenVPN(AgentCheck):
    def check(self, instance):
        metric_prefix = self.init_config.get("metric_prefix", "openvpn")
        license_usage = self.get_license_usage()
        self.gauge("%s.licenses_used" % metric_prefix, license_usage["used"])
        self.gauge("%s.licenses_available" % metric_prefix, license_usage["available"])
        self.gauge("%s.licenses_total" % metric_prefix, license_usage["total"])

    def get_license_usage(self):
        sacli_path = self.init_config.get(
            "sacli_path", "/usr/local/openvpn_as/scripts/sacli"
        )
        sacli_licusage = ["sudo", sacli_path, "LicUsage"]

        out, err, retcode = get_subprocess_output(
            sacli_licusage, self.log, raise_on_empty_output=True
        )
        out_split = out[3:-2].splitlines()
        lic_usage = [int(n.strip(", ")) for n in out_split]
        return {
            "used": lic_usage[0],
            "total": lic_usage[1],
            "available": lic_usage[1] - lic_usage[0],
        }
