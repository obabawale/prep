from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enroll_index_drugdispensing_record(osv.Model):
    _name = "enroll.index.drugdispensing.record"
    _columns = {
    'visitdate' : fields.date('Visit date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
    'arv_national':fields.selection([('yes','Yes'),('no','No')],'1. At this visit, is the participant eligible \n for ARVs under current national guidelines?'),
    'participant_on_arv':fields.selection([('yes','Yes'),('no','No')],'2. Is the participant already on ARVs?'),
    'arv_where':fields.selection([('onsite','Onsite'),('offsite','Offsite(specify)')],'2a. Where is the participant getting his / her ARVs?'),
    'offsite':fields.char('Offsite'),
    'arv_onsite': fields.selection([('yes','Yes'),('no','No')],'3a. ARVs offered on site '),
    'ref_offsite': fields.selection([('yes','Yes'),('no','No')],'3b. participant referred to off site '),
    'not_offered': fields.selection([('yes','Yes'),('no','No')],'3c. not offered or referred'),
    'explain_not_offered':fields.text('not offered or referred, explain:'),
    'others_explain':fields.text('3d. Others: explain'),
    'accepted_on_site':fields.boolean('4i. accepted on site'),
    'declined_on_site':fields.boolean('4ii. declined on site'),
    'accepted_referral':fields.boolean('4iii. accepted referral'),
    'declined_referral':fields.boolean('4iv. Declined referral'),
    'list_arvs':fields.text('4a. If ARVs accepted on site today, list all ARVs dispensed'),
    'comments':fields.text('5. Comments'),
    }

    @api.one
    @api.depends('partner_id.couple', 'partner_id.ips')
    def _compute_enrollment_id(self):
        if not (self.partner_id.couple and self.partner_id.ips):
            raise exceptions.ValidationError('Please update the couple and I/P fields!')
        #else
        if self.partner_id.ips == 'I' or self.partner_id.ips == 'i':
            self.enrollment_id = '000' + str(self.partner_id.couple) + 'A'
        if self.partner_id.ips == 'P' or self.partner_id.ips == 'p':
            self.enrollment_id = '000' + str(self.partner_id.couple) + 'B'
