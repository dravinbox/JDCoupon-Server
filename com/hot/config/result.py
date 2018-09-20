from enum import Enum, unique


@unique
class ResultCode(Enum):
    Success = 10000
    Failure = 20000


class Result:
    @classmethod
    def base(cls, code=ResultCode.Failure.value, msg=ResultCode.Failure.name, data=None):
        data = {"code": code, "msg": msg, "data": data}
        return data

    @classmethod
    def success(cls, data):
        return cls.base(ResultCode.Success.value, ResultCode.Success.name, data)

    @classmethod
    def failure(cls, data):
        return cls.base(ResultCode.Failure.value, ResultCode.Failure.name, data)

    @classmethod
    def failure_with_msg(cls, msg, data=None):
        return cls.base(ResultCode.Failure.value, msg, data)


