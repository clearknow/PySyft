# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/core_object.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.common import common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/core/core_object.proto',
  package='syft.core',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1cproto/core/core_object.proto\x12\tsyft.core\x1a%proto/core/common/common_object.proto\"C\n\nCoreObject\x12\x35\n\rcommon_object\x18\x01 \x01(\x0b\x32\x1e.syft.core.common.CommonObjectb\x06proto3'
  ,
  dependencies=[proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,])




_COREOBJECT = _descriptor.Descriptor(
  name='CoreObject',
  full_name='syft.core.CoreObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_object', full_name='syft.core.CoreObject.common_object', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=82,
  serialized_end=149,
)

_COREOBJECT.fields_by_name['common_object'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._COMMONOBJECT
DESCRIPTOR.message_types_by_name['CoreObject'] = _COREOBJECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CoreObject = _reflection.GeneratedProtocolMessageType('CoreObject', (_message.Message,), {
  'DESCRIPTOR' : _COREOBJECT,
  '__module__' : 'proto.core.core_object_pb2'
  # @@protoc_insertion_point(class_scope:syft.core.CoreObject)
  })
_sym_db.RegisterMessage(CoreObject)


# @@protoc_insertion_point(module_scope)