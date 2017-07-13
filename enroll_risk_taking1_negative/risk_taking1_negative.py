from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class risk_taking_negative(osv.Model):
    _name = "risk.taking.negative"
    _columns = {
    'visitdate':fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
    'ingeneral':fields.integer('a. in general'),
	'financialmatters':fields.integer('b. with financial matters'),
	'yourhealth':fields.integer('c. with your health'),
	'sexualbehaviours':fields.integer('d. In sexual behaviours'),
	'would_you_prefer':fields.selection([
        ('one','1'),
        ('two','2'),
        ('three','3')],
        'Answer'),
    'business1':fields.boolean('Preferred Business 1'),
    'business2':fields.boolean('Preferred Business 2'),
    'business3':fields.boolean('Preferred Business 3'),
    'business4':fields.boolean('Preferred Business 4'),
    'business5':fields.boolean('Preferred Business 5'),
    'business6':fields.boolean('Preferred Business 6'),
    'prefered_business': fields.char('Prefereed choice of business', compute='_compute_choice_business', store=True),
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

    @api.one
    @api.depends('business1','business2','business3','business4','business5','business6')
    def _compute_choice_business(self):
        #self.ensure_one()
        if not (self.business1 or self.business2 or self.business3 or self.business4 or self.business5 or self.business6):
            raise exceptions.Warning('Please choose at least one business!')

        #else
        if self.business1:
            if self.business2 or self.business3 or self.business4 or self.business5 or self.business6:
                raise exceptions.ValidationError('You are not allowed to pick more than one business!')
            self.prefered_business = 'Business 1'

        #else
        if self.business2:
            if self.business1 or self.business3 or self.business4 or self.business5 or self.business6:
                raise exceptions.ValidationError('You are not allowed to pick more than one business!')
            self.prefered_business = 'Business 2'

        #else
        if self.business3:
            if self.business1 or self.business2 or self.business4 or self.business5 or self.business6:
                raise exceptions.ValidationError('You are not allowed to pick more than one business!')
            self.prefered_business = 'Business 3'

        #else
        if self.business4:
            if self.business1 or self.business2 or self.business3 or self.business5 or self.business6:
                raise exceptions.ValidationError('You are not allowed to pick more than one business!')
            self.prefered_business = 'Business 4'

        #else
        if self.business5:
            if self.business1 or self.business2 or self.business3 or self.business4 or self.business6:
                raise exceptions.ValidationError('You are not allowed to pick more than one business!')
            self.prefered_business = 'Business 5'

        #else
        if self.business6:
            if self.business1 or self.business2 or self.business3 or self.business4 or self.business5:
                raise exceptions.ValidationError('You are not allowed to pick more than one business!')
            self.prefered_business = 'Business 6'