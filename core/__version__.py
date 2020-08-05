import sys
import platform

__title__ = 'KunLun-M'
__description__ = 'Code Security Audit'
__url__ = 'https://github.com/LoRexxar/Cobra-W'
__issue_page__ = 'https://github.com/LoRexxar/Cobra-W/issues/new'
__python_version__ = sys.version.split()[0]
__platform__ = platform.platform()
__version__ = '2.0 beta1'
__author__ = 'LoRexxar'
__author_email__ = 'LoRexxar@gmail.com'
__license__ = 'MIT License'
__copyright__ = 'Copyright (C) 2017 LoRexxar. All Rights Reserved'
__introduction__ = """
 _   __            _                      ___  ___
| | / /           | |                     |  \/  |
| |/ / _   _ _ __ | |    _   _ _ __ ______| .  . |
|    \| | | | '_ \| |   | | | | '_ \______| |\/| |
| |\  \ |_| | | | | |___| |_| | | | |     | |  | |
\_| \_/\__,_|_| |_\_____/\__,_|_| |_|     \_|  |_/  -v{version}

GitHub: https://github.com/LoRexxar/Cobra-W

KunLun-M is a static code analysis system that automates the detecting vulnerabilities and security issue.""".format(version=__version__)
__epilog__ = """Usage:
  python {m} -t {td}
  python {m} -t {td} -r 1000, 1001
  python {m} -t {td} -s wordpress
  python {m} -t {td} -f json -o /tmp/report.json 
  python {m} -t {td} --debug
  python {m} -t {td} -d -u
  python {m} -t {td} --lan php -b vendor --debug
  python {m} -t {td} --lan php -s roundcube -d -uc
  
  python {m} --list php
""".format(m='kunlun.py', td='tests/vulnerabilities')
