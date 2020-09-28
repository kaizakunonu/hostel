# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Hostel(models.Model):
    _name = 'hostel.hostel'
    _description = 'hostel.hostel'

    name = fields.Char(string='Hostel name', required=True, index=True)
    warden_name = fields.Char(string='Warden in Charge', required=True, index=True)
    capacity = fields.Integer(string='Hostel\'s carrying capacity', required=True, index=True)
    safe_capacity = fields.Integer(compute="safe_value", store=True,
                                   string='Safe number of residents', index=True)
    description = fields.Text(string='Warden\'s comments', required=True, index=True)

    @api.depends('capacity')
    def safe_value(self):
        for record in self:
            record.safe_capacity = float(record.capacity) * 0.8


class HostelResident(models.Model):
    _name = 'hostel_resident.hostel_resident'
    _description = 'hostel_resident.hostel_resident'

    name = fields.Char(string='Resident name', required=True, index=True)
    registration_no = fields.Char(string='Registration number', required=True, index=True)
