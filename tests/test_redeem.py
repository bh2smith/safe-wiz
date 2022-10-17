import unittest

from eth_typing import URI
from gnosis.eth import EthereumClient

from src.airdrop.allocation import Allocation
from src.airdrop.redeem import encode_redeem
from src.environment import INFURA_KEY
from src.safe import get_safe


class TestMultiSend(unittest.TestCase):
    def setUp(self) -> None:
        node_url = f"https://mainnet.infura.io/v3/{INFURA_KEY}"
        self.client = EthereumClient(URI(node_url))

    def test_fetch_and_parse_allocation_data(self):
        single_allocation = Allocation.from_address(
            "0xa1097B957A62B75482CFB9Af960Cbd6B8F9F02e8"
        )
        self.assertEqual(
            Allocation(
                tag="user",
                account="0xa1097B957A62B75482CFB9Af960Cbd6B8F9F02e8",
                chainId=1,
                contract="0xA0b937D5c8E32a80E3a8ed4227CD020221544ee6",
                vestingId="0xb7d48c91701a6b8abe620e1f8f543a3885d9570db3da7b0ae42fb320e2f3bc53",
                durationWeeks=416,
                startDate=1538042400,
                amount="1854720164105111994368",
                curve=0,
                proof=[
                    "0xe36a61615023453dd2e3b196c7eabd4b4c86fa2690e73327e727456661d7412f",
                    "0x6df65e0fca7b91a398d45fee84b8a6e45d1d353d28d8dd11b1134cdbc308113a",
                    "0x607471c45e52b1100ec7b9bdcfac945950dbdf6777c0f65b22773531ca0957c8",
                    "0xac96c9159261b22edcadb10baee2878c92427553a5dc5f6efa4327614ad15fee",
                    "0xc21e9113c866b3f5c3b3da4287ca6452a983cca497df18dd48d716143eb0fd91",
                    "0xb7457dcb21f2c1f39a8f4edf9b436e4ec349bd821587a07bbec37fb4a46166ae",
                    "0xed4aafe93ae6234aecc0c3fa5c836e2d8c9c3f579e6e2252f81a5495b616af3f",
                    "0x04081a367101d0b8f852e683c14cb04baa560a7e46b196be6781c5a7f0d527e9",
                    "0xb1f5ed5c04c9a7a56384400b25685b56e383f8f2949ce8a5f9246bb809d37ba0",
                    "0xc5112afaf9117ce34e6738b84ecf72d60414d2b4dfb0ebf9b7039bea0b0823ab",
                    "0x490ed305e00bcb700dc5defc281343d8374f82e5060303a16c39d53048d72fd2",
                    "0xc6093a1a2bd9d532b36d953dfa519abb54b8886013adb8ba3fb7d508495bdb45",
                    "0x595e955f2b50d15651e0fe5dd67f3dc482fc8ecb2b98de52fbd31e65544c40b0",
                    "0x15a9fdd60e5fde6b29363a082e3e3bb69e9e578434837e6c61aa95b3e8a509fd",
                    "0x59d69bacd790ff82f7310dd382bf3f53e885e74f5dad9b3aeb7fe96ce926ff47",
                    "0xf8e2791b9d07b3e620189a36bf17e30c874e66b205c79492a16cd5a9c5bb65b7",
                ],
            ),
            single_allocation,
        )
        multi_allocation = Allocation.from_address(
            "0x20026F06342e16415b070ae3bdB3983AF7c51C95"
        )

        self.assertEqual(
            Allocation(
                tag="user",
                account="0x20026F06342e16415b070ae3bdB3983AF7c51C95",
                chainId=1,
                contract="0xA0b937D5c8E32a80E3a8ed4227CD020221544ee6",
                vestingId="0x06a3aefe5ffffe5027c6ef050b83a7eaad7327483db9ef4fdce509af1d19fa64",
                durationWeeks=416,
                startDate=1538042400,
                amount="1757033820807298547712",
                curve=0,
                proof=[
                    "0x6aed4330bf7cef939af35d876edb8f7d739994cef4953c3c2eac9344151bb0e4",
                    "0xb26f3fd8c0901e4b5cf9884e8f05f6479622afd5ea2e5ca9c34fa7626fd85a06",
                    "0x28bb2fbd8eb3e19a0f0ee77839c7e38921b33d025f0855f716ddfba32ad87768",
                    "0x9d57d944d0cb1b51aba8b6c06c9f3a54896f6dec674cdbda35045f6b6112ff5d",
                    "0x167abea0d6fa3cc3e0b0175bfb60134b29bbfdacc20bb3144c4323d10a089474",
                    "0x09873864976ccacbe3b0295a9e5afe189bbdda1aa6e1463a133a612de4a514b8",
                    "0xa05e95e100ac40a4eea9c7d478aefa39f8c3da6622b6ea72d2cf7276e5099ba6",
                    "0x6ce17976fc6de8c85e9e144614a94ca3a33d43ad3a5d37039548a26ded8f4455",
                    "0xac3be362782e0952c559a424909d209974b68b2d11eaa02bb33f3f1cb42904e4",
                    "0x68ff2300d968ca5615bf82d4882911c39d4456f02fe83407f0660a6306b3dbc3",
                    "0x1e85606b3975a5a8523525d8bfc5793384b7cb3bb05ac19c394f571223f5e246",
                    "0x4750e2856684fec1a433554b3c3f6b9423c07ea4feb7be174ec79f5a1447398c",
                    "0x64f26ae4741f21afae2b3e930e526a91b355b74fd100ff17d5570ea8fa636552",
                    "0x531b401cf833453be5e19f3ee07df93c01947c0e49c7669d3751b2b97496f136",
                    "0x6b3e88b74da169ca93e56f322d7b2ab8416495d64a8a9f57d0ca443d995b2364",
                    "0xf8e2791b9d07b3e620189a36bf17e30c874e66b205c79492a16cd5a9c5bb65b7",
                ],
            ),
            multi_allocation,
        )

    def test_build_redeem_tx(self):
        safe = get_safe("0x20026F06342e16415b070ae3bdB3983AF7c51C95", self.client)
        tx = encode_redeem(Allocation.from_address(safe.address))
        self.assertEqual(
            """
            0xbf6213e4
            0000000000000000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000000000001a0
            000000000000000000000000000000000000000000000000000000005bacaa20
            00000000000000000000000000000000000000000000005f3fbe16dc2e600000
            00000000000000000000000000000000000000000000000000000000000000a0
            0000000000000000000000000000000000000000000000000000000000000010
            6aed4330bf7cef939af35d876edb8f7d739994cef4953c3c2eac9344151bb0e4
            b26f3fd8c0901e4b5cf9884e8f05f6479622afd5ea2e5ca9c34fa7626fd85a06
            28bb2fbd8eb3e19a0f0ee77839c7e38921b33d025f0855f716ddfba32ad87768
            9d57d944d0cb1b51aba8b6c06c9f3a54896f6dec674cdbda35045f6b6112ff5d
            167abea0d6fa3cc3e0b0175bfb60134b29bbfdacc20bb3144c4323d10a089474
            09873864976ccacbe3b0295a9e5afe189bbdda1aa6e1463a133a612de4a514b8
            a05e95e100ac40a4eea9c7d478aefa39f8c3da6622b6ea72d2cf7276e5099ba6
            6ce17976fc6de8c85e9e144614a94ca3a33d43ad3a5d37039548a26ded8f4455
            ac3be362782e0952c559a424909d209974b68b2d11eaa02bb33f3f1cb42904e4
            68ff2300d968ca5615bf82d4882911c39d4456f02fe83407f0660a6306b3dbc3
            1e85606b3975a5a8523525d8bfc5793384b7cb3bb05ac19c394f571223f5e246
            4750e2856684fec1a433554b3c3f6b9423c07ea4feb7be174ec79f5a1447398c
            64f26ae4741f21afae2b3e930e526a91b355b74fd100ff17d5570ea8fa636552
            531b401cf833453be5e19f3ee07df93c01947c0e49c7669d3751b2b97496f136
            6b3e88b74da169ca93e56f322d7b2ab8416495d64a8a9f57d0ca443d995b2364
            f8e2791b9d07b3e620189a36bf17e30c874e66b205c79492a16cd5a9c5bb65b7
            """.replace(
                "\n", ""
            ).replace(
                " ", ""
            ),
            tx.data,
        )


if __name__ == "__main__":
    unittest.main()
