class VoximplantClientException(BaseException):
    pass


class VoximplantBadApplicationNameException(VoximplantClientException):
    pass


class VoximplantRuleCreationError(VoximplantClientException):
    pass
