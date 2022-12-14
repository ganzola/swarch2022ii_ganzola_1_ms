from marshmallow import Schema, fields, post_load, ValidationError
from marshmallow.validate import Length, Range, Regexp

from app import models
from app.utils.log import logger


class SearchUser(Schema):
    id_user = fields.Int(validate=Range(min=1, error="id cannot be negative"))
    username = fields.Str(
        validate=[Length(min=1, max=20), Regexp(r"^[a-zA-Z]+$", error="Only alphabetic characters are allowed")]
    )

    @post_load
    def make(self, data, **kwargs):
        if not data:
            raise ValidationError("No params provided")

        return {k: v for k, v in models.User(**data).to_dict().items() if v is not None}


class CreateUser(Schema):
    first_name = fields.Str(validate=Length(min=1, max=20))
    last_name = fields.Str(validate=Length(min=1, max=20))
    username = fields.Str(
        validate=[Length(min=1, max=20), Regexp(r"^[a-zA-Z]+$", error="Only alphabetic characters are allowed")]
    )

    @post_load
    def make(self, data, **kwargs):
        return models.User(**data)
