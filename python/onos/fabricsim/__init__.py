# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/fabricsim/devices.proto, onos/fabricsim/hosts.proto, onos/fabricsim/links.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
import grpclib


@dataclass(eq=False, repr=False)
class Device(betterproto.Message):
    """Device describes a simulated switch or IPU"""

    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Port(betterproto.Message):
    """Port describes a simulated device port"""

    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetDevicesRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetDevicesResponse(betterproto.Message):
    devices: List["Device"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetDeviceRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetDeviceResponse(betterproto.Message):
    device: "Device" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddDeviceRequest(betterproto.Message):
    device: "Device" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddDeviceResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RemoveDeviceRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RemoveDeviceResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class StopDeviceRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class StopDeviceResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class StartDeviceRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class StartDeviceResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DisablePortRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DisablePortResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class EnablePortRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class EnablePortResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Host(betterproto.Message):
    """Device describes a simulated switch or IPU"""

    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class NetworkInterface(betterproto.Message):
    """Port describes a simulated device port"""

    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class NetworkInterfaceBehavior(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetHostsRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetHostsResponse(betterproto.Message):
    hosts: List["Host"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetHostRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetHostResponse(betterproto.Message):
    host: "Host" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddHostRequest(betterproto.Message):
    host: "Host" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddHostResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RemoveHostRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RemoveHostResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Link(betterproto.Message):
    """Device describes a simulated switch or IPU"""

    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetLinksRequest(betterproto.Message):
    """Port describes a simulated device port"""

    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetLinksResponse(betterproto.Message):
    links: List["Link"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetLinkRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetLinkResponse(betterproto.Message):
    link: "Link" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddLinkRequest(betterproto.Message):
    link: "Link" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AddLinkResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RemoveLinkRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RemoveLinkResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


class DeviceServiceStub(betterproto.ServiceStub):
    """
    DeviceService provides means to control inventory of simulated devices
    (switches and IPUs) and their ports
    """

    async def get_devices(self) -> "GetDevicesResponse":
        """
        GetDevices gets a list of all simulated devices (switches and/or IPUs)
        """

        request = GetDevicesRequest()

        return await self._unary_unary(
            "/onos.fabricsim.DeviceService/GetDevices", request, GetDevicesResponse
        )

    async def get_device(self) -> "GetDeviceResponse":
        """GetDevice gets a specific device entry"""

        request = GetDeviceRequest()

        return await self._unary_unary(
            "/onos.fabricsim.DeviceService/GetDevice", request, GetDeviceResponse
        )

    async def add_device(self, *, device: "Device" = None) -> "AddDeviceResponse":
        """
        AddDevice creates a new simulated deviceand start its P4Runtime and
        gNMI services
        """

        request = AddDeviceRequest()
        if device is not None:
            request.device = device

        return await self._unary_unary(
            "/onos.fabricsim.DeviceService/AddDevice", request, AddDeviceResponse
        )

    async def remove_device(self, *, device: "Device" = None) -> "RemoveDeviceResponse":
        """RemoveDevice removes a simulated device"""

        request = AddDeviceRequest()
        if device is not None:
            request.device = device

        return await self._unary_unary(
            "/onos.fabricsim.DeviceService/RemoveDevice", request, RemoveDeviceResponse
        )

    async def stop_device(self) -> "StopDeviceResponse":
        """StopDevice stops the simulated deviceP4Runtime and gNMI services"""

        request = StopDeviceRequest()

        return await self._unary_unary(
            "/onos.fabricsim.DeviceService/StopDevice", request, StopDeviceResponse
        )

    async def start_device(self) -> "StartDeviceResponse":
        """
        StartDevice starts the simulated deviceP4Runtime and gNMI services
        """

        request = StartDeviceRequest()

        return await self._unary_unary(
            "/onos.fabricsim.DeviceService/StartDevice", request, StartDeviceResponse
        )

    async def disable_port(self) -> "DisablePortResponse":
        """DisablePort disables the specified port"""

        request = DisablePortRequest()

        return await self._unary_unary(
            "/onos.fabricsim.DeviceService/DisablePort", request, DisablePortResponse
        )

    async def enable_port(self) -> "EnablePortResponse":
        """EnablePort enables the specified port"""

        request = EnablePortRequest()

        return await self._unary_unary(
            "/onos.fabricsim.DeviceService/EnablePort", request, EnablePortResponse
        )


class HostServiceStub(betterproto.ServiceStub):
    """
    DeviceService provides means to control inventory of simulated devices
    (switches and IPUs) and their ports
    """

    async def get_hosts(self) -> "GetHostsResponse":
        """
        GetDevices gets a list of all simulated devices (switches and/or IPUs)
        """

        request = GetHostsRequest()

        return await self._unary_unary(
            "/onos.fabricsim.HostService/GetHosts", request, GetHostsResponse
        )

    async def get_host(self) -> "GetHostResponse":
        """GetDevice gets a specific device entry"""

        request = GetHostRequest()

        return await self._unary_unary(
            "/onos.fabricsim.HostService/GetHost", request, GetHostResponse
        )

    async def add_host(self, *, host: "Host" = None) -> "AddHostResponse":
        """
        AddDevice creates a new simulated deviceand start its P4Runtime and
        gNMI services
        """

        request = AddHostRequest()
        if host is not None:
            request.host = host

        return await self._unary_unary(
            "/onos.fabricsim.HostService/AddHost", request, AddHostResponse
        )

    async def remove_host(self) -> "RemoveHostResponse":
        """RemoveDevice removes a simulated device"""

        request = RemoveHostRequest()

        return await self._unary_unary(
            "/onos.fabricsim.HostService/RemoveHost", request, RemoveHostResponse
        )


class LinkServiceStub(betterproto.ServiceStub):
    """
    DeviceService provides means to control inventory of simulated devices
    (switches and IPUs) and their ports
    """

    async def get_links(self) -> "GetLinksResponse":
        """
        GetDevices gets a list of all simulated devices (switches and/or IPUs)
        """

        request = GetLinksRequest()

        return await self._unary_unary(
            "/onos.fabricsim.LinkService/GetLinks", request, GetLinksResponse
        )

    async def get_link(self) -> "GetLinkResponse":
        """GetDevice gets a specific device entry"""

        request = GetLinkRequest()

        return await self._unary_unary(
            "/onos.fabricsim.LinkService/GetLink", request, GetLinkResponse
        )

    async def add_link(self, *, link: "Link" = None) -> "AddLinkRequest":
        """
        AddDevice creates a new simulated deviceand start its P4Runtime and
        gNMI services
        """

        request = AddLinkRequest()
        if link is not None:
            request.link = link

        return await self._unary_unary(
            "/onos.fabricsim.LinkService/AddLink", request, AddLinkRequest
        )

    async def remove_link(self) -> "RemoveLinkRequest":
        """RemoveDevice removes a simulated device"""

        request = RemoveLinkRequest()

        return await self._unary_unary(
            "/onos.fabricsim.LinkService/RemoveLink", request, RemoveLinkRequest
        )
