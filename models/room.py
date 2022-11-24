from odoo import fields, models


class Rooms(models.Model):
    _name = "rooms.model"
    _rec_name = 'room_name'
    _description = "Contains all rooms"

    room_name = fields.Char(string="Room's name")





