# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csensor.proto\x12\x17magothy.protobuf.sensor\x1a\x1fgoogle/protobuf/timestamp.proto\"\x90\x01\n\x04Pose\x12\x0f\n\x07lat_deg\x18\x01 \x01(\x01\x12\x0f\n\x07lon_deg\x18\x02 \x01(\x01\x12\x13\n\x0bheading_deg\x18\x03 \x01(\x02\x12\x1b\n\x13position_covariance\x18\x04 \x03(\x02\x12\x1e\n\x11heading_error_deg\x18\x05 \x01(\x02H\x00\x88\x01\x01\x42\x14\n\x12_heading_error_deg\"\x80\x03\n\x05Range\x12/\n\x0bttag_system\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0ettag_steady_ns\x18\x02 \x01(\x04\x12\x31\n\x04type\x18\x03 \x01(\x0e\x32#.magothy.protobuf.sensor.Range.Type\x12\x0f\n\x07range_m\x18\x04 \x01(\x01\x12\x1b\n\x13range_uncertainty_m\x18\x05 \x01(\x01\x12\x13\n\x0bmax_range_m\x18\x08 \x01(\x01\x12\x19\n\x11\x66ield_of_view_deg\x18\x06 \x01(\x01\x12\x30\n\x04pose\x18\x07 \x01(\x0b\x32\x1d.magothy.protobuf.sensor.PoseH\x00\x88\x01\x01\x12\x16\n\ttarget_id\x18\t \x01(\tH\x01\x88\x01\x01\"<\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nULTRASOUND\x10\x01\x12\x0c\n\x08INFRARED\x10\x02\x12\t\n\x05LASER\x10\x03\x42\x07\n\x05_poseB\x0c\n\n_target_id\"\xa2\x01\n\x0eTargetPosition\x12/\n\x0bttag_system\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0ettag_steady_ns\x18\x02 \x01(\x04\x12\x11\n\ttarget_id\x18\x03 \x01(\t\x12\x0f\n\x07lat_deg\x18\x04 \x01(\x01\x12\x0f\n\x07lon_deg\x18\x05 \x01(\x01\x12\x12\n\nconfidence\x18\x06 \x01(\x01\"\x96\x01\n\x0fTargetPositions\x12/\n\x0bttag_system\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0ettag_steady_ns\x18\x02 \x01(\x04\x12:\n\tpositions\x18\x03 \x03(\x0b\x32\'.magothy.protobuf.sensor.TargetPositionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sensor_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_POSE']._serialized_start=75
  _globals['_POSE']._serialized_end=219
  _globals['_RANGE']._serialized_start=222
  _globals['_RANGE']._serialized_end=606
  _globals['_RANGE_TYPE']._serialized_start=523
  _globals['_RANGE_TYPE']._serialized_end=583
  _globals['_TARGETPOSITION']._serialized_start=609
  _globals['_TARGETPOSITION']._serialized_end=771
  _globals['_TARGETPOSITIONS']._serialized_start=774
  _globals['_TARGETPOSITIONS']._serialized_end=924
# @@protoc_insertion_point(module_scope)
