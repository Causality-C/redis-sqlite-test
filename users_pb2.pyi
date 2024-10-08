"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Empty(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Empty = Empty

@typing.final
class User(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    PREFERRED_OS_FIELD_NUMBER: builtins.int
    id: builtins.int
    name: builtins.str
    email: builtins.str
    preferred_os: builtins.str
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        name: builtins.str = ...,
        email: builtins.str = ...,
        preferred_os: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["email", b"email", "id", b"id", "name", b"name", "preferred_os", b"preferred_os"]) -> None: ...

global___User = User

@typing.final
class NewUser(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    PREFERRED_OS_FIELD_NUMBER: builtins.int
    name: builtins.str
    email: builtins.str
    preferred_os: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        email: builtins.str = ...,
        preferred_os: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["email", b"email", "name", b"name", "preferred_os", b"preferred_os"]) -> None: ...

global___NewUser = NewUser

@typing.final
class UsersList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USERS_FIELD_NUMBER: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___User]: ...
    def __init__(
        self,
        *,
        users: collections.abc.Iterable[global___User] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["users", b"users"]) -> None: ...

global___UsersList = UsersList

@typing.final
class OSRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PREFERRED_OS_FIELD_NUMBER: builtins.int
    preferred_os: builtins.str
    def __init__(
        self,
        *,
        preferred_os: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["preferred_os", b"preferred_os"]) -> None: ...

global___OSRequest = OSRequest
