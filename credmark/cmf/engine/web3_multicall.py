# pylint:disable=protected-access

import logging
from dataclasses import dataclass
from typing import Any, Iterator, Sequence, TypeVar, cast

from eth_abi.exceptions import DecodingError
from eth_typing import ChecksumAddress
from hexbytes import HexBytes
from web3._utils.abi import map_abi_data
from web3._utils.normalizers import BASE_RETURN_NORMALIZERS
from web3.contract.contract import Contract, ContractFunction
from web3.exceptions import BadFunctionCallOutput, ContractLogicError

import credmark.cmf.model
from credmark.cmf.model.errors import ModelEngineError
from credmark.cmf.types.network import Network, NetworkDict

# pylint: disable=line-too-long
MULTICALL_V3_ABI = '[{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"aggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes[]","name":"returnData","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bool","name":"allowFailure","type":"bool"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call3[]","name":"calls","type":"tuple[]"}],"name":"aggregate3","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bool","name":"allowFailure","type":"bool"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call3Value[]","name":"calls","type":"tuple[]"}],"name":"aggregate3Value","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"blockAndAggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes32","name":"blockHash","type":"bytes32"},{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getBasefee","outputs":[{"internalType":"uint256","name":"basefee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getBlockHash","outputs":[{"internalType":"bytes32","name":"blockHash","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBlockNumber","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getChainId","outputs":[{"internalType":"uint256","name":"chainid","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockCoinbase","outputs":[{"internalType":"address","name":"coinbase","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockDifficulty","outputs":[{"internalType":"uint256","name":"difficulty","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockGasLimit","outputs":[{"internalType":"uint256","name":"gaslimit","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockTimestamp","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"getEthBalance","outputs":[{"internalType":"uint256","name":"balance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLastBlockHash","outputs":[{"internalType":"bytes32","name":"blockHash","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"requireSuccess","type":"bool"},{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"tryAggregate","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bool","name":"requireSuccess","type":"bool"},{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"tryBlockAndAggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes32","name":"blockHash","type":"bytes32"},{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"}]'
# pylint: disable=line-too-long
MULTICALL_V3_BYTECODE = b"`\x80`@R4\x80\x15a\x00\x10W`\x00\x80\xfd[Pa\x0e\xe0\x80a\x00 `\x009`\x00\xf3\xfe`\x80`@R`\x046\x10a\x00\xf3W`\x005`\xe0\x1c\x80cM#\x01\xcc\x11a\x00\x8aW\x80c\xa8\xb0WN\x11a\x00YW\x80c\xa8\xb0WN\x14a\x02ZW\x80c\xbc\xe3\x8b\xd7\x14a\x02uW\x80c\xc3\x07\x7f\xa9\x14a\x02\x88W\x80c\xee\x82\xac^\x14a\x02\x9bW`\x00\x80\xfd[\x80cM#\x01\xcc\x14a\x01\xecW\x80crB]\x9d\x14a\x02!W\x80c\x82\xadV\xcb\x14a\x024W\x80c\x86\xd5\x16\xe8\x14a\x02GW`\x00\x80\xfd[\x80c4\x08\xe4p\x11a\x00\xc6W\x80c4\x08\xe4p\x14a\x01\x91W\x80c9\x95B\xe9\x14a\x01\xa4W\x80c>d\xa6\x96\x14a\x01\xc6W\x80cB\xcb\xb1\\\x14a\x01\xd9W`\x00\x80\xfd[\x80c\x0f(\xc9}\x14a\x00\xf8W\x80c\x17M\xeaq\x14a\x01\x1aW\x80c%-\xbaB\x14a\x01:W\x80c'\xe8mn\x14a\x01[W[`\x00\x80\xfd[4\x80\x15a\x01\x04W`\x00\x80\xfd[PB[`@Q\x90\x81R` \x01[`@Q\x80\x91\x03\x90\xf3[a\x01-a\x01(6`\x04a\n\x85V[a\x02\xbaV[`@Qa\x01\x11\x91\x90a\x0b\xbeV[a\x01Ma\x01H6`\x04a\n\x85V[a\x04\xefV[`@Qa\x01\x11\x92\x91\x90a\x0b\xd8V[4\x80\x15a\x01gW`\x00\x80\xfd[PC\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01@a\x01\x07V[4\x80\x15a\x01\x9dW`\x00\x80\xfd[PFa\x01\x07V[a\x01\xb7a\x01\xb26`\x04a\x0c`V[a\x06\x90V[`@Qa\x01\x11\x93\x92\x91\x90a\x0c\xbaV[4\x80\x15a\x01\xd2W`\x00\x80\xfd[PHa\x01\x07V[4\x80\x15a\x01\xe5W`\x00\x80\xfd[PCa\x01\x07V[4\x80\x15a\x01\xf8W`\x00\x80\xfd[Pa\x01\x07a\x02\x076`\x04a\x0c\xe2V[s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x161\x90V[4\x80\x15a\x02-W`\x00\x80\xfd[PDa\x01\x07V[a\x01-a\x02B6`\x04a\n\x85V[a\x06\xabV[4\x80\x15a\x02SW`\x00\x80\xfd[PEa\x01\x07V[4\x80\x15a\x02fW`\x00\x80\xfd[P`@QA\x81R` \x01a\x01\x11V[a\x01-a\x02\x836`\x04a\x0c`V[a\x08ZV[a\x01\xb7a\x02\x966`\x04a\n\x85V[a\n\x1aV[4\x80\x15a\x02\xa7W`\x00\x80\xfd[Pa\x01\x07a\x02\xb66`\x04a\r\x18V[@\x90V[```\x00\x82\x80g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\x02\xd8Wa\x02\xd8a\r1V[`@Q\x90\x80\x82R\x80` \x02` \x01\x82\x01`@R\x80\x15a\x03\x1eW\x81` \x01[`@\x80Q\x80\x82\x01\x90\x91R`\x00\x81R``` \x82\x01R\x81R` \x01\x90`\x01\x90\x03\x90\x81a\x02\xf6W\x90P[P\x92P6`\x00[\x82\x81\x10\x15a\x04wW`\x00\x85\x82\x81Q\x81\x10a\x03AWa\x03Aa\r`V[` \x02` \x01\x01Q\x90P\x87\x87\x83\x81\x81\x10a\x03]Wa\x03]a\r`V[\x90P` \x02\x81\x01\x90a\x03o\x91\x90a\r\x8fV[`@\x81\x015\x95\x86\x01\x95\x90\x93Pa\x03\x88` \x85\x01\x85a\x0c\xe2V[s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16\x81a\x03\xac``\x87\x01\x87a\r\xcdV[`@Qa\x03\xba\x92\x91\x90a\x0e2V[`\x00`@Q\x80\x83\x03\x81\x85\x87Z\xf1\x92PPP=\x80`\x00\x81\x14a\x03\xf7W`@Q\x91P`\x1f\x19`?=\x01\x16\x82\x01`@R=\x82R=`\x00` \x84\x01>a\x03\xfcV[``\x91P[P` \x80\x85\x01\x91\x90\x91R\x90\x15\x15\x80\x84R\x90\x85\x015\x17a\x04mW\x7f\x08\xc3y\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00R` `\x04R`\x17`$R\x7fMulticall3: call failed\x00\x00\x00\x00\x00\x00\x00\x00\x00`DR`\x84`\x00\xfd[PP`\x01\x01a\x03%V[P\x824\x14a\x04\xe6W`@Q\x7f\x08\xc3y\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x81R` `\x04\x82\x01R`\x1a`$\x82\x01R\x7fMulticall3: value mismatch\x00\x00\x00\x00\x00\x00`D\x82\x01R`d\x01[`@Q\x80\x91\x03\x90\xfd[PPP\x92\x91PPV[C``\x82\x80g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\x05\x0cWa\x05\x0ca\r1V[`@Q\x90\x80\x82R\x80` \x02` \x01\x82\x01`@R\x80\x15a\x05?W\x81` \x01[``\x81R` \x01\x90`\x01\x90\x03\x90\x81a\x05*W\x90P[P\x91P6`\x00[\x82\x81\x10\x15a\x06\x86W`\x00\x87\x87\x83\x81\x81\x10a\x05bWa\x05ba\r`V[\x90P` \x02\x81\x01\x90a\x05t\x91\x90a\x0eBV[\x92Pa\x05\x83` \x84\x01\x84a\x0c\xe2V[s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16a\x05\xa6` \x85\x01\x85a\r\xcdV[`@Qa\x05\xb4\x92\x91\x90a\x0e2V[`\x00`@Q\x80\x83\x03\x81`\x00\x86Z\xf1\x91PP=\x80`\x00\x81\x14a\x05\xf1W`@Q\x91P`\x1f\x19`?=\x01\x16\x82\x01`@R=\x82R=`\x00` \x84\x01>a\x05\xf6V[``\x91P[P\x86\x84\x81Q\x81\x10a\x06\tWa\x06\ta\r`V[` \x90\x81\x02\x91\x90\x91\x01\x01R\x90P\x80a\x06}W`@Q\x7f\x08\xc3y\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x81R` `\x04\x82\x01R`\x17`$\x82\x01R\x7fMulticall3: call failed\x00\x00\x00\x00\x00\x00\x00\x00\x00`D\x82\x01R`d\x01a\x04\xddV[P`\x01\x01a\x05FV[PPP\x92P\x92\x90PV[C\x80@``a\x06\xa0\x86\x86\x86a\x08ZV[\x90P\x93P\x93P\x93\x90PV[``\x81\x80g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\x06\xc7Wa\x06\xc7a\r1V[`@Q\x90\x80\x82R\x80` \x02` \x01\x82\x01`@R\x80\x15a\x07\rW\x81` \x01[`@\x80Q\x80\x82\x01\x90\x91R`\x00\x81R``` \x82\x01R\x81R` \x01\x90`\x01\x90\x03\x90\x81a\x06\xe5W\x90P[P\x91P6`\x00[\x82\x81\x10\x15a\x04\xe6W`\x00\x84\x82\x81Q\x81\x10a\x070Wa\x070a\r`V[` \x02` \x01\x01Q\x90P\x86\x86\x83\x81\x81\x10a\x07LWa\x07La\r`V[\x90P` \x02\x81\x01\x90a\x07^\x91\x90a\x0evV[\x92Pa\x07m` \x84\x01\x84a\x0c\xe2V[s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16a\x07\x90`@\x85\x01\x85a\r\xcdV[`@Qa\x07\x9e\x92\x91\x90a\x0e2V[`\x00`@Q\x80\x83\x03\x81`\x00\x86Z\xf1\x91PP=\x80`\x00\x81\x14a\x07\xdbW`@Q\x91P`\x1f\x19`?=\x01\x16\x82\x01`@R=\x82R=`\x00` \x84\x01>a\x07\xe0V[``\x91P[P` \x80\x84\x01\x91\x90\x91R\x90\x15\x15\x80\x83R\x90\x84\x015\x17a\x08QW\x7f\x08\xc3y\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00R` `\x04R`\x17`$R\x7fMulticall3: call failed\x00\x00\x00\x00\x00\x00\x00\x00\x00`DR`d`\x00\xfd[P`\x01\x01a\x07\x14V[``\x81\x80g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\x08vWa\x08va\r1V[`@Q\x90\x80\x82R\x80` \x02` \x01\x82\x01`@R\x80\x15a\x08\xbcW\x81` \x01[`@\x80Q\x80\x82\x01\x90\x91R`\x00\x81R``` \x82\x01R\x81R` \x01\x90`\x01\x90\x03\x90\x81a\x08\x94W\x90P[P\x91P6`\x00[\x82\x81\x10\x15a\n\x10W`\x00\x84\x82\x81Q\x81\x10a\x08\xdfWa\x08\xdfa\r`V[` \x02` \x01\x01Q\x90P\x86\x86\x83\x81\x81\x10a\x08\xfbWa\x08\xfba\r`V[\x90P` \x02\x81\x01\x90a\t\r\x91\x90a\x0eBV[\x92Pa\t\x1c` \x84\x01\x84a\x0c\xe2V[s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16a\t?` \x85\x01\x85a\r\xcdV[`@Qa\tM\x92\x91\x90a\x0e2V[`\x00`@Q\x80\x83\x03\x81`\x00\x86Z\xf1\x91PP=\x80`\x00\x81\x14a\t\x8aW`@Q\x91P`\x1f\x19`?=\x01\x16\x82\x01`@R=\x82R=`\x00` \x84\x01>a\t\x8fV[``\x91P[P` \x83\x01R\x15\x15\x81R\x87\x15a\n\x07W\x80Qa\n\x07W`@Q\x7f\x08\xc3y\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x81R` `\x04\x82\x01R`\x17`$\x82\x01R\x7fMulticall3: call failed\x00\x00\x00\x00\x00\x00\x00\x00\x00`D\x82\x01R`d\x01a\x04\xddV[P`\x01\x01a\x08\xc3V[PPP\x93\x92PPPV[`\x00\x80``a\n+`\x01\x86\x86a\x06\x90V[\x91\x97\x90\x96P\x90\x94P\x92PPPV[`\x00\x80\x83`\x1f\x84\x01\x12a\nKW`\x00\x80\xfd[P\x815g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\ncW`\x00\x80\xfd[` \x83\x01\x91P\x83` \x82`\x05\x1b\x85\x01\x01\x11\x15a\n~W`\x00\x80\xfd[\x92P\x92\x90PV[`\x00\x80` \x83\x85\x03\x12\x15a\n\x98W`\x00\x80\xfd[\x825g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\n\xafW`\x00\x80\xfd[a\n\xbb\x85\x82\x86\x01a\n9V[\x90\x96\x90\x95P\x93PPPPV[`\x00\x81Q\x80\x84R`\x00[\x81\x81\x10\x15a\n\xedW` \x81\x85\x01\x81\x01Q\x86\x83\x01\x82\x01R\x01a\n\xd1V[\x81\x81\x11\x15a\n\xffW`\x00` \x83\x87\x01\x01R[P`\x1f\x01\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x16\x92\x90\x92\x01` \x01\x92\x91PPV[`\x00\x82\x82Q\x80\x85R` \x80\x86\x01\x95P\x80\x82`\x05\x1b\x84\x01\x01\x81\x86\x01`\x00[\x84\x81\x10\x15a\x0b\xb1W\x85\x83\x03\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x01\x89R\x81Q\x80Q\x15\x15\x84R\x84\x01Q`@\x85\x85\x01\x81\x90Ra\x0b\x9d\x81\x86\x01\x83a\n\xc7V[\x9a\x86\x01\x9a\x94PPP\x90\x83\x01\x90`\x01\x01a\x0bOV[P\x90\x97\x96PPPPPPPV[` \x81R`\x00a\x0b\xd1` \x83\x01\x84a\x0b2V[\x93\x92PPPV[`\x00`@\x82\x01\x84\x83R` `@\x81\x85\x01R\x81\x85Q\x80\x84R``\x86\x01\x91P``\x81`\x05\x1b\x87\x01\x01\x93P\x82\x87\x01`\x00[\x82\x81\x10\x15a\x0cRW\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xa0\x88\x87\x03\x01\x84Ra\x0c@\x86\x83Qa\n\xc7V[\x95P\x92\x84\x01\x92\x90\x84\x01\x90`\x01\x01a\x0c\x06V[P\x93\x98\x97PPPPPPPPV[`\x00\x80`\x00`@\x84\x86\x03\x12\x15a\x0cuW`\x00\x80\xfd[\x835\x80\x15\x15\x81\x14a\x0c\x85W`\x00\x80\xfd[\x92P` \x84\x015g\xff\xff\xff\xff\xff\xff\xff\xff\x81\x11\x15a\x0c\xa1W`\x00\x80\xfd[a\x0c\xad\x86\x82\x87\x01a\n9V[\x94\x97\x90\x96P\x93\x94PPPPV[\x83\x81R\x82` \x82\x01R```@\x82\x01R`\x00a\x0c\xd9``\x83\x01\x84a\x0b2V[\x95\x94PPPPPV[`\x00` \x82\x84\x03\x12\x15a\x0c\xf4W`\x00\x80\xfd[\x815s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x81\x16\x81\x14a\x0b\xd1W`\x00\x80\xfd[`\x00` \x82\x84\x03\x12\x15a\r*W`\x00\x80\xfd[P5\x91\x90PV[\x7fNH{q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00R`A`\x04R`$`\x00\xfd[\x7fNH{q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00R`2`\x04R`$`\x00\xfd[`\x00\x825\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x81\x836\x03\x01\x81\x12a\r\xc3W`\x00\x80\xfd[\x91\x90\x91\x01\x92\x91PPV[`\x00\x80\x835\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe1\x846\x03\x01\x81\x12a\x0e\x02W`\x00\x80\xfd[\x83\x01\x805\x91Pg\xff\xff\xff\xff\xff\xff\xff\xff\x82\x11\x15a\x0e\x1dW`\x00\x80\xfd[` \x01\x91P6\x81\x90\x03\x82\x13\x15a\n~W`\x00\x80\xfd[\x81\x83\x827`\x00\x91\x01\x90\x81R\x91\x90PV[`\x00\x825\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc1\x836\x03\x01\x81\x12a\r\xc3W`\x00\x80\xfd[`\x00\x825\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xa1\x836\x03\x01\x81\x12a\r\xc3W`\x00\x80\xfd\xfe\xa2dipfsX\"\x12 \xbb+\\q\xa3(\x03/\x97\xc6v\xae9\xa1\xec!H\xd3\xe5\xd6\xf7=\x95\xe9\xb1y\x10\x15-a\xf1bdsolcC\x00\x08\x0c\x003"

