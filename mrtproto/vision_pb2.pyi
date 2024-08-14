from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FramePrediction(_message.Message):
    __slots__ = ("x", "y", "width", "height", "confidence", "class_id", "class_name", "class_color")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    CLASS_COLOR_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    width: float
    height: float
    confidence: float
    class_id: int
    class_name: str
    class_color: str
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ..., confidence: _Optional[float] = ..., class_id: _Optional[int] = ..., class_name: _Optional[str] = ..., class_color: _Optional[str] = ...) -> None: ...

class Frame(_message.Message):
    __slots__ = ("frame_number", "ttag_system", "ttag_steady_ns", "prediction_duration_ms", "predictions")
    FRAME_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TTAG_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    TTAG_STEADY_NS_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    frame_number: int
    ttag_system: _timestamp_pb2.Timestamp
    ttag_steady_ns: int
    prediction_duration_ms: int
    predictions: _containers.RepeatedCompositeFieldContainer[FramePrediction]
    def __init__(self, frame_number: _Optional[int] = ..., ttag_system: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ttag_steady_ns: _Optional[int] = ..., prediction_duration_ms: _Optional[int] = ..., predictions: _Optional[_Iterable[_Union[FramePrediction, _Mapping]]] = ...) -> None: ...

class OccupancyMap(_message.Message):
    __slots__ = ("ttag_system", "ttag_steady_ns", "lat_deg", "lon_deg", "width_m", "height_m", "width_px", "height_px", "grid")
    TTAG_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    TTAG_STEADY_NS_FIELD_NUMBER: _ClassVar[int]
    LAT_DEG_FIELD_NUMBER: _ClassVar[int]
    LON_DEG_FIELD_NUMBER: _ClassVar[int]
    WIDTH_M_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_M_FIELD_NUMBER: _ClassVar[int]
    WIDTH_PX_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_PX_FIELD_NUMBER: _ClassVar[int]
    GRID_FIELD_NUMBER: _ClassVar[int]
    ttag_system: _timestamp_pb2.Timestamp
    ttag_steady_ns: int
    lat_deg: float
    lon_deg: float
    width_m: float
    height_m: float
    width_px: int
    height_px: int
    grid: bytes
    def __init__(self, ttag_system: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ttag_steady_ns: _Optional[int] = ..., lat_deg: _Optional[float] = ..., lon_deg: _Optional[float] = ..., width_m: _Optional[float] = ..., height_m: _Optional[float] = ..., width_px: _Optional[int] = ..., height_px: _Optional[int] = ..., grid: _Optional[bytes] = ...) -> None: ...
