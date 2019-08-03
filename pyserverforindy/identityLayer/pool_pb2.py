# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pool.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pool.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\npool.proto\"\\\n\x1d\x43reatePoolLedgerConfigRequest\x12\x12\n\nConfigName\x18\x01 \x01(\t\x12\'\n\x06\x43onfig\x18\x02 \x01(\x0b\x32\x17.ConfigCreatePoolLedger\"+\n\x16\x43onfigCreatePoolLedger\x12\x11\n\tGensisTxn\x18\x01 \x01(\t\"3\n\x1e\x43reatePoolLedgerConfigResponse\x12\x11\n\tErrorCode\x18\x01 \x01(\x03\"N\n\x15OpenPoolLedgerRequest\x12\x12\n\nConfigName\x18\x01 \x01(\t\x12!\n\x06\x43onfig\x18\x02 \x01(\x0b\x32\x11.ConfigOpenLedger\"U\n\x10\x43onfigOpenLedger\x12\x0f\n\x07Timeout\x18\x01 \x01(\x03\x12\x17\n\x0f\x45xtendedTimeour\x18\x02 \x01(\x03\x12\x17\n\x0fPreorderedNodes\x18\x03 \x03(\t\"(\n\x16OpenPoolLedgerResponse\x12\x0e\n\x06Handle\x18\x01 \x01(\x03\"*\n\x18RefreshPoolLedgerRequest\x12\x0e\n\x06Handle\x18\x01 \x01(\x03\".\n\x19RefreshPoolLedgerResponse\x12\x11\n\tErrorCode\x18\x01 \x01(\x03\"\x12\n\x10ListPoolsRequest\"&\n\x11ListPoolsResponse\x12\x11\n\tErrorCode\x18\x01 \x01(\x03\"(\n\x16\x43losePoolLedgerRequest\x12\x0e\n\x06Handle\x18\x01 \x01(\x03\",\n\x17\x43losePoolLedgerResponse\x12\x11\n\tErrorCode\x18\x01 \x01(\x03\"3\n\x1d\x44\x65letePoolLedgerConfigRequest\x12\x12\n\nConfigName\x18\x01 \x01(\t\"3\n\x1e\x44\x65letePoolLedgerConfigResponse\x12\x11\n\tErrorCode\x18\x01 \x01(\x03\"4\n\x19SetProtocolVersionRequest\x12\x17\n\x0fProtocolVersion\x18\x01 \x01(\x03\"/\n\x1aSetProtocolVersionResponse\x12\x11\n\tErrorCode\x18\x01 \x01(\x03\x62\x06proto3')
)




_CREATEPOOLLEDGERCONFIGREQUEST = _descriptor.Descriptor(
  name='CreatePoolLedgerConfigRequest',
  full_name='CreatePoolLedgerConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ConfigName', full_name='CreatePoolLedgerConfigRequest.ConfigName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Config', full_name='CreatePoolLedgerConfigRequest.Config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=106,
)


_CONFIGCREATEPOOLLEDGER = _descriptor.Descriptor(
  name='ConfigCreatePoolLedger',
  full_name='ConfigCreatePoolLedger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='GensisTxn', full_name='ConfigCreatePoolLedger.GensisTxn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=151,
)


_CREATEPOOLLEDGERCONFIGRESPONSE = _descriptor.Descriptor(
  name='CreatePoolLedgerConfigResponse',
  full_name='CreatePoolLedgerConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ErrorCode', full_name='CreatePoolLedgerConfigResponse.ErrorCode', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=204,
)


_OPENPOOLLEDGERREQUEST = _descriptor.Descriptor(
  name='OpenPoolLedgerRequest',
  full_name='OpenPoolLedgerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ConfigName', full_name='OpenPoolLedgerRequest.ConfigName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Config', full_name='OpenPoolLedgerRequest.Config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=284,
)


_CONFIGOPENLEDGER = _descriptor.Descriptor(
  name='ConfigOpenLedger',
  full_name='ConfigOpenLedger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Timeout', full_name='ConfigOpenLedger.Timeout', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ExtendedTimeour', full_name='ConfigOpenLedger.ExtendedTimeour', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PreorderedNodes', full_name='ConfigOpenLedger.PreorderedNodes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=371,
)


_OPENPOOLLEDGERRESPONSE = _descriptor.Descriptor(
  name='OpenPoolLedgerResponse',
  full_name='OpenPoolLedgerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Handle', full_name='OpenPoolLedgerResponse.Handle', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=413,
)


_REFRESHPOOLLEDGERREQUEST = _descriptor.Descriptor(
  name='RefreshPoolLedgerRequest',
  full_name='RefreshPoolLedgerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Handle', full_name='RefreshPoolLedgerRequest.Handle', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=415,
  serialized_end=457,
)


