class VoxImplantClientException(BaseException):
    pass


class VoxImplantBadApplicationNameException(VoxImplantClientException):
    pass


class VoxImplantRuleCreationError(VoxImplantClientException):
    pass
