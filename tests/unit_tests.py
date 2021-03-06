import json
import unittest
from builtins import str, bytes
try:
    from test import support
except ImportError:
    # Try to import from the Python2 path
    from test import test_support as support

from blockstack_zones import make_zone_file, parse_zone_file
from test_sample_data import zone_files, zone_file_objects


class ZoneFileTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_zone_file_creation_1(self):
        json_zone_file = zone_file_objects["sample_1"]
        zone_file = make_zone_file(json_zone_file)
        print(zone_file)
        self.assertTrue(isinstance(zone_file, (str, bytes)))
        self.assertTrue("$ORIGIN" in zone_file)
        self.assertTrue("$TTL" in zone_file)
        self.assertTrue("@ 1D IN URI" in zone_file)

    def test_zone_file_creation_2(self):
        json_zone_file = zone_file_objects["sample_2"]
        zone_file = make_zone_file(json_zone_file)
        print(zone_file)
        self.assertTrue(isinstance(zone_file, (str, bytes)))
        self.assertTrue("$ORIGIN" in zone_file)
        self.assertTrue("$TTL" in zone_file)
        self.assertTrue("@ IN SOA" in zone_file)
        # www has a TTL and a class
        self.assertTrue("www 3600 IN A 127.0.0.1" in zone_file)
        # mail has "_missing_class" set, confirm no class is output
        self.assertTrue("mail 3600 A 127.0.0.1" in zone_file)

    def test_zone_file_creation_3(self):
        json_zone_file = zone_file_objects["sample_3"]
        zone_file = make_zone_file(json_zone_file)
        print(zone_file)
        self.assertTrue(isinstance(zone_file, (str, bytes)))
        self.assertTrue("$ORIGIN" in zone_file)
        self.assertTrue("$TTL" in zone_file)
        self.assertTrue("@ IN SOA" in zone_file)

    def test_zone_file_parsing_1(self):
        zone_file = parse_zone_file(zone_files["sample_1"])
        print(json.dumps(zone_file, indent=2))
        self.assertTrue(isinstance(zone_file, dict))
        self.assertTrue("a" in zone_file)
        self.assertTrue("cname" in zone_file)
        self.assertTrue("alias" in zone_file)
        self.assertTrue("mx" in zone_file)
        self.assertTrue("$ttl" in zone_file)
        self.assertTrue("$origin" in zone_file)

    def test_zone_file_parsing_2(self):
        zone_file = parse_zone_file(zone_files["sample_2"])
        # print(json.dumps(zone_file, indent=2))
        self.assertTrue(isinstance(zone_file, dict))
        self.assertTrue("a" in zone_file)
        self.assertTrue("cname" in zone_file)
        self.assertTrue("alias" in zone_file)
        self.assertTrue("$ttl" in zone_file)
        self.assertTrue("$origin" in zone_file)

        a_records = {record["name"]: record for record in zone_file["a"]}
        # Confirm that all records have class "IN"
        self.assertTrue(all([(record["class"] == "IN") for record in a_records.values()]))
        # TTL and no CLASS
        self.assertEqual(a_records["server1"].get("_missing_class"), True)
        # CLASS and no TTL
        self.assertEqual(a_records["server2"].get("_missing_class"), None)
        # TTL and no CLASS
        self.assertEqual(a_records["server3"].get("ttl"), 3600)
        self.assertEqual(a_records["server3"].get("_missing_class"), True)
        # TTL and CLASS
        self.assertEqual(a_records["dns1"].get("ttl"), 3600)
        self.assertEqual(a_records["dns1"].get("_missing_class"), None)
        # Reversed TTL and CLASS field order
        self.assertEqual(a_records["dns2"].get("ttl"), 3600)
        self.assertEqual(a_records["dns2"].get("_missing_class"), None)

    def test_zone_file_parsing_3(self):
        zone_file = parse_zone_file(zone_files["sample_3"])
        # print(json.dumps(zone_file, indent=2))
        self.assertTrue(isinstance(zone_file, dict))
        self.assertTrue("soa" in zone_file)
        self.assertTrue("mx" in zone_file)
        self.assertTrue("ns" in zone_file)
        self.assertTrue("a" in zone_file)
        self.assertTrue("cname" in zone_file)
        self.assertTrue("alias" in zone_file)
        self.assertTrue("$ttl" in zone_file)
        self.assertTrue("$origin" in zone_file)


def test_main():
    support.run_unittest(
        ZoneFileTests
    )


if __name__ == '__main__':
    test_main()