logger = logging.getLogger(__name__)


@dataclass
class MulticallResult:
    success: bool
    return_data: bytes


@dataclass
class MulticallDecodedResult:
    success: bool
    return_data_decoded: Any

    def unwrap(self, replace_with: Any = None) -> Any:
        if replace_with:
            return self.return_data_decoded if self.success else replace_with
        if not self.success:
            raise ModelEngineError("Multicall function failed")
        return self.return_data_decoded


# https://github.com/mds1/multicall#deployments
MULTICALL_CONTRACTS = NetworkDict(lambda: "0xcA11bde05977b3631167028862bE2a173976CA11", {
    Network.Mainnet: "0xcA11bde05977b3631167028862bE2a173976CA11",
    Network.Ropsten: "0xcA11bde05977b3631167028862bE2a173976CA11",
    Network.Rinkeby: "0xcA11bde05977b3631167028862bE2a173976CA11",
    Network.Görli: "0xcA11bde05977b3631167028862bE2a173976CA11",
    Network.Optimism: "0xcA11bde05977b3631167028862bE2a173976CA11",
    Network.Kovan: "0xcA11bde05977b3631167028862bE2a173976CA11",
    Network.BSC: "0xcA11bde05977b3631167028862bE2a173976CA11",
    Network.Polygon: "0xcA11bde05977b3631167028862bE2a173976CA11",
    Network.Fantom: "0xcA11bde05977b3631167028862bE2a173976CA11",
    Network.ArbitrumOne: "0xcA11bde05977b3631167028862bE2a173976CA11",
    Network.Avalanche: "0xcA11bde05977b3631167028862bE2a173976CA11",
})

