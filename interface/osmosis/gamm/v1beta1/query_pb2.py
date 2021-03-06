# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmosis/gamm/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from osmosis.gamm.v1beta1 import tx_pb2 as osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2
from osmosis.gamm.v1beta1 import pool_pb2 as osmosis_dot_gamm_dot_v1beta1_dot_pool__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n osmosis/gamm/v1beta1/query.proto\x12\x14osmosis.gamm.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1dosmosis/gamm/v1beta1/tx.proto\x1a\x1fosmosis/gamm/v1beta1/pool.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\"6\n\x10QueryPoolRequest\x12\"\n\x06poolId\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\"B\n\x11QueryPoolResponse\x12-\n\x04pool\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI\"O\n\x11QueryPoolsRequest\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x81\x01\n\x12QueryPoolsResponse\x12.\n\x05pools\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x16\n\x14QueryNumPoolsRequest\"?\n\x15QueryNumPoolsResponse\x12&\n\x08numPools\x18\x01 \x01(\x04\x42\x14\xf2\xde\x1f\x10yaml:\"num_pools\"\"<\n\x16QueryPoolParamsRequest\x12\"\n\x06poolId\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\"?\n\x17QueryPoolParamsResponse\x12$\n\x06params\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"=\n\x17QueryTotalSharesRequest\x12\"\n\x06poolId\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\"g\n\x18QueryTotalSharesResponse\x12K\n\x0btotalShares\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x1b\xf2\xde\x1f\x13yaml:\"total_shares\"\xc8\xde\x1f\x00\"<\n\x16QueryPoolAssetsRequest\x12\"\n\x06poolId\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\"T\n\x17QueryPoolAssetsResponse\x12\x39\n\npoolAssets\x18\x01 \x03(\x0b\x32\x1f.osmosis.gamm.v1beta1.PoolAssetB\x04\xc8\xde\x1f\x00\"\xce\x01\n\x15QuerySpotPriceRequest\x12\"\n\x06poolId\x18\x01 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\x12/\n\x0ctokenInDenom\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:\"token_in_denom\"\x12\x31\n\rtokenOutDenom\x18\x03 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"token_out_denom\"\x12-\n\x0bwithSwapFee\x18\x04 \x01(\x08\x42\x18\xf2\xde\x1f\x14yaml:\"with_swap_fee\"\"B\n\x16QuerySpotPriceResponse\x12(\n\tspotPrice\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"spot_price\"\"\xdc\x01\n\x1dQuerySwapExactAmountInRequest\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\"\n\x06poolId\x18\x02 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\x12$\n\x07tokenIn\x18\x03 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:\"token_in\"\x12N\n\x06routes\x18\x04 \x03(\x0b\x32\'.osmosis.gamm.v1beta1.SwapAmountInRouteB\x15\xf2\xde\x1f\ryaml:\"routes\"\xc8\xde\x1f\x00\"\x83\x01\n\x1eQuerySwapExactAmountInResponse\x12\x61\n\x0etokenOutAmount\x18\x01 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:\"token_out_amount\"\xc8\xde\x1f\x00\"\xe0\x01\n\x1eQuerySwapExactAmountOutRequest\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\"\n\x06poolId\x18\x02 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\x12O\n\x06routes\x18\x03 \x03(\x0b\x32(.osmosis.gamm.v1beta1.SwapAmountOutRouteB\x15\xf2\xde\x1f\ryaml:\"routes\"\xc8\xde\x1f\x00\x12&\n\x08tokenOut\x18\x04 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"token_out\"\"\x82\x01\n\x1fQuerySwapExactAmountOutResponse\x12_\n\rtokenInAmount\x18\x01 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:\"token_in_amount\"\xc8\xde\x1f\x00\"\x1c\n\x1aQueryTotalLiquidityRequest\"\x91\x01\n\x1bQueryTotalLiquidityResponse\x12r\n\tliquidity\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBD\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x10yaml:\"liquidity\"\xc8\xde\x1f\x00\x32\xf2\x0c\n\x05Query\x12\x7f\n\x05Pools\x12\'.osmosis.gamm.v1beta1.QueryPoolsRequest\x1a(.osmosis.gamm.v1beta1.QueryPoolsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/osmosis/gamm/v1beta1/pools\x12\x8c\x01\n\x08NumPools\x12*.osmosis.gamm.v1beta1.QueryNumPoolsRequest\x1a+.osmosis.gamm.v1beta1.QueryNumPoolsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/osmosis/gamm/v1beta1/num_pools\x12\xa4\x01\n\x0eTotalLiquidity\x12\x30.osmosis.gamm.v1beta1.QueryTotalLiquidityRequest\x1a\x31.osmosis.gamm.v1beta1.QueryTotalLiquidityResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/osmosis/gamm/v1beta1/total_liquidity\x12\x85\x01\n\x04Pool\x12&.osmosis.gamm.v1beta1.QueryPoolRequest\x1a\'.osmosis.gamm.v1beta1.QueryPoolResponse\",\x82\xd3\xe4\x93\x02&\x12$/osmosis/gamm/v1beta1/pools/{poolId}\x12\x9e\x01\n\nPoolParams\x12,.osmosis.gamm.v1beta1.QueryPoolParamsRequest\x1a-.osmosis.gamm.v1beta1.QueryPoolParamsResponse\"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/gamm/v1beta1/pools/{poolId}/params\x12\xa7\x01\n\x0bTotalShares\x12-.osmosis.gamm.v1beta1.QueryTotalSharesRequest\x1a..osmosis.gamm.v1beta1.QueryTotalSharesResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/osmosis/gamm/v1beta1/pools/{poolId}/total_shares\x12\x9e\x01\n\nPoolAssets\x12,.osmosis.gamm.v1beta1.QueryPoolAssetsRequest\x1a-.osmosis.gamm.v1beta1.QueryPoolAssetsResponse\"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/gamm/v1beta1/pools/{poolId}/tokens\x12\x9b\x01\n\tSpotPrice\x12+.osmosis.gamm.v1beta1.QuerySpotPriceRequest\x1a,.osmosis.gamm.v1beta1.QuerySpotPriceResponse\"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/gamm/v1beta1/pools/{poolId}/prices\x12\xcc\x01\n\x19\x45stimateSwapExactAmountIn\x12\x33.osmosis.gamm.v1beta1.QuerySwapExactAmountInRequest\x1a\x34.osmosis.gamm.v1beta1.QuerySwapExactAmountInResponse\"D\x82\xd3\xe4\x93\x02>\x12</osmosis/gamm/v1beta1/{poolId}/estimate/swap_exact_amount_in\x12\xd0\x01\n\x1a\x45stimateSwapExactAmountOut\x12\x34.osmosis.gamm.v1beta1.QuerySwapExactAmountOutRequest\x1a\x35.osmosis.gamm.v1beta1.QuerySwapExactAmountOutResponse\"E\x82\xd3\xe4\x93\x02?\x12=/osmosis/gamm/v1beta1/{poolId}/estimate/swap_exact_amount_outB.Z,github.com/osmosis-labs/osmosis/x/gamm/typesb\x06proto3')



