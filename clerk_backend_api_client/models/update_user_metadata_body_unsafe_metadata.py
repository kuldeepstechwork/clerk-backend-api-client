from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateUserMetadataBodyUnsafeMetadata")


@_attrs_define
class UpdateUserMetadataBodyUnsafeMetadata:
    """Metadata saved on the user, that can be updated from both the Frontend and Backend APIs.
    The new object will be merged with the existing value.

    Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.

    """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        update_user_metadata_body_unsafe_metadata = cls()

        update_user_metadata_body_unsafe_metadata.additional_properties = d
        return update_user_metadata_body_unsafe_metadata

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
