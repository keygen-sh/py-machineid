from sys import platform
from uuid import UUID

import machineid
import unittest


class TestMachineId(unittest.TestCase):
    def uuid_formatted_id(self):
        self.assertTrue(isinstance(machineid.uuid_formatted_id(), str))
        self.assertTrue(len(machineid.uuid_formatted_id()) > 0)
        self.assertTrue(
            machineid.uuid_formatted_id("foo") != machineid.uuid_formatted_id("bar")
        )
        self.assertTrue(
            machineid.uuid_formatted_id("foo") != machineid.uuid_formatted_id()
        )
        uuid_set = set()
        for _ in range(100):
            uuid_set.add(machineid.uuid_formatted_id())
        self.assertEqual(len(uuid_set), 100)
        self.assertIsInstance(UUID(machineid.uuid_formatted_id().lower), UUID)

    def test_hashed_id(self):
        self.assertTrue(isinstance(machineid.hashed_id(), str))
        self.assertTrue(len(machineid.hashed_id()) > 0)
        self.assertTrue(machineid.hashed_id("foo") != machineid.hashed_id("bar"))
        self.assertTrue(machineid.hashed_id("foo") != machineid.hashed_id())

    def test_id(self):
        self.assertTrue(isinstance(machineid.id(), str))
        self.assertTrue(len(machineid.id()) > 0)
        self.assertTrue(machineid.id() != machineid.hashed_id())


if __name__ == "__main__":
    unittest.main()
