# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spdk.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spdk.proto',
  package='proto',
  syntax='proto3',
  serialized_pb=_b('\n\nspdk.proto\x12\x05proto\".\n\rErrorResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"\xe4\x02\n\x0b\x42lockDevice\x12\x11\n\tnumBlocks\x18\x01 \x01(\x05\x12\x42\n\x10supportedIOTypes\x18\x02 \x03(\x0b\x32(.proto.BlockDevice.SupportedIOTypesEntry\x12\x18\n\x10isOpenedForWrite\x18\x03 \x01(\x08\x12>\n\x0e\x64riverSpecific\x18\x04 \x03(\x0b\x32&.proto.BlockDevice.DriverSpecificEntry\x12\x11\n\tblockSize\x18\x05 \x01(\x05\x12\x13\n\x0bproductName\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x1a\x37\n\x15SupportedIOTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x35\n\x13\x44riverSpecificEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"y\n\x18\x43onstructNVMEbdevRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06trtype\x18\x02 \x01(\t\x12\x0e\n\x06traddr\x18\x03 \x01(\t\x12\x0e\n\x06\x61\x64rfam\x18\x04 \x01(\t\x12\x0f\n\x07trsvcid\x18\x05 \x01(\t\x12\x0e\n\x06subnqn\x18\x06 \x01(\t\"L\n\x17\x43onstructAIObdevRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x66ileName\x18\x02 \x01(\t\x12\x11\n\tblockSize\x18\x03 \x01(\x05\"c\n\rNVMFSubsystem\x12\x17\n\x0flistenAddresses\x18\x01 \x03(\t\x12\x0c\n\x04\x63ore\x18\x02 \x01(\x05\x12\x0b\n\x03nqn\x18\x03 \x01(\t\x12\r\n\x05hosts\x18\x04 \x03(\t\x12\x0f\n\x07subtype\x18\x05 \x01(\t\"\x9d\x01\n\x1d\x43onstructNVMFSubsystemRequest\x12\x0c\n\x04\x63ore\x18\x01 \x01(\x05\x12\x0b\n\x03nqn\x18\x02 \x01(\t\x12\x0e\n\x06listen\x18\x03 \x01(\t\x12\r\n\x05hosts\x18\x04 \x01(\t\x12\x18\n\x10isAnyHostAllowed\x18\x05 \x01(\x08\x12\x14\n\x0cserialNumber\x18\x06 \x01(\t\x12\x12\n\nnamespaces\x18\x07 \x01(\t\"\xe7\x01\n\x16\x43onstructTargetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\taliasName\x18\x02 \x01(\t\x12\x16\n\x0elunNameIdPairs\x18\x03 \x01(\t\x12\x14\n\x0cpgigMappings\x18\x04 \x01(\t\x12\x12\n\nqueueDepth\x18\x05 \x01(\x05\x12\x14\n\x0c\x63hapDisabled\x18\x06 \x01(\x05\x12\x13\n\x0b\x63hapEnabled\x18\x07 \x01(\x05\x12\x14\n\x0c\x63hapRequired\x18\x08 \x01(\x05\x12\x12\n\nchapMutual\x18\t \x01(\x05\x12\x15\n\rchapAuthGroup\x18\n \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ERRORRESPONSE = _descriptor.Descriptor(
  name='ErrorResponse',
  full_name='proto.ErrorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.ErrorResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='proto.ErrorResponse.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=67,
)


_BLOCKDEVICE_SUPPORTEDIOTYPESENTRY = _descriptor.Descriptor(
  name='SupportedIOTypesEntry',
  full_name='proto.BlockDevice.SupportedIOTypesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.BlockDevice.SupportedIOTypesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.BlockDevice.SupportedIOTypesEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=371,
)

_BLOCKDEVICE_DRIVERSPECIFICENTRY = _descriptor.Descriptor(
  name='DriverSpecificEntry',
  full_name='proto.BlockDevice.DriverSpecificEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.BlockDevice.DriverSpecificEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.BlockDevice.DriverSpecificEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=426,
)

_BLOCKDEVICE = _descriptor.Descriptor(
  name='BlockDevice',
  full_name='proto.BlockDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numBlocks', full_name='proto.BlockDevice.numBlocks', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supportedIOTypes', full_name='proto.BlockDevice.supportedIOTypes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isOpenedForWrite', full_name='proto.BlockDevice.isOpenedForWrite', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='driverSpecific', full_name='proto.BlockDevice.driverSpecific', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blockSize', full_name='proto.BlockDevice.blockSize', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productName', full_name='proto.BlockDevice.productName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.BlockDevice.name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BLOCKDEVICE_SUPPORTEDIOTYPESENTRY, _BLOCKDEVICE_DRIVERSPECIFICENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=426,
)


