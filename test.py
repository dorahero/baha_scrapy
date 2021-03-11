from baha.util.proxy_list import PROXY_LIST
from proxy_checker import ProxyChecker

checker = ProxyChecker()
for p in PROXY_LIST:
    ip = p['proxy'].split(':')[1].replace('//', '')
    port = p['port']
    print(ip, port)
    c = checker.check_proxy('{}:{}'.format(ip, port))
    print(c)