_QUERYPOOLREQUEST = DESCRIPTOR.message_types_by_name['QueryPoolRequest']
_QUERYPOOLRESPONSE = DESCRIPTOR.message_types_by_name['QueryPoolResponse']
_QUERYPOOLSREQUEST = DESCRIPTOR.message_types_by_name['QueryPoolsRequest']
_QUERYPOOLSRESPONSE = DESCRIPTOR.message_types_by_name['QueryPoolsResponse']
_QUERYNUMPOOLSREQUEST = DESCRIPTOR.message_types_by_name['QueryNumPoolsRequest']
_QUERYNUMPOOLSRESPONSE = DESCRIPTOR.message_types_by_name['QueryNumPoolsResponse']
_QUERYPOOLPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryPoolParamsRequest']
_QUERYPOOLPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryPoolParamsResponse']
_QUERYTOTALSHARESREQUEST = DESCRIPTOR.message_types_by_name['QueryTotalSharesRequest']
_QUERYTOTALSHARESRESPONSE = DESCRIPTOR.message_types_by_name['QueryTotalSharesResponse']
_QUERYPOOLASSETSREQUEST = DESCRIPTOR.message_types_by_name['QueryPoolAssetsRequest']
_QUERYPOOLASSETSRESPONSE = DESCRIPTOR.message_types_by_name['QueryPoolAssetsResponse']
_QUERYSPOTPRICEREQUEST = DESCRIPTOR.message_types_by_name['QuerySpotPriceRequest']
_QUERYSPOTPRICERESPONSE = DESCRIPTOR.message_types_by_name['QuerySpotPriceResponse']
_QUERYSWAPEXACTAMOUNTINREQUEST = DESCRIPTOR.message_types_by_name['QuerySwapExactAmountInRequest']
_QUERYSWAPEXACTAMOUNTINRESPONSE = DESCRIPTOR.message_types_by_name['QuerySwapExactAmountInResponse']
_QUERYSWAPEXACTAMOUNTOUTREQUEST = DESCRIPTOR.message_types_by_name['QuerySwapExactAmountOutRequest']
_QUERYSWAPEXACTAMOUNTOUTRESPONSE = DESCRIPTOR.message_types_by_name['QuerySwapExactAmountOutResponse']
_QUERYTOTALLIQUIDITYREQUEST = DESCRIPTOR.message_types_by_name['QueryTotalLiquidityRequest']
_QUERYTOTALLIQUIDITYRESPONSE = DESCRIPTOR.message_types_by_name['QueryTotalLiquidityResponse']
QueryPoolRequest = _reflection.GeneratedProtocolMessageType('QueryPoolRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPOOLREQUEST,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryPoolRequest)
  })
