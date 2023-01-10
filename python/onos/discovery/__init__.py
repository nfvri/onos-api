# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/discovery/discovery.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto
import grpclib


@dataclass(eq=False, repr=False)
class AddPodRequest(betterproto.Message):
    id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddPodResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddRackRequest(betterproto.Message):
    id: str = betterproto.string_field(1)
    pod_id: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddRackResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddSwitchRequest(betterproto.Message):
    id: str = betterproto.string_field(1)
    rack_id: str = betterproto.string_field(2)
    p4_endpoint: str = betterproto.string_field(3)
    gnmi_endpoint: str = betterproto.string_field(4)
    pipeline_config_id: str = betterproto.string_field(5)
    chassis_config_id: str = betterproto.string_field(6)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddSwitchResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddServerIpuRequest(betterproto.Message):
    id: str = betterproto.string_field(1)
    rack_id: str = betterproto.string_field(2)
    p4_endpoint: str = betterproto.string_field(3)
    gnmi_endpoint: str = betterproto.string_field(4)
    pipeline_config_id: str = betterproto.string_field(5)
    chassis_config_id: str = betterproto.string_field(6)
    links: List["InjectedLink"] = betterproto.message_field(7)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class InjectedLink(betterproto.Message):
    port: int = betterproto.uint64_field(1)
    remote_port: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddServerIpuResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


class DiscoveryServiceStub(betterproto.ServiceStub):
    """
    DiscoveryService allows injection of topology objects to act as seeds for
    the topology discovery.
    """

    async def add_pod(self, *, id: str = "") -> "AddPodResponse":
        """AddPod adds a new POD entity with the requisite aspects"""

        request = AddPodRequest()
        request.id = id

        return await self._unary_unary(
            "/onos.discovery.DiscoveryService/AddPod", request, AddPodResponse
        )

    async def add_rack(self, *, id: str = "", pod_id: str = "") -> "AddRackResponse":
        """
        AddRack adds a new rack entity with the requisite aspects as part of a
        POD
        """

        request = AddRackRequest()
        request.id = id
        request.pod_id = pod_id

        return await self._unary_unary(
            "/onos.discovery.DiscoveryService/AddRack", request, AddRackResponse
        )

    async def add_switch(
        self,
        *,
        id: str = "",
        rack_id: str = "",
        p4_endpoint: str = "",
        gnmi_endpoint: str = "",
        pipeline_config_id: str = "",
        chassis_config_id: str = "",
    ) -> "AddSwitchResponse":
        """
        AddSwitch adds a new switch entity with the requisite aspects into a
        rack
        """

        request = AddSwitchRequest()
        request.id = id
        request.rack_id = rack_id
        request.p4_endpoint = p4_endpoint
        request.gnmi_endpoint = gnmi_endpoint
        request.pipeline_config_id = pipeline_config_id
        request.chassis_config_id = chassis_config_id

        return await self._unary_unary(
            "/onos.discovery.DiscoveryService/AddSwitch", request, AddSwitchResponse
        )

    async def add_server_ipu(self) -> "AddServerIpuResponse":
        """
        AddServerIPU adds a new server entity and an associated IPU entity,
        both with the requisite aspects into a rack
        """

        request = AddServerIpuRequest()

        return await self._unary_unary(
            "/onos.discovery.DiscoveryService/AddServerIPU",
            request,
            AddServerIpuResponse,
        )