MULTICALL_DEPLOYMENT = NetworkDict(lambda: "0xcA11bde05977b3631167028862bE2a173976CA11", {
    Network.Mainnet: 14353601,
    Network.Optimism: 4286263,
    Network.ArbitrumOne: 7654707,
})

T = TypeVar("T")


def divide_chunks(big_list: Sequence[T], chunk_size: int) -> Iterator[Sequence[T]]:
    for i in range(0, len(big_list), chunk_size):
        yield big_list[i:i + chunk_size]


class Web3Multicall:
    _contract: Contract | None = None

    @property
    def contract(self) -> Contract:
        context = credmark.cmf.model.ModelContext.current_context()
        if self._contract is not None:
            if (self._contract.w3.eth.chain_id != context.chain_id
                    or self._contract.w3.eth.default_block != context.block_number):
                self._contract = None

        if self._contract is None:
            address = cast(ChecksumAddress,
                           MULTICALL_CONTRACTS.get(context.network))
            self._contract = context.web3.eth.contract(
                address=context.web3.to_checksum_address(address),
                abi=MULTICALL_V3_ABI, bytecode=MULTICALL_V3_BYTECODE
            )

        return self._contract

    @staticmethod
    def _build_payload(
        contract_functions: Sequence[ContractFunction],
    ) -> tuple[list[tuple[ChecksumAddress, bytes]], list[list[Any]]]:
        targets_with_data = []
        output_types = []
        for contract_function in contract_functions:
            targets_with_data.append(
                (
                    contract_function.address,
                    HexBytes(contract_function._encode_transaction_data()
                             ),
                )
            )

            outputs = contract_function.abi["outputs"] if "outputs" in contract_function.abi else [
            ]
            output_types.append(
                [output["type"] if "type" in output else None for output in outputs]
            )

        return targets_with_data, output_types

    def _build_payload_same_function(
        self,
        tx_data: HexBytes,
        contract_addresses: Sequence[ChecksumAddress],
    ) -> list[tuple[ChecksumAddress, bytes]]:
        targets_with_data = []
        for contract_address in contract_addresses:
            targets_with_data.append((contract_address, tx_data))

        return targets_with_data

    def _decode_data(self,
                     contract_function: ContractFunction,
                     output_types: Sequence[str],
                     return_data: bytes):
        w3 = self.contract.w3
        function_identifier = contract_function.function_identifier
        try:
            output_data = w3.codec.decode(output_types, return_data)
        except DecodingError as e:
            msg = (
                f"Could not decode contract function call to {function_identifier} "
                f"with return data: {str(return_data)}, output_types: {output_types}"
            )

            raise BadFunctionCallOutput(msg) from e

        normalized_data = map_abi_data(
            BASE_RETURN_NORMALIZERS, output_types, output_data)

        if len(normalized_data) == 1:
            return normalized_data[0]
        else:
            return normalized_data

    def _try_aggregate(
        self,
        targets_with_data: Sequence[tuple[ChecksumAddress, bytes]],
        require_success: bool = False,
    ) -> list[MulticallResult]:
        aggregate_parameter = [
            {"target": target, "callData": data} for target, data in targets_with_data
        ]
        try:
            result = self.contract.functions.tryAggregate(
                require_success, aggregate_parameter
            ).call()

            if require_success and b"" in (data for _, data in result):
                # `b''` values are decoding errors/missing contracts/missing functions
                raise ModelEngineError("Multicall function failed")

            return [
                MulticallResult(success, data)
                for success, data in result
            ]
        except (ContractLogicError, OverflowError, ValueError) as err:
            raise ModelEngineError("Multicall function failed") from err

    @property
    def is_deployed(self) -> bool:
        context = credmark.cmf.model.ModelContext.current_context()
        deployment = MULTICALL_DEPLOYMENT.get(context.network)
        if deployment is None:
            return True
        return self.contract.w3.eth.default_block >= deployment

    def run_sequence(self, contract_functions: Sequence[ContractFunction], require_success) -> list[MulticallDecodedResult]:
        results = []
        for contract_function in contract_functions:
            try:
                result = contract_function.call()
                results.append(MulticallDecodedResult(True, result))
            except (ContractLogicError, OverflowError, ValueError) as err:
                if require_success:
                    raise ModelEngineError(
                        "Multicall function failed") from err
                results.append(MulticallDecodedResult(False, None))
        return results

    def try_aggregate(
        self,
        contract_functions: Sequence[ContractFunction],
        *,
        require_success: bool = False,
        batch_size: int = 100,
    ) -> list[MulticallDecodedResult]:
        if not self.is_deployed:
            return self.run_sequence(contract_functions, require_success)
        result: list[MulticallDecodedResult] = []
        for chunk in divide_chunks(contract_functions, batch_size):
            targets_with_data, output_types = self._build_payload(chunk)
            results = self._try_aggregate(
                targets_with_data,
                require_success=require_success,
            )

            for idx, (output_type, multicall_result) in enumerate(zip(output_types, results)):
                contract_function = contract_functions[idx]
                success = multicall_result.success
                try:
                    data = self._decode_data(
                        contract_function, output_type, multicall_result.return_data) \
                        if multicall_result.success \
                        else multicall_result.return_data
                except BadFunctionCallOutput:
                    success = False
                    data = multicall_result.return_data
                result.append(MulticallDecodedResult(
                    success,
                    data,
                ))

        return result

    def try_aggregate_unwrap(
            self,
            contract_functions: Sequence[ContractFunction],
            *,
            require_success: bool = False,
            batch_size: int = 100,
            replace_with: Any = None):
        return [x.unwrap(replace_with) for x in self.try_aggregate(
            contract_functions, require_success=require_success, batch_size=batch_size)]

    # pylint:disable=too-many-locals
    def try_aggregate_same_function(
        self,
        contract_function: ContractFunction,
        contract_addresses: Sequence[ChecksumAddress],
        *,
        require_success: bool = False,
        batch_size: int = 100,
        fallback_contract_function: ContractFunction | None = None,
    ) -> list[MulticallDecodedResult]:
        result: list[MulticallDecodedResult] = []

        tx_data = HexBytes(contract_function._encode_transaction_data(
        ))  # pylint:disable=protected-access
        outputs = contract_function.abi["outputs"] if "outputs" in contract_function.abi else [
        ]
        output_type = [output["type"]
                       for output in outputs if "type" in output]

        for chunk in divide_chunks(contract_addresses, batch_size):
            for multicall_result in self._try_aggregate(
                self._build_payload_same_function(tx_data, chunk),
                require_success=False if fallback_contract_function else require_success,
            ):
                success = multicall_result.success
                try:
                    data = self._decode_data(
                        contract_function, output_type, multicall_result.return_data) \
                        if multicall_result.success \
                        else multicall_result.return_data
                except BadFunctionCallOutput:
                    success = False
                    data = multicall_result.return_data
                result.append(MulticallDecodedResult(
                    success,
                    data,
                ))

        failed = [(idx, contract_addresses[idx])
                  for idx, decoded_result in enumerate(result) if not decoded_result.success]

        if not failed or not fallback_contract_function:
            return result

        fallback_results = self.try_aggregate_same_function(
            fallback_contract_function,
            [address for (_, address) in failed],
            require_success=require_success,
            batch_size=batch_size)

        for idx, fallback_result in enumerate(fallback_results):
            result[failed[idx][0]] = fallback_result

        return result

    def try_aggregate_same_function_unwrap(
            self,
            contract_function: ContractFunction,
            contract_addresses: Sequence[ChecksumAddress],
            *,
            require_success: bool = False,
            batch_size: int = 100,
            fallback_contract_function: ContractFunction | None = None):
        return [x.unwrap() for x in self.try_aggregate_same_function(
            contract_function,
            contract_addresses,
            require_success=require_success,
            batch_size=batch_size,
            fallback_contract_function=fallback_contract_function,
        )]
