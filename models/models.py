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


#####################################################
# HostelNurse class definition start ################
#####################################################

class HostelNurse(models.Model):
    _name = 'hostel_nurse.hostel_nurse'
    _description = 'Hostel nurse and/or doctor information'

    name = fields.Char(string='Nurse full name', required=True, index=True,
                       help='Write the full name of hostel nurse in charge')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
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
    _description = 'Hostel Cleaner information'

    name = fields.Char(string='Cleaner full name', required=True, index=True,
                       help='Write the full name of hostel cleaner in charge')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
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

    name = fields.Char(string='Resident full name', required=True, index=True,
                       help='Write the full name of hostel resident')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
    college = fields.Char(string='Resident college', required=True, index=True,
                          help='Write the name of the college the resident is attending')
    registration_no = fields.Char(string='Resident registration number', required=True, index=True,
                                  help='Write the university registration number of the resident')
    mobile_no = fields.Char(string='Resident mobile number', required=True, index=True,
                            help='Write the cellular phone number of the resident')
    room_no = fields.Integer(string='Resident room number', required=True, index=True,
                             help='Write the number of the room assigned to this resident')
    rent_fee = fields.Float(string='Rent fee', digits=(6, 2), required=True, index=True,
                            help='Enter amount of money paid by the resident as room rent fee')
    start_date = fields.Date(string='Residence start date', required=True, index=True,
                             help='Write the residence contract start date')
    end_date = fields.Date(string='Residence end date', required=True, index=True,
                           help='Write the residence contract end date')


##############################################
# start of HostelStudentLeader class #########
##############################################
class HostelStudentLeader(models.Model):
    _name = 'hostel_student_leader.hostel_student_leader'
    _description = 'Hostel student leader information'

    name = fields.Char(string='Leader full name', required=True, index=True,
                       help='Write the full name of hostel student leader')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
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
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
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
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
    mobile_no = fields.Char(string='Mobile number', required=True, index=True,
                            help='Mobile number of the hostel warden')
    start_date = fields.Date(string='Contract start date', required=True, index=True,
                             help='Write the employment contract start date')
    end_date = fields.Date(string='Contract end date', required=True, index=True,
                           help='Write the employment contract end date')


###############################################
# start of HostelRoom class ###################
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
# start of HostelToilet class #################
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


###############################################
# start of HostelStore class ##################
###############################################
class HostelStore(models.Model):
    _name = 'hostel_store.hostel_store'
    _description = 'Hostel store information'

    name = fields.Char(string='Store name', required=True, index=True, default='Boys Block A',
                       help='Write the name of the hostel store')
    first_cleaner = fields.Char(string='Name of first cleaner', required=True, index=True,
                                help='Write the name the first cleaner of the hostel store')
    second_cleaner = fields.Char(string='Name of second cleaner', required=True, index=True,
                                 help='Write the name the second cleaner of the hostel store')
    toilet_condition = fields.Text(string='Description of the store based on the last inspection',
                                   required=True, default='All items are present and working',
                                   index=True, help='Write the current condition of items in the toilet')


###################################################
# start of HostelAccommodation class ##############
###################################################
class HostelAccommodation(models.Model):
    _name = 'hostel_accommodation.hostel_accommodation'
    _description = 'Hostel accommodation information'

    name = fields.Char(string='Accommodation Type', required=True, index=True,
                       help='Write the accommodation season, e.g 1st semester 2019/20')
    rent_fee_per_resident_per_bed = fields.Float(string='Daily rent fee per resident per bed',
                                                 digits=(6, 2), required=True, index=True,
                                                 help='Write the daily bed rent fee per resident')
    start_date = fields.Date(string='Season start date', required=True, index=True,
                             help='Write the accommodation season start date')
    end_date = fields.Date(string='Season end date', required=True, index=True,
                           help='Write the accommodation season  end date')
    # format = '%Y-%m-%d'
    # initial_date = str(start_date)
    # final_date = str(end_date)
    # start = datetime.strptime(initial_date, format)
    # end = datetime.strptime(final_date, format)
    # days = str((end - start).days)
    # number_of_residence = end_date.days - start_date.days
    number_of_rooms = fields.Integer(string='Number of rooms', required=True, index=True,
                                     help='Write the number of rooms for the hostel')
    #  revenue = fields.Float(string='Season revenue', compute='', required=True, index=True,
    #     help='This figure represents the total revenue from '
    #   'hostel accommodation')
    # season_payment = fields.Float(string='Season payment', compute='payment_amount', required=True,
    #                              index=True, store=True,
    #                             help='This figure represents the total revenue '
    #                                  'from hostel accommodation')


# @api.depends('rent_fee_per_resident_per_bed', 'days')
# def payment_amount(self):
#    for record in self:
#       record.season_payment = record.number_of_residence * record.days


###############################################################
#  security service ###########################################
###############################################################

class Security(models.Model):
    _name = 'hostel_security.hostel_security'
    _description = 'Hostel security information'

    name = fields.Char('Security service incidence')
    occurrence_date = fields.Date('When did it happen', required=True)


###############################################################
#  health service ###########################################
###############################################################

class Health(models.Model):
    _name = 'hostel_health.hostel_health'
    _description = 'Hostel health information'

    name = fields.Char('Health item name')
    how_many = fields.Integer('Amount required', required=True)
    price_per_item = fields.Float('Buying price', required=True)
    total = fields.Float('Total cost', compute='calculate_total', store=True)

    @api.depends('how_many', 'price_per_item')
    def calculate_total(self):
        for record in self:
            record.total = record.how_many * record.price_per_item


###############################################
# HostelCounselling class start ###############
###############################################
class HostelCounselling (models.Model):
    _name = 'hostel_counselling.hostel_counselling'
    _description = 'Hostel counselling information'

    name = fields.Char('Session name', required=True, index=True)
    start_date = fields.Date('Starting date', required=True, index=True)
    end_date = fields.Date('End date', required=True, index=True)
    numbers = fields.Integer('Number of participants', required=True, index=True)

    ###############################################
    # HostelSport class start ###############
    ###############################################
    class HostelSport(models.Model):
        _name = 'hostel_sport.hostel_sport'
        _description = 'Hostel sport information'

        name = fields.Char('Sport name', required=True, index=True)
        start_date = fields.Date('Starting date', required=True, index=True)
        end_date = fields.Date('End date', required=True, index=True)
        numbers = fields.Integer('Number of participants', required=True, index=True)

