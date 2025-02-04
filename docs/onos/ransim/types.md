# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [onos/ransim/types/types.proto](#onos_ransim_types_types-proto)
    - [Beam](#onos-ransim-types-Beam)
    - [BeamCoverageEntry](#onos-ransim-types-BeamCoverageEntry)
    - [BeamID](#onos-ransim-types-BeamID)
    - [BoundingBox](#onos-ransim-types-BoundingBox)
    - [BoundingBoxEntry](#onos-ransim-types-BoundingBoxEntry)
    - [Bwp](#onos-ransim-types-Bwp)
    - [Carrier](#onos-ransim-types-Carrier)
    - [Cell](#onos-ransim-types-Cell)
    - [Cell.BwpsEntry](#onos-ransim-types-Cell-BwpsEntry)
    - [Cell.CachedStatesEntry](#onos-ransim-types-Cell-CachedStatesEntry)
    - [CellConfig](#onos-ransim-types-CellConfig)
    - [CellCoverageInfo](#onos-ransim-types-CellCoverageInfo)
    - [Channel](#onos-ransim-types-Channel)
    - [Coordinate](#onos-ransim-types-Coordinate)
    - [CoverageBoundary](#onos-ransim-types-CoverageBoundary)
    - [EventA3Params](#onos-ransim-types-EventA3Params)
    - [Grid](#onos-ransim-types-Grid)
    - [GridPointsEntry](#onos-ransim-types-GridPointsEntry)
    - [Guami](#onos-ransim-types-Guami)
    - [InterferingBeamsEntry](#onos-ransim-types-InterferingBeamsEntry)
    - [MapLayout](#onos-ransim-types-MapLayout)
    - [MeasurementParams](#onos-ransim-types-MeasurementParams)
    - [MeasurementParams.NcellIndividualOffsetsEntry](#onos-ransim-types-MeasurementParams-NcellIndividualOffsetsEntry)
    - [Node](#onos-ransim-types-Node)
    - [Route](#onos-ransim-types-Route)
    - [ShadowingMapEntry](#onos-ransim-types-ShadowingMapEntry)
    - [UECell](#onos-ransim-types-UECell)
    - [Ue](#onos-ransim-types-Ue)
    - [UeIdentity](#onos-ransim-types-UeIdentity)
    - [UeMetrics](#onos-ransim-types-UeMetrics)
  
    - [CellType](#onos-ransim-types-CellType)
  
- [Scalar Value Types](#scalar-value-types)



<a name="onos_ransim_types_types-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## onos/ransim/types/types.proto



<a name="onos-ransim-types-Beam"></a>

### Beam



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| beam_index | [int32](#int32) |  |  |
| azimuth | [double](#double) |  |  |
| tilt | [double](#double) |  |  |
| h3db_angle | [double](#double) |  |  |
| v3db_angle | [double](#double) |  |  |
| max_gain | [double](#double) |  |  |






<a name="onos-ransim-types-BeamCoverageEntry"></a>

### BeamCoverageEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| beam_id | [BeamID](#onos-ransim-types-BeamID) |  |  |
| coverage_boundaries | [CoverageBoundary](#onos-ransim-types-CoverageBoundary) | repeated |  |






<a name="onos-ransim-types-BeamID"></a>

### BeamID



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ncgi | [uint64](#uint64) |  |  |
| carrier_index | [int32](#int32) |  |  |
| beam_index | [int32](#int32) |  |  |






<a name="onos-ransim-types-BoundingBox"></a>

### BoundingBox



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min_lat | [double](#double) |  |  |
| min_lng | [double](#double) |  |  |
| max_lat | [double](#double) |  |  |
| max_lng | [double](#double) |  |  |






<a name="onos-ransim-types-BoundingBoxEntry"></a>

### BoundingBoxEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| beam_id | [BeamID](#onos-ransim-types-BeamID) |  |  |
| bounding_box | [BoundingBox](#onos-ransim-types-BoundingBox) |  |  |






<a name="onos-ransim-types-Bwp"></a>

### Bwp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint64](#uint64) |  |  |
| scs | [int32](#int32) |  |  |
| number_of_rbs | [int32](#int32) |  |  |
| downlink | [bool](#bool) |  |  |






<a name="onos-ransim-types-Carrier"></a>

### Carrier



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| beams | [Beam](#onos-ransim-types-Beam) | repeated |  |
| center | [Coordinate](#onos-ransim-types-Coordinate) |  |  |
| height | [int32](#int32) |  |  |
| arfcn_dl | [uint32](#uint32) |  |  |
| arfcn_ul | [uint32](#uint32) |  |  |
| bs_channel_bw_dl | [uint32](#uint32) |  |  |
| bs_channel_bw_ul | [uint32](#uint32) |  |  |
| tx_power_db | [double](#double) |  |  |
| v_side_lobe_attenuation_db | [double](#double) |  |  |
| environment | [string](#string) |  |  |
| los | [bool](#bool) |  |  |






<a name="onos-ransim-types-Cell"></a>

### Cell



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cell_config | [CellConfig](#onos-ransim-types-CellConfig) |  |  |
| ncgi | [uint64](#uint64) |  |  |
| color | [string](#string) |  |  |
| max_ues | [uint32](#uint32) |  |  |
| neighbors | [uint64](#uint64) | repeated |  |
| measurement_params | [MeasurementParams](#onos-ransim-types-MeasurementParams) |  |  |
| pci | [uint32](#uint32) |  |  |
| earfcn | [uint32](#uint32) |  |  |
| cell_type | [CellType](#onos-ransim-types-CellType) |  |  |
| arfcn_dl | [uint32](#uint32) |  |  |
| arfcn_ul | [uint32](#uint32) |  |  |
| bs_channel_bw_dl | [uint32](#uint32) |  |  |
| bs_channel_bw_ul | [uint32](#uint32) |  |  |
| bwps | [Cell.BwpsEntry](#onos-ransim-types-Cell-BwpsEntry) | repeated |  |
| rrc_idle_count | [uint32](#uint32) |  |  |
| rrc_connected_count | [uint32](#uint32) |  |  |
| cached | [bool](#bool) |  |  |
| cached_states | [Cell.CachedStatesEntry](#onos-ransim-types-Cell-CachedStatesEntry) | repeated |  |
| current_state_hash | [string](#string) |  |  |
| resource_alloc_scheme | [string](#string) |  |  |
| beam_interference_mapping | [InterferingBeamsEntry](#onos-ransim-types-InterferingBeamsEntry) | repeated |  |
| grid | [Grid](#onos-ransim-types-Grid) |  |  |






<a name="onos-ransim-types-Cell-BwpsEntry"></a>

### Cell.BwpsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint64](#uint64) |  |  |
| value | [Bwp](#onos-ransim-types-Bwp) |  |  |






<a name="onos-ransim-types-Cell-CachedStatesEntry"></a>

### Cell.CachedStatesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [CellCoverageInfo](#onos-ransim-types-CellCoverageInfo) |  |  |






<a name="onos-ransim-types-CellConfig"></a>

### CellConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| carriers | [Carrier](#onos-ransim-types-Carrier) | repeated |  |






<a name="onos-ransim-types-CellCoverageInfo"></a>

### CellCoverageInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rp_coverage_boundaries | [BeamCoverageEntry](#onos-ransim-types-BeamCoverageEntry) | repeated |  |
| coverage_boundaries | [BeamCoverageEntry](#onos-ransim-types-BeamCoverageEntry) | repeated |  |






<a name="onos-ransim-types-Channel"></a>

### Channel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ssb_frequency | [uint32](#uint32) |  |  |
| arfcn_dl | [uint32](#uint32) |  |  |
| arfcn_ul | [uint32](#uint32) |  |  |
| environment | [string](#string) |  |  |
| bs_channel_bw_dl | [uint32](#uint32) |  |  |
| bs_channel_bw_ul | [uint32](#uint32) |  |  |
| bs_channel_bw_sul | [uint32](#uint32) |  |  |
| los | [bool](#bool) |  |  |






<a name="onos-ransim-types-Coordinate"></a>

### Coordinate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lat | [double](#double) |  |  |
| lng | [double](#double) |  |  |






<a name="onos-ransim-types-CoverageBoundary"></a>

### CoverageBoundary



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_signal_strength | [double](#double) |  |  |
| boundary_points | [Coordinate](#onos-ransim-types-Coordinate) | repeated |  |






<a name="onos-ransim-types-EventA3Params"></a>

### EventA3Params



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| a3_offset | [int32](#int32) |  |  |
| report_on_leave | [bool](#bool) |  |  |






<a name="onos-ransim-types-Grid"></a>

### Grid



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| shadowing_maps | [ShadowingMapEntry](#onos-ransim-types-ShadowingMapEntry) | repeated |  |
| grid_points_maps | [GridPointsEntry](#onos-ransim-types-GridPointsEntry) | repeated |  |
| bounding_boxes | [BoundingBoxEntry](#onos-ransim-types-BoundingBoxEntry) | repeated |  |






<a name="onos-ransim-types-GridPointsEntry"></a>

### GridPointsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| beam_id | [BeamID](#onos-ransim-types-BeamID) |  |  |
| grid_points | [Coordinate](#onos-ransim-types-Coordinate) | repeated |  |






<a name="onos-ransim-types-Guami"></a>

### Guami



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| plmnid | [uint32](#uint32) |  | 24 bits (12 bits for MCC and 12 bits for MNC) |
| amf_region_id | [uint32](#uint32) |  | 8 bits |
| amf_set_id | [uint32](#uint32) |  | 10 bits |
| amf_pointer | [uint32](#uint32) |  | 6 bits |






<a name="onos-ransim-types-InterferingBeamsEntry"></a>

### InterferingBeamsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| beam_id | [BeamID](#onos-ransim-types-BeamID) |  |  |
| interfering_beams | [BeamID](#onos-ransim-types-BeamID) | repeated |  |






<a name="onos-ransim-types-MapLayout"></a>

### MapLayout



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| center | [Coordinate](#onos-ransim-types-Coordinate) |  | Map center latitude and longitude |
| zoom | [float](#float) |  | The starting Zoom level |
| fade | [bool](#bool) |  | Show map as faded on start |
| show_routes | [bool](#bool) |  | Show routes on start |
| show_power | [bool](#bool) |  | Show power as circle on start |
| locations_scale | [float](#float) |  | Ratio of random locations diameter to tower grid width |
| min_ues | [uint32](#uint32) |  | FIXME: These are deprecated; remove Max number of UEs for complete simulation |
| max_ues | [uint32](#uint32) |  | Max number of UEs for complete simulation |
| current_routes | [uint32](#uint32) |  | the current number of routes |






<a name="onos-ransim-types-MeasurementParams"></a>

### MeasurementParams



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time_to_trigger | [int32](#int32) |  |  |
| frequency_offset | [int32](#int32) |  |  |
| pcell_individual_offset | [int32](#int32) |  |  |
| ncell_individual_offsets | [MeasurementParams.NcellIndividualOffsetsEntry](#onos-ransim-types-MeasurementParams-NcellIndividualOffsetsEntry) | repeated |  |
| hysteresis | [int32](#int32) |  |  |
| event_a3_params | [EventA3Params](#onos-ransim-types-EventA3Params) |  |  |






<a name="onos-ransim-types-MeasurementParams-NcellIndividualOffsetsEntry"></a>

### MeasurementParams.NcellIndividualOffsetsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint64](#uint64) |  |  |
| value | [int32](#int32) |  |  |






<a name="onos-ransim-types-Node"></a>

### Node



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| enbid | [uint32](#uint32) |  |  |
| controllers | [string](#string) | repeated |  |
| service_models | [string](#string) | repeated |  |
| cell_ecgis | [uint64](#uint64) | repeated |  |
| status | [string](#string) |  |  |






<a name="onos-ransim-types-Route"></a>

### Route



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [uint64](#uint64) |  |  |
| waypoints | [Coordinate](#onos-ransim-types-Coordinate) | repeated |  |
| color | [string](#string) |  |  |
| speed_avg | [uint32](#uint32) |  |  |
| speed_stdev | [uint32](#uint32) |  |  |
| reverse | [bool](#bool) |  |  |
| next_point | [uint32](#uint32) |  |  |






<a name="onos-ransim-types-ShadowingMapEntry"></a>

### ShadowingMapEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| beam_id | [BeamID](#onos-ransim-types-BeamID) |  |  |
| shadowing_map | [double](#double) | repeated |  |






<a name="onos-ransim-types-UECell"></a>

### UECell



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint64](#uint64) |  |  |
| ncgi | [uint64](#uint64) |  |  |
| beam_id | [BeamID](#onos-ransim-types-BeamID) |  |  |
| rsrp | [double](#double) |  |  |
| rsrq | [double](#double) |  |  |
| sinr | [double](#double) |  |  |
| bwp_refs | [Bwp](#onos-ransim-types-Bwp) | repeated |  |
| avail_prbs_dl | [uint32](#uint32) |  |  |






<a name="onos-ransim-types-Ue"></a>

### Ue



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| imsi | [uint64](#uint64) |  |  |
| ueid | [UeIdentity](#onos-ransim-types-UeIdentity) |  |  |
| type | [string](#string) |  |  |
| rrc_state | [uint32](#uint32) |  |  |
| location | [Coordinate](#onos-ransim-types-Coordinate) |  |  |
| heading | [uint32](#uint32) |  |  |
| five_qi | [int32](#int32) |  |  |
| serving_cells | [UECell](#onos-ransim-types-UECell) | repeated |  |
| crnti | [uint32](#uint32) |  |  |
| neighbor_cells | [UECell](#onos-ransim-types-UECell) | repeated |  |
| height | [double](#double) |  |  |
| is_admitted | [bool](#bool) |  |  |






<a name="onos-ransim-types-UeIdentity"></a>

### UeIdentity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| guami | [Guami](#onos-ransim-types-Guami) |  |  |
| amf_ue_ngap_id | [uint64](#uint64) |  |  |






<a name="onos-ransim-types-UeMetrics"></a>

### UeMetrics



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ho_latency | [int64](#int64) |  | Latency (in nanoseconds) of the most recent hand-over |
| ho_report_timestamp | [int64](#int64) |  | Handover report timestamp (in nanoseconds since epoch) |
| is_first | [bool](#bool) |  | flag to indicate the first measurement |





 


<a name="onos-ransim-types-CellType"></a>

### CellType


| Name | Number | Description |
| ---- | ------ | ----------- |
| FEMTO | 0 |  |
| ENTERPRISE | 1 |  |
| OUTDOOR_SMALL | 2 |  |
| MACRO | 3 |  |


 

 

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