_CONSTRUCTNVMEBDEVREQUEST = _descriptor.Descriptor(
  name='ConstructNVMEbdevRequest',
  full_name='proto.ConstructNVMEbdevRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.ConstructNVMEbdevRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trtype', full_name='proto.ConstructNVMEbdevRequest.trtype', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traddr', full_name='proto.ConstructNVMEbdevRequest.traddr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adrfam', full_name='proto.ConstructNVMEbdevRequest.adrfam', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trsvcid', full_name='proto.ConstructNVMEbdevRequest.trsvcid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subnqn', full_name='proto.ConstructNVMEbdevRequest.subnqn', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=549,
)


_CONSTRUCTAIOBDEVREQUEST = _descriptor.Descriptor(
  name='ConstructAIObdevRequest',
  full_name='proto.ConstructAIObdevRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.ConstructAIObdevRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileName', full_name='proto.ConstructAIObdevRequest.fileName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blockSize', full_name='proto.ConstructAIObdevRequest.blockSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=627,
)


_NVMFSUBSYSTEM = _descriptor.Descriptor(
  name='NVMFSubsystem',
  full_name='proto.NVMFSubsystem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='listenAddresses', full_name='proto.NVMFSubsystem.listenAddresses', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='core', full_name='proto.NVMFSubsystem.core', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nqn', full_name='proto.NVMFSubsystem.nqn', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hosts', full_name='proto.NVMFSubsystem.hosts', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='proto.NVMFSubsystem.subtype', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=629,
  serialized_end=728,
)


_CONSTRUCTNVMFSUBSYSTEMREQUEST = _descriptor.Descriptor(
  name='ConstructNVMFSubsystemRequest',
  full_name='proto.ConstructNVMFSubsystemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='core', full_name='proto.ConstructNVMFSubsystemRequest.core', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nqn', full_name='proto.ConstructNVMFSubsystemRequest.nqn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='listen', full_name='proto.ConstructNVMFSubsystemRequest.listen', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hosts', full_name='proto.ConstructNVMFSubsystemRequest.hosts', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isAnyHostAllowed', full_name='proto.ConstructNVMFSubsystemRequest.isAnyHostAllowed', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serialNumber', full_name='proto.ConstructNVMFSubsystemRequest.serialNumber', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='namespaces', full_name='proto.ConstructNVMFSubsystemRequest.namespaces', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=731,
  serialized_end=888,
)


_CONSTRUCTTARGETREQUEST = _descriptor.Descriptor(
  name='ConstructTargetRequest',
  full_name='proto.ConstructTargetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.ConstructTargetRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aliasName', full_name='proto.ConstructTargetRequest.aliasName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lunNameIdPairs', full_name='proto.ConstructTargetRequest.lunNameIdPairs', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pgigMappings', full_name='proto.ConstructTargetRequest.pgigMappings', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='queueDepth', full_name='proto.ConstructTargetRequest.queueDepth', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chapDisabled', full_name='proto.ConstructTargetRequest.chapDisabled', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chapEnabled', full_name='proto.ConstructTargetRequest.chapEnabled', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chapRequired', full_name='proto.ConstructTargetRequest.chapRequired', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chapMutual', full_name='proto.ConstructTargetRequest.chapMutual', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chapAuthGroup', full_name='proto.ConstructTargetRequest.chapAuthGroup', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=891,
  serialized_end=1122,
)

_BLOCKDEVICE_SUPPORTEDIOTYPESENTRY.containing_type = _BLOCKDEVICE
_BLOCKDEVICE_DRIVERSPECIFICENTRY.containing_type = _BLOCKDEVICE
_BLOCKDEVICE.fields_by_name['supportedIOTypes'].message_type = _BLOCKDEVICE_SUPPORTEDIOTYPESENTRY
_BLOCKDEVICE.fields_by_name['driverSpecific'].message_type = _BLOCKDEVICE_DRIVERSPECIFICENTRY
DESCRIPTOR.message_types_by_name['ErrorResponse'] = _ERRORRESPONSE
DESCRIPTOR.message_types_by_name['BlockDevice'] = _BLOCKDEVICE
DESCRIPTOR.message_types_by_name['ConstructNVMEbdevRequest'] = _CONSTRUCTNVMEBDEVREQUEST
DESCRIPTOR.message_types_by_name['ConstructAIObdevRequest'] = _CONSTRUCTAIOBDEVREQUEST
DESCRIPTOR.message_types_by_name['NVMFSubsystem'] = _NVMFSUBSYSTEM
DESCRIPTOR.message_types_by_name['ConstructNVMFSubsystemRequest'] = _CONSTRUCTNVMFSUBSYSTEMREQUEST
DESCRIPTOR.message_types_by_name['ConstructTargetRequest'] = _CONSTRUCTTARGETREQUEST

