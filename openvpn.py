import ast
from checks import AgentCheck
from subprocess import check_output


class OpenVPN(AgentCheck):


    def check(self, instance):
        metric_prefix = self.init_config.get('metric_prefix', 'openvpn')
        license_usage = self.get_license_usage()
        self.gauge('%s.licenses_used' % metric_prefix, license_usage['used'])
        self.gauge('%s.licenses_available' % metric_prefix, license_usage['available'])
        self.gauge('%s.licenses_total' % metric_prefix, license_usage['total'])


    def get_license_usage(self):
        sacli_path = self.init_config.get('sacli_path', '/usr/local/openvpn_as/scripts/sacli')
        lic_usage = ast.literal_eval(check_output(["sudo", sacli_path, "LicUsage"]).decode('utf-8'))
        return {
                    'used': lic_usage[0],
                    'total': lic_usage[1],
                    'available': lic_usage[1] - lic_usage[0]
                }


if __name__ == '__main__':
    check.check(instance)
