import subprocess
import unittest
from unittest.mock import MagicMock, Mock, mock_open, patch

import machineid

RETURNS_NONE = Mock(return_value=None)
CALL_FAILURE = Mock(side_effect=subprocess.CalledProcessError(
  cmd='powershell.exe',
  returncode=1)
)
WINREG_ERROR = MagicMock()
WINREG_ERROR.return_value.__enter__.return_value.read_entry.side_effect = OSError()

class TestExceptionsHandling(unittest.TestCase):
  @patch.multiple(
    'machineid',
    __exec__=RETURNS_NONE,
    __read__=RETURNS_NONE,
    __reg__=RETURNS_NONE,
  )
  def test_raises_custom_error(self):
    with self.assertRaises(machineid.MachineIdNotFound):
      machineid.id()

  @patch.multiple(
    'machineid',
    __exec__=RETURNS_NONE,
    __read__=RETURNS_NONE,
  )
  def test_logs_winreg_error(self):
    with patch('machineid.WinRegistry', WINREG_ERROR):
      with self.assertLogs(machineid.log, level='DEBUG'):
        result = machineid.__reg__(r'HKEY_LOCAL_MACHINE\TEST', 'TEST')
        self.assertIsNone(result)

  @patch.multiple(
    'machineid',
    __exec__=RETURNS_NONE,
    __reg__=RETURNS_NONE,
  )
  def test_logs_read_error(self):
    with patch('builtins.open', mock_open()) as fake_open:
      fake_open.side_effect = IOError()
      with self.assertLogs(machineid.log, level='DEBUG'):
        result = machineid.__read__('/tmp/testfile')
        self.assertIsNone(result)

  @patch.multiple(
    'machineid',
    __read__=RETURNS_NONE,
    __reg__=RETURNS_NONE,
  )
  def test_logs_exec_error(self):
    with patch('machineid.subprocess.call', CALL_FAILURE):
      with self.assertLogs(machineid.log, level='DEBUG'):
        result = machineid.__exec__('powershell.exe doTest')
        self.assertIsNone(result)

