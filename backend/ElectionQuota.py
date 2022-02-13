from abc import ABC, abstractmethod


class ElectionQuota(ABC):
    @abstractmethod
    def get_quota(self) -> int:
        pass



