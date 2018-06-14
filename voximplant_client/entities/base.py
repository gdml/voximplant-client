from voximplant_client.http import VoximplantHTTPClient
from voximplant_client.result import VoxImplantAPIResult


class BaseVoximplantEntity:
    list_endpoint = None

    def __init__(self, base_client: 'VoximplantClient'):
        self.base_client = base_client

    def list(self) -> VoxImplantAPIResult:
        if self.list_endpoint is None:
            raise NotImplemented()

        return self.http.get(self.list_endpoint)

    def add(self) -> VoxImplantAPIResult:
        raise NotImplemented()

    @property
    def http(self) -> VoximplantHTTPClient:
        return self.base_client.http


__all__ = [
    BaseVoximplantEntity,
]