_REFRESHPOOLLEDGERRESPONSE = _descriptor.Descriptor(
  name='RefreshPoolLedgerResponse',
  full_name='RefreshPoolLedgerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ErrorCode', full_name='RefreshPoolLedgerResponse.ErrorCode', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=459,
  serialized_end=505,
)


_LISTPOOLSREQUEST = _descriptor.Descriptor(
  name='ListPoolsRequest',
  full_name='ListPoolsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=507,
  serialized_end=525,
)


_LISTPOOLSRESPONSE = _descriptor.Descriptor(
  name='ListPoolsResponse',
  full_name='ListPoolsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ErrorCode', full_name='ListPoolsResponse.ErrorCode', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=565,
)


_CLOSEPOOLLEDGERREQUEST = _descriptor.Descriptor(
  name='ClosePoolLedgerRequest',
  full_name='ClosePoolLedgerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Handle', full_name='ClosePoolLedgerRequest.Handle', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=567,
  serialized_end=607,
)


_CLOSEPOOLLEDGERRESPONSE = _descriptor.Descriptor(
  name='ClosePoolLedgerResponse',
  full_name='ClosePoolLedgerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ErrorCode', full_name='ClosePoolLedgerResponse.ErrorCode', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=653,
)


_DELETEPOOLLEDGERCONFIGREQUEST = _descriptor.Descriptor(
  name='DeletePoolLedgerConfigRequest',
  full_name='DeletePoolLedgerConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ConfigName', full_name='DeletePoolLedgerConfigRequest.ConfigName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=655,
  serialized_end=706,
)


_DELETEPOOLLEDGERCONFIGRESPONSE = _descriptor.Descriptor(
  name='DeletePoolLedgerConfigResponse',
  full_name='DeletePoolLedgerConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ErrorCode', full_name='DeletePoolLedgerConfigResponse.ErrorCode', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=708,
  serialized_end=759,
)


_SETPROTOCOLVERSIONREQUEST = _descriptor.Descriptor(
  name='SetProtocolVersionRequest',
  full_name='SetProtocolVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ProtocolVersion', full_name='SetProtocolVersionRequest.ProtocolVersion', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=761,
  serialized_end=813,
)


_SETPROTOCOLVERSIONRESPONSE = _descriptor.Descriptor(
  name='SetProtocolVersionResponse',
  full_name='SetProtocolVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ErrorCode', full_name='SetProtocolVersionResponse.ErrorCode', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=815,
  serialized_end=862,
)

_CREATEPOOLLEDGERCONFIGREQUEST.fields_by_name['Config'].message_type = _CONFIGCREATEPOOLLEDGER
_OPENPOOLLEDGERREQUEST.fields_by_name['Config'].message_type = _CONFIGOPENLEDGER
DESCRIPTOR.message_types_by_name['CreatePoolLedgerConfigRequest'] = _CREATEPOOLLEDGERCONFIGREQUEST
DESCRIPTOR.message_types_by_name['ConfigCreatePoolLedger'] = _CONFIGCREATEPOOLLEDGER
DESCRIPTOR.message_types_by_name['CreatePoolLedgerConfigResponse'] = _CREATEPOOLLEDGERCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['OpenPoolLedgerRequest'] = _OPENPOOLLEDGERREQUEST
DESCRIPTOR.message_types_by_name['ConfigOpenLedger'] = _CONFIGOPENLEDGER
DESCRIPTOR.message_types_by_name['OpenPoolLedgerResponse'] = _OPENPOOLLEDGERRESPONSE
DESCRIPTOR.message_types_by_name['RefreshPoolLedgerRequest'] = _REFRESHPOOLLEDGERREQUEST
DESCRIPTOR.message_types_by_name['RefreshPoolLedgerResponse'] = _REFRESHPOOLLEDGERRESPONSE
DESCRIPTOR.message_types_by_name['ListPoolsRequest'] = _LISTPOOLSREQUEST
DESCRIPTOR.message_types_by_name['ListPoolsResponse'] = _LISTPOOLSRESPONSE
DESCRIPTOR.message_types_by_name['ClosePoolLedgerRequest'] = _CLOSEPOOLLEDGERREQUEST
DESCRIPTOR.message_types_by_name['ClosePoolLedgerResponse'] = _CLOSEPOOLLEDGERRESPONSE
DESCRIPTOR.message_types_by_name['DeletePoolLedgerConfigRequest'] = _DELETEPOOLLEDGERCONFIGREQUEST
DESCRIPTOR.message_types_by_name['DeletePoolLedgerConfigResponse'] = _DELETEPOOLLEDGERCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['SetProtocolVersionRequest'] = _SETPROTOCOLVERSIONREQUEST
DESCRIPTOR.message_types_by_name['SetProtocolVersionResponse'] = _SETPROTOCOLVERSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreatePoolLedgerConfigRequest = _reflection.GeneratedProtocolMessageType('CreatePoolLedgerConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEPOOLLEDGERCONFIGREQUEST,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:CreatePoolLedgerConfigRequest)
  ))
