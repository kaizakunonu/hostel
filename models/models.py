# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Hostel(models.Model):
    _name = 'hostel.hostel'
    _description = 'hostel.hostel'

    name = fields.Char(string='Hostel name', required=True, index=True,
                       help='Write the official hostel name')
    warden_name = fields.Char(string='Warden in Charge', required=True, index=True,
                              help='Write the full name of the warden in charge')
    capacity = fields.Integer(string='Hostel\'s carrying capacity', required=True, index=True,
                              help='Number of beds for the whole hostel')
    safe_capacity = fields.Integer(compute="safe_value", store=True,
                                   string='Safe number of residents', index=True,
                                   help='Allowed number of beds to be occupied by students')
    description = fields.Text(string='Warden\'s comments', required=True, index=True,
                              help='Any other business observed by the warden in charge')

    @api.depends('capacity')
    def safe_value(self):
        for record in self:
            record.safe_capacity = float(record.capacity) * 0.8


class HostelNurse(models.Model):
    _name = 'hostel_nurse.hostel_nurse'
    _description = 'Hostel nurses and/or doctors'

    name = fields.Char(string='Nurse name', required=True, index=True)
    mobile_no = fields.Char(string='Mobile number', required=True, index=True)
    start_date = fields.Date(string='Contract start date', required=True, index=True)


class HostelCleaner(models.Model):
    _name = 'hostel_cleaner.hostel_cleaner'
    _description = 'Hostel Cleaners'

    name = fields.Char(string='Cleaner name', required=True, index=True)
    mobile_no = fields.Char(string='Mobile number', required=True, index=True)
    start_date = fields.Date(string='Contract start date', required=True, index=True)


class HostelResident(models.Model):
    _name = 'hostel_resident.hostel_resident'
    _description = 'hostel_resident.hostel_resident'

    name = fields.Char(string='Resident name', required=True, index=True)
    registration_no = fields.Char(string='Registration number', required=True, index=True)
    room_no = fields.Integer(string='Room number', required=True, index=True)
    rent_fee = fields.Float(string='Rent fee', digits=(6, 2), required=True, index=True)
