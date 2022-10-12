"""
py-machineid
~~~~~~~~~~~~

Get the unique machine ID of any host (without admin privileges).

Basic usage:

    >>> import machineid
    >>> machineid.id()
    17A28A73-BEA9-4D4B-AF5B-03A5AAE9B92C

You can anonymize the ID like so, with an optional app ID:

    >>> machine.hashed_id('myappid')
    366048092ef4e7db53cd7adec82dcab15ab67ac2a6b234dc6a69303a4dd48e83
    >>> machine.hashed_id()
    ce2127ade536eaa9529f4a7b73141bbc2f094c46e32742c97679e186e7f13fde

Special thanks to Denis Brodbeck for his Go package, machineid (https://github.com/denisbrodbeck/machineid).

:license: MIT, see LICENSE for more details.
"""

__version__ = '0.1.0'
__author__  = 'Zeke Gabrielse'
__credits__ = 'https://github.com/denisbrodbeck/machineid'

from sys import platform
import subprocess
import hashlib
import hmac

def __run__(cmd: str) -> str:
  return subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
                   .stdout \
                   .strip()

def id() -> str:
  """
  id returns the platform specific device GUID of the current host OS.
  """

  id = ''

  if platform == 'darwin':
    id = __run__("ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'")

  if platform == 'win32' or platform == 'cygwin' or platform == 'msys':
    id = __run__('wmic csproduct get uuid').split('\n')[1] \
                                           .strip()

  if platform.startswith('linux'):
    id = __run__('cat /var/lib/dbus/machine-id')
    if id == '':
      id = __run__('cat /etc/machine-id')

  if platform.startswith('openbsd') or platform.startswith('freebsd'):
    id = __run__('cat /etc/hostid')
    if id == '':
      id = __run__('kenv -q smbios.system.uuid')

  if id == '':
    raise Exception('failed to obtain id on platform {}'.format(platform))

  return id

def hashed_id(app_id: str = '') -> str:
  """
  hashed_id returns the device's native GUID, hashed using HMAC-SHA256 with an optional application ID.
  """

  return hmac.new(bytes(app_id.encode()), id().encode(), hashlib.sha256).hexdigest()
