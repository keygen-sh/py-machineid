from sys import platform

import machineid
import unittest

class TestMachineId(unittest.TestCase):
  def test_hashed_id(self):
    self.assertIsInstance(machineid.hashed_id(), str)
    self.assertGreater(len(machineid.hashed_id()), 0)
    self.assertNotEqual(machineid.hashed_id('foo'), machineid.hashed_id('bar'))
    self.assertNotEqual(machineid.hashed_id('foo'), machineid.hashed_id())

  def test_id(self):
    self.assertIsInstance(machineid.id(), str)
    self.assertGreater(len(machineid.id()), 0)
    self.assertNotEqual(machineid.id(), machineid.hashed_id())

if __name__ == '__main__':
  unittest.main()
