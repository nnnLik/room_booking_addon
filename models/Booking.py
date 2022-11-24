from odoo import models, fields


class Booking(models.Model):
    _name = 'booking.model'
    _rec_name = 'title'
    _description = 'Contains users already booked rooms'

    title = fields.Char(string="Title")

    name_ids = fields.Many2one('res.users', 'Creator')
    room_name_ids = fields.Many2one('rooms.model', "Room's name")

    start_data = fields.Datetime(string="Start of booking")
    end_data = fields.Datetime(string="End of booking")
