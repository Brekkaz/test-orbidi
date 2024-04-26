from graphql import GraphQLError
from strawberry.exceptions import StrawberryGraphQLError


class AppError(BaseException):
    CANCEL = "NONE"
    WAIT_AND_RETRY = "WAIT_AND_RETRY"
    RETRY = "RETRY"

    UNAUTHENTICATED = "UNAUTHENTICATED"
    DATASOURCE_ERROR = "DATASOURCE_ERROR"

    def __init__(self, detail: str = "", code: str = "", level: str = WAIT_AND_RETRY):
        self.detail = detail
        self.code = code
        self.level = level

    def extend(self):
        return StrawberryGraphQLError(
            message=self.detail,
            extensions={
                "detail": self.detail,
                "code": self.code,
                "level": self.level
            }
        )

    def error(self):
        return StrawberryGraphQLError(
            message=self.detail,
            extensions={
                "detail": self.detail,
                "code": self.code,
                "level": self.level
            }
        ).__dict__

    @staticmethod
    def unauthenticated():
        return AppError(
            detail=AppError.UNAUTHENTICATED,
            code=AppError.UNAUTHENTICATED,
            level=AppError.CANCEL,
        )
