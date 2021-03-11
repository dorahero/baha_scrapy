from baha.utils import ScyllaProxies, MongoProxies
PROXY_LIST = MongoProxies("proxy_checked").get_all_data()