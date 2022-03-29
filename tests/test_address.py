import unittest
import logging

from credmark.dto import DTO, DTOField
from credmark.types import Address
import functools

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level='DEBUG')


def expect_exception(func):
    got_exception = False
    try:
        func()
    except Exception:
        got_exception = True
    if not got_exception:
        raise ValueError


class PoolAddress(DTO):
    poolAddress: Address = DTOField(..., description='Address of Pool')


class TestStringMethods(unittest.TestCase):

    def test_run(self):
        expect_exception(
            functools.partial(PoolAddress, {'poolAddress': '0xD905e2eaeBe188fc92179b6350'})
        )

        addr1 = '0xd905e2eaebe188fc92179b6350807d8bd91db0d8'

        self.assertEqual(Address(0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8),
                         Address(0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8))

        self.assertEqual(Address(0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8),  # type: ignore
                         addr1.lower())
        self.assertEqual(Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8'), addr1.lower())
        self.assertEqual(Address(addr1).checksum, '0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')
        self.assertNotEqual(Address(addr1).checksum, '0xA905e2eaeBe188fc92179b6350807D8bd91Db0D8')
        self.assertEqual(Address('0x' + (bytes.fromhex(addr1[2:])).hex()), addr1.lower())
        self.assertEqual(Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8'),
                         Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8'))
        self.assertNotEqual(Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D9'),
                            Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8'))

        self.assertTrue(Address.valid('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8'))
        self.assertFalse(Address.valid('0xD905e2eaeBe'))

        expect_exception(
            functools.partial(Address, 123)
        )

        expect_exception(
            functools.partial(
                Address, '0x' + bytes.fromhex(
                    '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'[2:]).hex())
        )

        addr3 = '0xd905e2eaebe188fc92179b6350807d8bd91db0d8'
        self.assertEqual(hash(Address(addr3)), hash(addr3))


if __name__ == '__main__':
    unittest.main()