_sym_db.RegisterMessage(QueryPoolRequest)

QueryPoolResponse = _reflection.GeneratedProtocolMessageType('QueryPoolResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPOOLRESPONSE,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryPoolResponse)
  })
_sym_db.RegisterMessage(QueryPoolResponse)

QueryPoolsRequest = _reflection.GeneratedProtocolMessageType('QueryPoolsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPOOLSREQUEST,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryPoolsRequest)
  })
_sym_db.RegisterMessage(QueryPoolsRequest)

QueryPoolsResponse = _reflection.GeneratedProtocolMessageType('QueryPoolsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPOOLSRESPONSE,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryPoolsResponse)
  })
_sym_db.RegisterMessage(QueryPoolsResponse)

QueryNumPoolsRequest = _reflection.GeneratedProtocolMessageType('QueryNumPoolsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYNUMPOOLSREQUEST,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryNumPoolsRequest)
  })
_sym_db.RegisterMessage(QueryNumPoolsRequest)

QueryNumPoolsResponse = _reflection.GeneratedProtocolMessageType('QueryNumPoolsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYNUMPOOLSRESPONSE,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryNumPoolsResponse)
  })
_sym_db.RegisterMessage(QueryNumPoolsResponse)

QueryPoolParamsRequest = _reflection.GeneratedProtocolMessageType('QueryPoolParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPOOLPARAMSREQUEST,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryPoolParamsRequest)
  })
_sym_db.RegisterMessage(QueryPoolParamsRequest)

QueryPoolParamsResponse = _reflection.GeneratedProtocolMessageType('QueryPoolParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPOOLPARAMSRESPONSE,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryPoolParamsResponse)
  })
_sym_db.RegisterMessage(QueryPoolParamsResponse)

QueryTotalSharesRequest = _reflection.GeneratedProtocolMessageType('QueryTotalSharesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTOTALSHARESREQUEST,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryTotalSharesRequest)
  })
_sym_db.RegisterMessage(QueryTotalSharesRequest)

QueryTotalSharesResponse = _reflection.GeneratedProtocolMessageType('QueryTotalSharesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTOTALSHARESRESPONSE,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryTotalSharesResponse)
  })
_sym_db.RegisterMessage(QueryTotalSharesResponse)

QueryPoolAssetsRequest = _reflection.GeneratedProtocolMessageType('QueryPoolAssetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPOOLASSETSREQUEST,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryPoolAssetsRequest)
  })
_sym_db.RegisterMessage(QueryPoolAssetsRequest)

QueryPoolAssetsResponse = _reflection.GeneratedProtocolMessageType('QueryPoolAssetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPOOLASSETSRESPONSE,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryPoolAssetsResponse)
  })
_sym_db.RegisterMessage(QueryPoolAssetsResponse)

QuerySpotPriceRequest = _reflection.GeneratedProtocolMessageType('QuerySpotPriceRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSPOTPRICEREQUEST,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QuerySpotPriceRequest)
  })
_sym_db.RegisterMessage(QuerySpotPriceRequest)

