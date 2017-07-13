from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_partnerdrugdispensing(osv.Model):

    @api.multi
    @api.depends('partner_id.couple', 'partner_id.ips')
    def _compute_enrollment_id(self):
        self.ensure_one()
        if not(self.partner_id.couple and self.partner_id.ips):
            raise exceptions.ValidationError("Update the Couple and I/P fields for the respondent!")
        #else if
        if self.partner_id.ips == 'I' or self.partner_id.ips == 'i':
            self.enrollment_id = '000' + str(self.partner_id.couple) + 'A'
        #else
        if self.partner_id.ips == 'P' or self.partner_id.ips == 'p':
            self.enrollment_id = '000' + str(self.partner_id.couple) + 'B' 

    _name = "enrollment.partnerdrugdispensing"
    _columns = {

    'visitdate' : fields.date('Visit date'),
    'partner_id': fields.many2one('res.partner', 'Screening ID'),
    'sceening_id': fields.char(string="Screening ID", related='partner_id.name'),
    'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),

    'bottle_return':fields.selection([
        ('never accepted study PrEP','never accepted study PrEP, End of form'),
        ('Enrolled','Enrolled, Go to item 1a.'),
        ], 'Bottle return'),

    'retbottles':fields.char('a. Number of bottles returned'),
    'retpills':fields.char('Number of pills returned'),
    'leftpills':fields.char('Number of pills left at home'),
    'disbottles':fields.char('Number of bottles dispensed'),
    'whynodispense':fields.selection([
        ('ongoingpsdi','i. Ongoing PSDI'),
        ('studystop','ii. Study Stop'),
        ('prepstop','iii. PrEP Stop'),
        ('other', 'iv. Other')
        ], '3. Why were no bottles dispensed?'),
    'specify_other' : fields.char('Specify other'),
    'mems_cap_no':fields.char("MEMS cap number"),
    'mems_data_uploaded' : fields.selection([
        ('yes','Yes'),
        ('no','No')
        ], "4. Were MEMS data uploaded?"),
    'why_not' : fields.selection([
        ('lost/stolen','i. lost/stolen'),
        ('malfunctioning','ii. malfunctioning'),
        ('others','iii. Others')
        ],'a. Why not?'),
    'replacement_cap_dispensed' : fields.selection([
        ('yes','Yes'),
        ('no','No')
        ],'5. Was a replacement cap dispensed today?'),
    'new_cap_no' : fields.char('a. New cap number'),
    'reason_dispensed' : fields.selection([
        ('lost/stolen','i. lost/stolen'),
        ('malfunctioning','ii. malfunctioning'),
        ('others','iii. Others:')
        ],'b. Reason dispensed?'),
    'prev_cap_returned' : fields.selection([
        ('yes','Yes'),
        ('no','No')
        ], "6. Was a previously dispensed cap returned today?"),
    'ret_cap_num' : fields.char('Returned cap number:'),
    'times_opened_med_bottle' : fields.integer('7. Since the last visit, how many times have you or someone else \n \
        opened the your special medication bottle without taking any tablets out of it?'),
    'times_taken_more_than_one_tab' : fields.integer('8. Since the last visit, how many times have you taken more \n \
        than one tablet out of your special medication bottle at a time?'),
    'xtra_tabs_taken' : fields.integer('8a. Since the last visit, how many extra tablets in total have you taken \n \
        out of your special medication bottle? Do not include the tablet taken out to be used that day'),

    } 
