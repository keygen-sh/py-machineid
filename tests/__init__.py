from sys import platform

import machineid
import unittest

class TestMachineId(unittest.TestCase):
  def test_hashed_id(self):
    self.assertTrue(isinstance(machineid.hashed_id(), str))
    self.assertTrue(len(machineid.hashed_id()) > 0)
    self.assertTrue(machineid.hashed_id('foo') != machineid.hashed_id('bar'))
    self.assertTrue(machineid.hashed_id('foo') != machineid.hashed_id())

  def test_id(self):
    self.assertTrue(isinstance(machineid.id(), str))
    self.assertTrue(len(machineid.id()) > 0)
    self.assertTrue(machineid.id() != machineid.hashed_id())

if __name__ == '__main__':
  unittest.main()