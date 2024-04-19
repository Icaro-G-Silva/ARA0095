import datetime as dt

from marshmallow import Schema, fields, post_load


class Greenhouse(object):
    def __init__(
        self,
        name,
        address,
        packet_timestamp,
        temperature,
        solar_incidence,
        soil_moisture,
        lamp_status,
        fan_status,
    ):
        self.name = name
        self.address = address
        self.temperature = temperature
        self.solar_incidence = solar_incidence
        self.soil_moisture = soil_moisture
        self.lamp_status = lamp_status
        self.fan_status = fan_status
        self.packet_timestamp = packet_timestamp
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<Greenhouse(name={self.name!r})>".format(self=self)


class GreenhouseSchema(Schema):
    name = fields.Str()
    address = fields.Str()
    temperature = fields.Number()
    solar_incidence = fields.Number()
    soil_moisture = fields.Number()
    lamp_status = fields.Number()
    fan_status = fields.Number()
    packet_timestamp = fields.Str()
    created_at = fields.Date()

    @post_load
    def make_ghInfo(self, data, **kwargs):
        return Greenhouse(**data)
