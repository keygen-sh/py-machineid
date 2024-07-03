import unittest
from unittest.mock import Mock, patch

import machineid


RETURNS_NONE = Mock(return_value=None)


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