QuerySpotPriceResponse = _reflection.GeneratedProtocolMessageType('QuerySpotPriceResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSPOTPRICERESPONSE,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QuerySpotPriceResponse)
  })
_sym_db.RegisterMessage(QuerySpotPriceResponse)

QuerySwapExactAmountInRequest = _reflection.GeneratedProtocolMessageType('QuerySwapExactAmountInRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSWAPEXACTAMOUNTINREQUEST,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QuerySwapExactAmountInRequest)
  })
_sym_db.RegisterMessage(QuerySwapExactAmountInRequest)

QuerySwapExactAmountInResponse = _reflection.GeneratedProtocolMessageType('QuerySwapExactAmountInResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSWAPEXACTAMOUNTINRESPONSE,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QuerySwapExactAmountInResponse)
  })
_sym_db.RegisterMessage(QuerySwapExactAmountInResponse)

QuerySwapExactAmountOutRequest = _reflection.GeneratedProtocolMessageType('QuerySwapExactAmountOutRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSWAPEXACTAMOUNTOUTREQUEST,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QuerySwapExactAmountOutRequest)
  })
_sym_db.RegisterMessage(QuerySwapExactAmountOutRequest)

QuerySwapExactAmountOutResponse = _reflection.GeneratedProtocolMessageType('QuerySwapExactAmountOutResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSWAPEXACTAMOUNTOUTRESPONSE,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QuerySwapExactAmountOutResponse)
  })
_sym_db.RegisterMessage(QuerySwapExactAmountOutResponse)

QueryTotalLiquidityRequest = _reflection.GeneratedProtocolMessageType('QueryTotalLiquidityRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTOTALLIQUIDITYREQUEST,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryTotalLiquidityRequest)
  })
_sym_db.RegisterMessage(QueryTotalLiquidityRequest)

QueryTotalLiquidityResponse = _reflection.GeneratedProtocolMessageType('QueryTotalLiquidityResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTOTALLIQUIDITYRESPONSE,
  '__module__' : 'osmosis.gamm.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.gamm.v1beta1.QueryTotalLiquidityResponse)
  })
