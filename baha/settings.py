# Scrapy settings for baha project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# import logging
# from logging.handlers import RotatingFileHandler

# from scrapy.utils.log import configure_logging

# LOG_ENABLED = False
# # Disable default Scrapy log settings.
# configure_logging(install_root_handler=False)

# # Define your logging settings.
# log_file = 'log/CRAWLER_logs.log'

# root_logger = logging.getLogger()
# root_logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# rotating_file_log = RotatingFileHandler(log_file, maxBytes=10485760, backupCount=1)
# rotating_file_log.setLevel(logging.ERROR)
# rotating_file_log.setFormatter(formatter)
# root_logger.addHandler(rotating_file_log)

BOT_NAME = 'baha'

SPIDER_MODULES = ['baha.spiders']
NEWSPIDER_MODULE = 'baha.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baha (+http://www.yourdomain.com)'
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS = 1024

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'baha.middlewares.BahaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'baha.middlewares.BahaDownloaderMiddleware': 543,
#}
from baha.utils import ScyllaProxies, MongoProxies
# PROXY_POOL_ENABLED = True
ROTATING_PROXY_LIST = MongoProxies("proxy_checked").get_all_proxies()
DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 800,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 800,
}
# PROXY_POOL_ENABLED = True
# DOWNLOADER_MIDDLEWARES = {
#     # ...
#     'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
#     'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
#     # ...
# }
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'baha.pipelines.BahaPipeline': 300,
#}
from baha.util.mongo_setting import *
ITEM_PIPELINES = {
   'baha.pipelines.BahaPipeline': 300,
}
MONGO_URI=f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/"
MONGO_DATABASE="baha"
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# REACTOR_THREADPOOL_MAXSIZE = 20