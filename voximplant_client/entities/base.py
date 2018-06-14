from typing import Iterable

from cached_property import cached_property

from voximplant_client.http import VoximplantHTTPClient
from voximplant_client.result import VoxImplantAPIResult


class BaseVoximplantEntity:
    list_endpoint = None

    def __init__(self, base_client: 'VoximplantClient'):
        self.base_client = base_client  # instance of base client, used for interaction between entities

    def list(self) -> VoxImplantAPIResult:
        """A list of entities.

        For simple endpoints you do not need to define this method, settings class attribute `list_endpoint` would be enough"""
        if self.list_endpoint is None:
            raise NotImplemented()

        return self.http.get_list(self.list_endpoint)

    def add(self) -> VoxImplantAPIResult:
        raise NotImplemented()

    @property
    def http(self) -> VoximplantHTTPClient:
        """Instance of the app-wide HTTP client"""
        return self.base_client.http

    @cached_property
    def _cached_list(self) -> Iterable[dict]:
        """A list of entities, that is retrieved only on the first call"""
        result = self.list()
        return result.result


__all__ = [
    BaseVoximplantEntity,
]