_sym_db.RegisterMessage(QueryTotalLiquidityResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/osmosis-labs/osmosis/x/gamm/types'
  _QUERYPOOLREQUEST.fields_by_name['poolId']._options = None
  _QUERYPOOLREQUEST.fields_by_name['poolId']._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
  _QUERYPOOLRESPONSE.fields_by_name['pool']._options = None
  _QUERYPOOLRESPONSE.fields_by_name['pool']._serialized_options = b'\312\264-\005PoolI'
  _QUERYPOOLSRESPONSE.fields_by_name['pools']._options = None
  _QUERYPOOLSRESPONSE.fields_by_name['pools']._serialized_options = b'\312\264-\005PoolI'
  _QUERYNUMPOOLSRESPONSE.fields_by_name['numPools']._options = None
  _QUERYNUMPOOLSRESPONSE.fields_by_name['numPools']._serialized_options = b'\362\336\037\020yaml:\"num_pools\"'
  _QUERYPOOLPARAMSREQUEST.fields_by_name['poolId']._options = None
  _QUERYPOOLPARAMSREQUEST.fields_by_name['poolId']._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
  _QUERYTOTALSHARESREQUEST.fields_by_name['poolId']._options = None
  _QUERYTOTALSHARESREQUEST.fields_by_name['poolId']._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
  _QUERYTOTALSHARESRESPONSE.fields_by_name['totalShares']._options = None
  _QUERYTOTALSHARESRESPONSE.fields_by_name['totalShares']._serialized_options = b'\362\336\037\023yaml:\"total_shares\"\310\336\037\000'
  _QUERYPOOLASSETSREQUEST.fields_by_name['poolId']._options = None
  _QUERYPOOLASSETSREQUEST.fields_by_name['poolId']._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
  _QUERYPOOLASSETSRESPONSE.fields_by_name['poolAssets']._options = None
  _QUERYPOOLASSETSRESPONSE.fields_by_name['poolAssets']._serialized_options = b'\310\336\037\000'
  _QUERYSPOTPRICEREQUEST.fields_by_name['poolId']._options = None
  _QUERYSPOTPRICEREQUEST.fields_by_name['poolId']._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
  _QUERYSPOTPRICEREQUEST.fields_by_name['tokenInDenom']._options = None
  _QUERYSPOTPRICEREQUEST.fields_by_name['tokenInDenom']._serialized_options = b'\362\336\037\025yaml:\"token_in_denom\"'
  _QUERYSPOTPRICEREQUEST.fields_by_name['tokenOutDenom']._options = None
  _QUERYSPOTPRICEREQUEST.fields_by_name['tokenOutDenom']._serialized_options = b'\362\336\037\026yaml:\"token_out_denom\"'
  _QUERYSPOTPRICEREQUEST.fields_by_name['withSwapFee']._options = None
  _QUERYSPOTPRICEREQUEST.fields_by_name['withSwapFee']._serialized_options = b'\362\336\037\024yaml:\"with_swap_fee\"'
  _QUERYSPOTPRICERESPONSE.fields_by_name['spotPrice']._options = None
  _QUERYSPOTPRICERESPONSE.fields_by_name['spotPrice']._serialized_options = b'\362\336\037\021yaml:\"spot_price\"'
  _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['sender']._options = None
  _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['poolId']._options = None
  _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['poolId']._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
  _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['tokenIn']._options = None
  _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['tokenIn']._serialized_options = b'\362\336\037\017yaml:\"token_in\"'
  _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['routes']._options = None
  _QUERYSWAPEXACTAMOUNTINREQUEST.fields_by_name['routes']._serialized_options = b'\362\336\037\ryaml:\"routes\"\310\336\037\000'
  _QUERYSWAPEXACTAMOUNTINRESPONSE.fields_by_name['tokenOutAmount']._options = None
  _QUERYSWAPEXACTAMOUNTINRESPONSE.fields_by_name['tokenOutAmount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\027yaml:\"token_out_amount\"\310\336\037\000'
  _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['sender']._options = None
  _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['poolId']._options = None
  _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['poolId']._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
  _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['routes']._options = None
  _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['routes']._serialized_options = b'\362\336\037\ryaml:\"routes\"\310\336\037\000'
  _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['tokenOut']._options = None
  _QUERYSWAPEXACTAMOUNTOUTREQUEST.fields_by_name['tokenOut']._serialized_options = b'\362\336\037\020yaml:\"token_out\"'
  _QUERYSWAPEXACTAMOUNTOUTRESPONSE.fields_by_name['tokenInAmount']._options = None
  _QUERYSWAPEXACTAMOUNTOUTRESPONSE.fields_by_name['tokenInAmount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\026yaml:\"token_in_amount\"\310\336\037\000'
  _QUERYTOTALLIQUIDITYRESPONSE.fields_by_name['liquidity']._options = None
  _QUERYTOTALLIQUIDITYRESPONSE.fields_by_name['liquidity']._serialized_options = b'\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\020yaml:\"liquidity\"\310\336\037\000'
  _QUERY.methods_by_name['Pools']._options = None
  _QUERY.methods_by_name['Pools']._serialized_options = b'\202\323\344\223\002\035\022\033/osmosis/gamm/v1beta1/pools'
  _QUERY.methods_by_name['NumPools']._options = None
  _QUERY.methods_by_name['NumPools']._serialized_options = b'\202\323\344\223\002!\022\037/osmosis/gamm/v1beta1/num_pools'
  _QUERY.methods_by_name['TotalLiquidity']._options = None
  _QUERY.methods_by_name['TotalLiquidity']._serialized_options = b'\202\323\344\223\002\'\022%/osmosis/gamm/v1beta1/total_liquidity'
  _QUERY.methods_by_name['Pool']._options = None
  _QUERY.methods_by_name['Pool']._serialized_options = b'\202\323\344\223\002&\022$/osmosis/gamm/v1beta1/pools/{poolId}'
  _QUERY.methods_by_name['PoolParams']._options = None
  _QUERY.methods_by_name['PoolParams']._serialized_options = b'\202\323\344\223\002-\022+/osmosis/gamm/v1beta1/pools/{poolId}/params'
  _QUERY.methods_by_name['TotalShares']._options = None
  _QUERY.methods_by_name['TotalShares']._serialized_options = b'\202\323\344\223\0023\0221/osmosis/gamm/v1beta1/pools/{poolId}/total_shares'
  _QUERY.methods_by_name['PoolAssets']._options = None
  _QUERY.methods_by_name['PoolAssets']._serialized_options = b'\202\323\344\223\002-\022+/osmosis/gamm/v1beta1/pools/{poolId}/tokens'
  _QUERY.methods_by_name['SpotPrice']._options = None
  _QUERY.methods_by_name['SpotPrice']._serialized_options = b'\202\323\344\223\002-\022+/osmosis/gamm/v1beta1/pools/{poolId}/prices'
  _QUERY.methods_by_name['EstimateSwapExactAmountIn']._options = None
  _QUERY.methods_by_name['EstimateSwapExactAmountIn']._serialized_options = b'\202\323\344\223\002>\022</osmosis/gamm/v1beta1/{poolId}/estimate/swap_exact_amount_in'
  _QUERY.methods_by_name['EstimateSwapExactAmountOut']._options = None
  _QUERY.methods_by_name['EstimateSwapExactAmountOut']._serialized_options = b'\202\323\344\223\002?\022=/osmosis/gamm/v1beta1/{poolId}/estimate/swap_exact_amount_out'
  _QUERYPOOLREQUEST._serialized_start=304
  _QUERYPOOLREQUEST._serialized_end=358
  _QUERYPOOLRESPONSE._serialized_start=360
  _QUERYPOOLRESPONSE._serialized_end=426
  _QUERYPOOLSREQUEST._serialized_start=428
  _QUERYPOOLSREQUEST._serialized_end=507
  _QUERYPOOLSRESPONSE._serialized_start=510
  _QUERYPOOLSRESPONSE._serialized_end=639
  _QUERYNUMPOOLSREQUEST._serialized_start=641
  _QUERYNUMPOOLSREQUEST._serialized_end=663
  _QUERYNUMPOOLSRESPONSE._serialized_start=665
  _QUERYNUMPOOLSRESPONSE._serialized_end=728
  _QUERYPOOLPARAMSREQUEST._serialized_start=730
  _QUERYPOOLPARAMSREQUEST._serialized_end=790
  _QUERYPOOLPARAMSRESPONSE._serialized_start=792
  _QUERYPOOLPARAMSRESPONSE._serialized_end=855
  _QUERYTOTALSHARESREQUEST._serialized_start=857
  _QUERYTOTALSHARESREQUEST._serialized_end=918
  _QUERYTOTALSHARESRESPONSE._serialized_start=920
  _QUERYTOTALSHARESRESPONSE._serialized_end=1023
  _QUERYPOOLASSETSREQUEST._serialized_start=1025
  _QUERYPOOLASSETSREQUEST._serialized_end=1085
  _QUERYPOOLASSETSRESPONSE._serialized_start=1087
  _QUERYPOOLASSETSRESPONSE._serialized_end=1171
  _QUERYSPOTPRICEREQUEST._serialized_start=1174
  _QUERYSPOTPRICEREQUEST._serialized_end=1380
  _QUERYSPOTPRICERESPONSE._serialized_start=1382
  _QUERYSPOTPRICERESPONSE._serialized_end=1448
  _QUERYSWAPEXACTAMOUNTINREQUEST._serialized_start=1451
  _QUERYSWAPEXACTAMOUNTINREQUEST._serialized_end=1671
  _QUERYSWAPEXACTAMOUNTINRESPONSE._serialized_start=1674
  _QUERYSWAPEXACTAMOUNTINRESPONSE._serialized_end=1805
  _QUERYSWAPEXACTAMOUNTOUTREQUEST._serialized_start=1808
  _QUERYSWAPEXACTAMOUNTOUTREQUEST._serialized_end=2032
  _QUERYSWAPEXACTAMOUNTOUTRESPONSE._serialized_start=2035
  _QUERYSWAPEXACTAMOUNTOUTRESPONSE._serialized_end=2165
  _QUERYTOTALLIQUIDITYREQUEST._serialized_start=2167
  _QUERYTOTALLIQUIDITYREQUEST._serialized_end=2195
  _QUERYTOTALLIQUIDITYRESPONSE._serialized_start=2198
  _QUERYTOTALLIQUIDITYRESPONSE._serialized_end=2343
  _QUERY._serialized_start=2346
  _QUERY._serialized_end=3996
# @@protoc_insertion_point(module_scope)
