from collections import OrderedDict
from typing import Iterable, Optional


class VoxImplantAPIResult(OrderedDict):
    @property
    def result(self) -> Iterable:
        return self.get('result', [])

    @property
    def error(self) -> Optional[dict]:
        return self.get('error')

    @property
    def isError(self) -> bool:
        return self.error is not None
