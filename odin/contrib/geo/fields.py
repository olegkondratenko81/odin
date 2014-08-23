from __future__ import absolute_import, print_function
import odin
from odin import exceptions
from odin.validators import EMPTY_VALUES
from .datatypes import latitude, longitude, latlng, point

__all__ = ('LatitudeField', 'LongitudeField', 'LatLngField')


class LatitudeField(odin.ScalarField):
    """
    Field that contains a latitude value.
    """
    default_error_messages = {
        'invalid': "'%s' value must be a latitude.",
    }

    def to_python(self, value):
        if value in EMPTY_VALUES:
            return
        try:
            return latitude(value)
        except ValueError:
            msg = self.error_messages['invalid'] % value
            raise exceptions.ValidationError(msg)


class LongitudeField(odin.ScalarField):
    """
    Field that contains a longitude value.
    """
    default_error_messages = {
        'invalid': "'%s' value must be a longitude.",
    }

    def to_python(self, value):
        if value in EMPTY_VALUES:
            return
        try:
            return longitude(value)
        except ValueError:
            msg = self.error_messages['invalid'] % value
            raise exceptions.ValidationError(msg)


class LatLngField(odin.Field):
    """
    Field that contains a lat/long pair.
    """
    default_error_messages = {
        'invalid': "'%s' value must be a (latitude, longitude).",
    }

    def to_python(self, value):
        if value in EMPTY_VALUES:
            return
        try:
            return latlng(value)
        except ValueError:
            msg = self.error_messages['invalid'] % value
            raise exceptions.ValidationError(msg)


class PointField(odin.Field):
    """
    Field that contains a point in cartesian space. This can be either 2D (on a plain) or 3D (includes a z-axis).
    """
    default_error_messages = {
        'invalid': "'%s' value must be a (latitude, longitude).",
    }

    def to_python(self, value):
        if value in EMPTY_VALUES:
            return
        try:
            return point(value)
        except ValueError:
            msg = self.error_messages['invalid'] % value
            raise exceptions.ValidationError(msg)