ErrorResponse = _reflection.GeneratedProtocolMessageType('ErrorResponse', (_message.Message,), dict(
  DESCRIPTOR = _ERRORRESPONSE,
  __module__ = 'spdk_pb2'
  # @@protoc_insertion_point(class_scope:proto.ErrorResponse)
  ))
_sym_db.RegisterMessage(ErrorResponse)

BlockDevice = _reflection.GeneratedProtocolMessageType('BlockDevice', (_message.Message,), dict(

  SupportedIOTypesEntry = _reflection.GeneratedProtocolMessageType('SupportedIOTypesEntry', (_message.Message,), dict(
    DESCRIPTOR = _BLOCKDEVICE_SUPPORTEDIOTYPESENTRY,
    __module__ = 'spdk_pb2'
    # @@protoc_insertion_point(class_scope:proto.BlockDevice.SupportedIOTypesEntry)
    ))
  ,

  DriverSpecificEntry = _reflection.GeneratedProtocolMessageType('DriverSpecificEntry', (_message.Message,), dict(
    DESCRIPTOR = _BLOCKDEVICE_DRIVERSPECIFICENTRY,
    __module__ = 'spdk_pb2'
    # @@protoc_insertion_point(class_scope:proto.BlockDevice.DriverSpecificEntry)
    ))
  ,
  DESCRIPTOR = _BLOCKDEVICE,
  __module__ = 'spdk_pb2'
  # @@protoc_insertion_point(class_scope:proto.BlockDevice)
  ))
_sym_db.RegisterMessage(BlockDevice)
_sym_db.RegisterMessage(BlockDevice.SupportedIOTypesEntry)
_sym_db.RegisterMessage(BlockDevice.DriverSpecificEntry)

ConstructNVMEbdevRequest = _reflection.GeneratedProtocolMessageType('ConstructNVMEbdevRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONSTRUCTNVMEBDEVREQUEST,
  __module__ = 'spdk_pb2'
  # @@protoc_insertion_point(class_scope:proto.ConstructNVMEbdevRequest)
  ))
_sym_db.RegisterMessage(ConstructNVMEbdevRequest)

ConstructAIObdevRequest = _reflection.GeneratedProtocolMessageType('ConstructAIObdevRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONSTRUCTAIOBDEVREQUEST,
  __module__ = 'spdk_pb2'
  # @@protoc_insertion_point(class_scope:proto.ConstructAIObdevRequest)
  ))
_sym_db.RegisterMessage(ConstructAIObdevRequest)

NVMFSubsystem = _reflection.GeneratedProtocolMessageType('NVMFSubsystem', (_message.Message,), dict(
  DESCRIPTOR = _NVMFSUBSYSTEM,
  __module__ = 'spdk_pb2'
  # @@protoc_insertion_point(class_scope:proto.NVMFSubsystem)
  ))
_sym_db.RegisterMessage(NVMFSubsystem)

ConstructNVMFSubsystemRequest = _reflection.GeneratedProtocolMessageType('ConstructNVMFSubsystemRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONSTRUCTNVMFSUBSYSTEMREQUEST,
  __module__ = 'spdk_pb2'
  # @@protoc_insertion_point(class_scope:proto.ConstructNVMFSubsystemRequest)
  ))
_sym_db.RegisterMessage(ConstructNVMFSubsystemRequest)

ConstructTargetRequest = _reflection.GeneratedProtocolMessageType('ConstructTargetRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONSTRUCTTARGETREQUEST,
  __module__ = 'spdk_pb2'
  # @@protoc_insertion_point(class_scope:proto.ConstructTargetRequest)
  ))
_sym_db.RegisterMessage(ConstructTargetRequest)


_BLOCKDEVICE_SUPPORTEDIOTYPESENTRY.has_options = True
_BLOCKDEVICE_SUPPORTEDIOTYPESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_BLOCKDEVICE_DRIVERSPECIFICENTRY.has_options = True
_BLOCKDEVICE_DRIVERSPECIFICENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)