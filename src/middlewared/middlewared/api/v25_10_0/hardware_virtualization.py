from middlewared.api.base import BaseModel

__all__ = ("HardwareVirtualizationVariantArgs", "HardwareVirtualizationVariantResult")


class HardwareVirtualizationVariantArgs(BaseModel):
    pass


class HardwareVirtualizationVariantResult(BaseModel):
    result: str
    """The hardware virtualization variant available on this system."""
