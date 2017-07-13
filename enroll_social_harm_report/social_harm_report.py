from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_socialharm(osv.Model):
    _name = "enrollment.socialharm"
    _columns = {
    'visit_date':fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
    'verbal_abuse':fields.selection([('yes','Yes'),('no','No')],'1. Was the participant verbally abused by his or her study partner?'),
    'verbal_abuse_howoften':fields.char('1a. How often'),
    'phyabuse':fields.selection([('yes','Yes'),('no','No')],'2. Was the participant physically abused by his study partner?'),
    'phyabuse_how_often':fields.char('2a. How often'),
    'econabuse':fields.selection([('yes','Yes'),('no','No')],'3. Was the participant economically abused by his or her study partner?'),
    'otherabuse':fields.selection([('yes','Yes'),('no','No')],'4. Was the participant abused by his or her study partner in any other way (not fitting into the categories of verbal, physical, or economic abuse)?'),
    'breakup':fields.boolean('i. relationship break-up'),
    'lossincome':fields.boolean('ii. loss of income or economic support'),
    'lossofemploy':fields.boolean('iii. loss of employment'),
    'residence':fields.boolean('iv. change of residence'),
    'custody':fields.boolean('v. loss of custody of children'),
    'other':fields.boolean('vi. Other'),
    'none':fields.boolean('vii. None'),
    'describe':fields.text('6. Concisely describe the social harm'),
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