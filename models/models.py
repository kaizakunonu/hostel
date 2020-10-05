# -*- coding: utf-8 -*-

from odoo import models, fields, api


# definition of Hostel class start
class Hostel(models.Model):
    _name = 'hostel.hostel'
    _description = 'Hostel information'

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


# HostelNurse class definition start
class HostelNurse(models.Model):
    _name = 'hostel_nurse.hostel_nurse'
    _description = 'Hostel nurses and/or doctors'

    name = fields.Char(string='Hostel\'s nurse full name', required=True, index=True,
                       help='Write the full name of hostel nurse in charge')
    mobile_no = fields.Char(string='Mobile number', required=True, index=True,
                            help='Write the mobile number of the nurse in charge')
    start_date = fields.Date(string='Contract start date', required=True, index=True,
                             help='Write the employment contract start date')
    end_date = fields.Date(string='Contract end date', required=True, index=True,
                           help='Write the employment contract end date')


######################################
# start of HostelCleaner class #######
######################################
class HostelCleaner(models.Model):
    _name = 'hostel_cleaner.hostel_cleaner'
    _description = 'Hostel Cleaners'

    name = fields.Char(string='Hostel\'s cleaner full name', required=True, index=True,
                       help='Write the full name of hostel cleaner in charge')
    mobile_no = fields.Char(string='Mobile number', required=True, index=True,
                            help='Mobile number of the hostel cleaner')
    start_date = fields.Date(string='Contract start date', required=True, index=True,
                             help='Write the employment contract start date')
    end_date = fields.Date(string='Contract end date', required=True, index=True,
                           help='Write the employment contract end date')


#####################################
# start of HostelResident class #####
#####################################
class HostelResident(models.Model):
    _name = 'hostel_resident.hostel_resident'
    _description = 'Hostel resident information'

    name = fields.Char(string='Hostel resident name', required=True, index=True,
                       help='Write the full name of hostel resident')
    registration_no = fields.Char(string='Resident registration number', required=True, index=True,
                                  help='Write the university registration number of the resident')
    room_no = fields.Integer(string='Resident room number', required=True, index=True,
                             help='Write the number of the room assigned to this resident')
    rent_fee = fields.Float(string='Rent fee', digits=(6, 2), required=True, index=True,
                            help='Enter amount of money paid by the resident as room rent fee')


##############################################
# start of HostelStudentLeader class #########
##############################################
class HostelStudentLeader(models.Model):
    _name = 'hostel_student_leader.hostel_student_leader'
    _description = 'Hostel student leader information'

    name = fields.Char(string='Leader full name', required=True, index=True,
                       help='Write the full name of hostel student leader')
    registration_no = fields.Char(string='Leader registration number', required=True, index=True,
                                  help='Write the university registration number of the leader')
    room_no = fields.Integer(string='Leader room number', required=True, index=True,
                             help='Write the number of the room assigned to this leader')
    mobile_no = fields.Integer(string='Leader mobile number', required=True, index=True,
                               help='Write the number of their mobile phone')
    start_date = fields.Date(string='Tenure start date', required=True, index=True,
                             help='Write the leadership tenure start date')
    end_date = fields.Date(string='Tenure end date', required=True, index=True,
                           help='Write the leadership tenure end date')


#########################################
# start of HostelSecurityGuard class ####
#########################################
class HostelSecurityGuard(models.Model):
    _name = 'hostel_security_guard.hostel_security_guard'
    _description = 'Hostel security guard information'

    name = fields.Char(string='Security guard full name', required=True, index=True,
                       help='Write the full name of hostel security guard')
    mobile_no = fields.Char(string='Mobile number', required=True, index=True,
                            help='Mobile number of the hostel security guard')
    start_date = fields.Date(string='Contract start date', required=True, index=True,
                             help='Write the employment contract start date')
    end_date = fields.Date(string='Contract end date', required=True, index=True,
                           help='Write the employment contract end date')


##########################################
# start of HostelWarden class ############
##########################################
class HostelWarden(models.Model):
    _name = 'hostel_warden.hostel_warden'
    _description = 'Hostel warden information'

    name = fields.Char(string='Warden full name', required=True, index=True,
                       help='Write the full name of hostel warden')
    mobile_no = fields.Char(string='Mobile number', required=True, index=True,
                            help='Mobile number of the hostel warden')
    start_date = fields.Date(string='Contract start date', required=True, index=True,
                             help='Write the employment contract start date')
    end_date = fields.Date(string='Contract end date', required=True, index=True,
                           help='Write the employment contract end date')


###############################################
# start of HostelRoom class, class for showing room ###################
###############################################
class HostelRoom(models.Model):
    _name = 'hostel_room.hostel_room'
    _description = 'Hostel room information'

    name = fields.Integer(string='Room number', required=True, index=True,
                          help='Write the number of the hostel room')
    first_resident = fields.Char(string='Name of first resident', required=True, index=True,
                                 help='Write the name the first resident of the hostel room')
    second_resident = fields.Char(string='Name of second resident', required=True, index=True,
                                  help='Write the name the second resident of the hostel room')
    rent_fee = fields.Float(string='Rent fee', digits=(6, 2), required=True, index=True,
                            help='Write the amount of fee paid by the occupant')
    rented = fields.Boolean(string='Is it occupied?', required=True, default=False, index=True,
                            help='Tick if the room is already rented')
    room_condition = fields.Text(string='Description of the room based on last inspection',
                                 required=True, default='All items are present and working',
                                 index=True, help='Write the current condition of items in the room')


###############################################
# start of HostelToilet class, responsible for Hostel #################
###############################################
class HostelToilet(models.Model):
    _name = 'hostel_toilet.hostel_toilet'
    _description = 'Hostel toilet information'

    name = fields.Char(string='Toilet name', required=True, index=True, default='Boys Block A',
                       help='Write the name of the hostel toilet')
    first_cleaner = fields.Char(string='Name of first cleaner', required=True, index=True,
                                help='Write the name the first cleaner of the hostel toilet')
    second_cleaner = fields.Char(string='Name of second cleaner', required=True, index=True,
                                 help='Write the name the second cleaner of the hostel toilet')
    toilet_condition = fields.Text(string='Description of the toilet based on the last inspection',
                                   required=True, default='All items are present and working',
                                   index=True, help='Write the current condition of items in the toilet')


###################################################
# start of HostelAccommodation class ##############
###################################################
class HostelAccommodation(models.Model):
    _name = 'hostel_service.hostel_service'
    _description = 'hostel_service.hostel_service'

    name = fields.Char(string='Service name', required=True, index=True)
    room_no = fields.Integer(string='Room number', required=True, index=True)
    rent_fee = fields.Float(string='Rent fee', digits=(6, 2), required=True, index=True)
    rented = fields.Boolean(string='Is it occupied?', required=True, default=False, index=True)