_sym_db.RegisterMessage(CreatePoolLedgerConfigRequest)

ConfigCreatePoolLedger = _reflection.GeneratedProtocolMessageType('ConfigCreatePoolLedger', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGCREATEPOOLLEDGER,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:ConfigCreatePoolLedger)
  ))
_sym_db.RegisterMessage(ConfigCreatePoolLedger)

CreatePoolLedgerConfigResponse = _reflection.GeneratedProtocolMessageType('CreatePoolLedgerConfigResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEPOOLLEDGERCONFIGRESPONSE,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:CreatePoolLedgerConfigResponse)
  ))
_sym_db.RegisterMessage(CreatePoolLedgerConfigResponse)

OpenPoolLedgerRequest = _reflection.GeneratedProtocolMessageType('OpenPoolLedgerRequest', (_message.Message,), dict(
  DESCRIPTOR = _OPENPOOLLEDGERREQUEST,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:OpenPoolLedgerRequest)
  ))
_sym_db.RegisterMessage(OpenPoolLedgerRequest)

ConfigOpenLedger = _reflection.GeneratedProtocolMessageType('ConfigOpenLedger', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGOPENLEDGER,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:ConfigOpenLedger)
  ))
_sym_db.RegisterMessage(ConfigOpenLedger)

OpenPoolLedgerResponse = _reflection.GeneratedProtocolMessageType('OpenPoolLedgerResponse', (_message.Message,), dict(
  DESCRIPTOR = _OPENPOOLLEDGERRESPONSE,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:OpenPoolLedgerResponse)
  ))
_sym_db.RegisterMessage(OpenPoolLedgerResponse)

RefreshPoolLedgerRequest = _reflection.GeneratedProtocolMessageType('RefreshPoolLedgerRequest', (_message.Message,), dict(
  DESCRIPTOR = _REFRESHPOOLLEDGERREQUEST,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:RefreshPoolLedgerRequest)
  ))
_sym_db.RegisterMessage(RefreshPoolLedgerRequest)

RefreshPoolLedgerResponse = _reflection.GeneratedProtocolMessageType('RefreshPoolLedgerResponse', (_message.Message,), dict(
  DESCRIPTOR = _REFRESHPOOLLEDGERRESPONSE,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:RefreshPoolLedgerResponse)
  ))
_sym_db.RegisterMessage(RefreshPoolLedgerResponse)

ListPoolsRequest = _reflection.GeneratedProtocolMessageType('ListPoolsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPOOLSREQUEST,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:ListPoolsRequest)
  ))
_sym_db.RegisterMessage(ListPoolsRequest)

ListPoolsResponse = _reflection.GeneratedProtocolMessageType('ListPoolsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTPOOLSRESPONSE,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:ListPoolsResponse)
  ))
_sym_db.RegisterMessage(ListPoolsResponse)

ClosePoolLedgerRequest = _reflection.GeneratedProtocolMessageType('ClosePoolLedgerRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLOSEPOOLLEDGERREQUEST,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:ClosePoolLedgerRequest)
  ))
_sym_db.RegisterMessage(ClosePoolLedgerRequest)

ClosePoolLedgerResponse = _reflection.GeneratedProtocolMessageType('ClosePoolLedgerResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLOSEPOOLLEDGERRESPONSE,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:ClosePoolLedgerResponse)
  ))
_sym_db.RegisterMessage(ClosePoolLedgerResponse)

DeletePoolLedgerConfigRequest = _reflection.GeneratedProtocolMessageType('DeletePoolLedgerConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEPOOLLEDGERCONFIGREQUEST,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:DeletePoolLedgerConfigRequest)
  ))
_sym_db.RegisterMessage(DeletePoolLedgerConfigRequest)

DeletePoolLedgerConfigResponse = _reflection.GeneratedProtocolMessageType('DeletePoolLedgerConfigResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETEPOOLLEDGERCONFIGRESPONSE,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:DeletePoolLedgerConfigResponse)
  ))
_sym_db.RegisterMessage(DeletePoolLedgerConfigResponse)

SetProtocolVersionRequest = _reflection.GeneratedProtocolMessageType('SetProtocolVersionRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETPROTOCOLVERSIONREQUEST,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:SetProtocolVersionRequest)
  ))
_sym_db.RegisterMessage(SetProtocolVersionRequest)

SetProtocolVersionResponse = _reflection.GeneratedProtocolMessageType('SetProtocolVersionResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETPROTOCOLVERSIONRESPONSE,
  __module__ = 'pool_pb2'
  # @@protoc_insertion_point(class_scope:SetProtocolVersionResponse)
  ))
_sym_db.RegisterMessage(SetProtocolVersionResponse)


# @@protoc_insertion_point(module_scope)