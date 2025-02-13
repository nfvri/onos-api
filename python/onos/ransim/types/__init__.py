# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/ransim/types/types.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto


class CellType(betterproto.Enum):
    FEMTO = 0
    ENTERPRISE = 1
    OUTDOOR_SMALL = 2
    MACRO = 3


@dataclass(eq=False, repr=False)
class Coordinate(betterproto.Message):
    lat: float = betterproto.double_field(1)
    lng: float = betterproto.double_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Carrier(betterproto.Message):
    beams: List["Beam"] = betterproto.message_field(1)
    center: "Coordinate" = betterproto.message_field(2)
    height: int = betterproto.int32_field(3)
    arfcn_dl: int = betterproto.uint32_field(4)
    arfcn_ul: int = betterproto.uint32_field(5)
    bs_channel_bw_dl: int = betterproto.uint32_field(6)
    bs_channel_bw_ul: int = betterproto.uint32_field(7)
    tx_power_db: float = betterproto.double_field(8)
    v_side_lobe_attenuation_db: float = betterproto.double_field(9)
    environment: str = betterproto.string_field(10)
    los: bool = betterproto.bool_field(11)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Route(betterproto.Message):
    name: int = betterproto.uint64_field(1)
    waypoints: List["Coordinate"] = betterproto.message_field(2)
    color: str = betterproto.string_field(3)
    speed_avg: int = betterproto.uint32_field(4)
    speed_stdev: int = betterproto.uint32_field(5)
    reverse: bool = betterproto.bool_field(6)
    next_point: int = betterproto.uint32_field(7)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Ue(betterproto.Message):
    imsi: int = betterproto.uint64_field(1)
    ueid: "UeIdentity" = betterproto.message_field(2)
    type: str = betterproto.string_field(3)
    rrc_state: int = betterproto.uint32_field(4)
    location: "Coordinate" = betterproto.message_field(5)
    heading: int = betterproto.uint32_field(6)
    five_qi: int = betterproto.int32_field(7)
    serving_cells: List["UeCell"] = betterproto.message_field(8)
    crnti: int = betterproto.uint32_field(9)
    neighbor_cells: List["UeCell"] = betterproto.message_field(10)
    height: float = betterproto.double_field(11)
    is_admitted: bool = betterproto.bool_field(12)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class UeCell(betterproto.Message):
    id: int = betterproto.uint64_field(1)
    ncgi: int = betterproto.uint64_field(2)
    beam_id: "BeamId" = betterproto.message_field(3)
    rsrp: float = betterproto.double_field(4)
    rsrq: float = betterproto.double_field(5)
    sinr: float = betterproto.double_field(6)
    bwp_refs: List["Bwp"] = betterproto.message_field(7)
    avail_prbs_dl: int = betterproto.uint32_field(8)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class UeIdentity(betterproto.Message):
    guami: "Guami" = betterproto.message_field(1)
    amf_ue_ngap_id: int = betterproto.uint64_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Guami(betterproto.Message):
    plmnid: int = betterproto.uint32_field(1)
    amf_region_id: int = betterproto.uint32_field(2)
    amf_set_id: int = betterproto.uint32_field(3)
    amf_pointer: int = betterproto.uint32_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class UeMetrics(betterproto.Message):
    # Latency (in nanoseconds) of the most recent hand-over
    ho_latency: int = betterproto.int64_field(1)
    # Handover report timestamp (in nanoseconds since epoch)
    ho_report_timestamp: int = betterproto.int64_field(2)
    # flag to indicate the first measurement
    is_first: bool = betterproto.bool_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class InterferingBeamsEntry(betterproto.Message):
    beam_id: "BeamId" = betterproto.message_field(1)
    interfering_beams: List["BeamId"] = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Cell(betterproto.Message):
    cell_config: "CellConfig" = betterproto.message_field(1)
    ncgi: int = betterproto.uint64_field(2)
    color: str = betterproto.string_field(3)
    max_ues: int = betterproto.uint32_field(4)
    neighbors: List[int] = betterproto.uint64_field(5)
    measurement_params: "MeasurementParams" = betterproto.message_field(6)
    pci: int = betterproto.uint32_field(7)
    earfcn: int = betterproto.uint32_field(8)
    cell_type: "CellType" = betterproto.enum_field(9)
    arfcn_dl: int = betterproto.uint32_field(10)
    arfcn_ul: int = betterproto.uint32_field(11)
    bs_channel_bw_dl: int = betterproto.uint32_field(12)
    bs_channel_bw_ul: int = betterproto.uint32_field(13)
    bwps: Dict[int, "Bwp"] = betterproto.map_field(
        14, betterproto.TYPE_UINT64, betterproto.TYPE_MESSAGE
    )
    rrc_idle_count: int = betterproto.uint32_field(15)
    rrc_connected_count: int = betterproto.uint32_field(16)
    cached: bool = betterproto.bool_field(17)
    cached_states: Dict[str, "CellCoverageInfo"] = betterproto.map_field(
        18, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    current_state_hash: str = betterproto.string_field(19)
    resource_alloc_scheme: str = betterproto.string_field(20)
    beam_interference_mapping: List[
        "InterferingBeamsEntry"
    ] = betterproto.message_field(21)
    grid: "Grid" = betterproto.message_field(22)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class CellConfig(betterproto.Message):
    carriers: List["Carrier"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Channel(betterproto.Message):
    ssb_frequency: int = betterproto.uint32_field(1)
    arfcn_dl: int = betterproto.uint32_field(2)
    arfcn_ul: int = betterproto.uint32_field(3)
    environment: str = betterproto.string_field(4)
    bs_channel_bw_dl: int = betterproto.uint32_field(5)
    bs_channel_bw_ul: int = betterproto.uint32_field(6)
    bs_channel_bw_sul: int = betterproto.uint32_field(7)
    los: bool = betterproto.bool_field(8)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class BeamId(betterproto.Message):
    ncgi: int = betterproto.uint64_field(1)
    carrier_index: int = betterproto.int32_field(2)
    beam_index: int = betterproto.int32_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Beam(betterproto.Message):
    beam_index: int = betterproto.int32_field(1)
    azimuth: float = betterproto.double_field(2)
    tilt: float = betterproto.double_field(3)
    h3_db_angle: float = betterproto.double_field(4)
    v3_db_angle: float = betterproto.double_field(5)
    max_gain: float = betterproto.double_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MeasurementParams(betterproto.Message):
    time_to_trigger: int = betterproto.int32_field(1)
    frequency_offset: int = betterproto.int32_field(2)
    pcell_individual_offset: int = betterproto.int32_field(3)
    ncell_individual_offsets: Dict[int, int] = betterproto.map_field(
        4, betterproto.TYPE_UINT64, betterproto.TYPE_INT32
    )
    hysteresis: int = betterproto.int32_field(5)
    event_a3_params: "EventA3Params" = betterproto.message_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class EventA3Params(betterproto.Message):
    a3_offset: int = betterproto.int32_field(1)
    report_on_leave: bool = betterproto.bool_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Bwp(betterproto.Message):
    id: int = betterproto.uint64_field(1)
    scs: int = betterproto.int32_field(2)
    number_of_rbs: int = betterproto.int32_field(3)
    downlink: bool = betterproto.bool_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class BeamCoverageEntry(betterproto.Message):
    beam_id: "BeamId" = betterproto.message_field(1)
    coverage_boundaries: List["CoverageBoundary"] = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class CellCoverageInfo(betterproto.Message):
    rp_coverage_boundaries: List["BeamCoverageEntry"] = betterproto.message_field(1)
    coverage_boundaries: List["BeamCoverageEntry"] = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class CoverageBoundary(betterproto.Message):
    ref_signal_strength: float = betterproto.double_field(1)
    boundary_points: List["Coordinate"] = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ShadowingMapEntry(betterproto.Message):
    beam_id: "BeamId" = betterproto.message_field(1)
    shadowing_map: List[float] = betterproto.double_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GridPointsEntry(betterproto.Message):
    beam_id: "BeamId" = betterproto.message_field(1)
    grid_points: List["Coordinate"] = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class BoundingBoxEntry(betterproto.Message):
    beam_id: "BeamId" = betterproto.message_field(1)
    bounding_box: "BoundingBox" = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Grid(betterproto.Message):
    shadowing_maps: List["ShadowingMapEntry"] = betterproto.message_field(1)
    grid_points_maps: List["GridPointsEntry"] = betterproto.message_field(2)
    bounding_boxes: List["BoundingBoxEntry"] = betterproto.message_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class BoundingBox(betterproto.Message):
    min_lat: float = betterproto.double_field(1)
    min_lng: float = betterproto.double_field(2)
    max_lat: float = betterproto.double_field(3)
    max_lng: float = betterproto.double_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Node(betterproto.Message):
    enbid: int = betterproto.uint32_field(1)
    controllers: List[str] = betterproto.string_field(2)
    service_models: List[str] = betterproto.string_field(3)
    cell_ecgis: List[int] = betterproto.uint64_field(4)
    status: str = betterproto.string_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MapLayout(betterproto.Message):
    # Map center latitude and longitude
    center: "Coordinate" = betterproto.message_field(1)
    # The starting Zoom level
    zoom: float = betterproto.float_field(2)
    # Show map as faded on start
    fade: bool = betterproto.bool_field(3)
    # Show routes on start
    show_routes: bool = betterproto.bool_field(4)
    # Show power as circle on start
    show_power: bool = betterproto.bool_field(5)
    # Ratio of random locations diameter to tower grid width
    locations_scale: float = betterproto.float_field(9)
    # FIXME: These are deprecated; remove Max number of UEs for complete
    # simulation
    min_ues: int = betterproto.uint32_field(6)
    # Max number of UEs for complete simulation
    max_ues: int = betterproto.uint32_field(7)
    # the current number of routes
    current_routes: int = betterproto.uint32_field(8)

    def __post_init__(self) -> None:
        super().__post_init__()
