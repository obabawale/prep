from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_partnerpreventionpref(osv.Model):
    _name = "enrollment.partnerpreventionpref"
    _columns = {
        'visitdate' : fields.date('Visit date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
        'noconcers' : fields.boolean('no concerns?'),
        'notwilling' : fields.boolean('not willing to take if there is no benefit for me'),
        'iwilldie' : fields.boolean('taking ARVs means I will die soon'),
        'sideffect' : fields.boolean('side effects'),
        'pillburden' : fields.boolean('Pill burden will be too great for too long'),
        'maybeforced' : fields.boolean('I may be forced to disclose'),
        'stigmaconcerns' : fields.boolean('concerns about stigma'),
        'resistmaycom' : fields.boolean('resistance may come sooner'),
        'others' : fields.char('Others:'),

        'prefer_for_hiv_prevention' : fields.selection([
            ('start on ARVs','start on ARVs'),
            ('have my partner use PrEP','have my partner use PrEP'),
            ('Both PrEP and ARVs','Both PrEP and ARVs')
            ],'2. If you could start on ARVs or your partner could take PrEP, which would you prefer for HIV prevention?'),

        'willbenefit' : fields.boolean('ARVs will benfit my partner in the long term'),
        'usedtodrug' : fields.boolean('my partner is already used to taking study drug every day'),
        'takePrEP' : fields.boolean('I can take PrEP to show support for my partner'),
        'free' : fields.boolean('ARVs are currently free'),
        'keepfrom' : fields.boolean('My partner should do everything possible to keep from giving me HIV'),
        'incharge' : fields.boolean('better for my partner to be in charge of my own HIV prevention'),
        'alreadyon' : fields.boolean('My partner is already using ARVs'),
        "studydrug":fields.boolean('I am already used to taking study drug every day'),
        'trustpart':fields.boolean('I don\'t trust my partner'),
        'others_2' : fields.char('Others:'),
        'noofchildren' : fields.integer('4. How many children would you like to have now or in the nearest future'),

        'plan_to_have_next_child':fields.selection([
            ('currently trying to get pregnant','currently trying to get pregnant'),
            ('currently pregnant/partner pregnant','currently pregnant/partner pregnant'),
            ('within the next 2 years','within the next 2 years'),
            ('More than two years from now','More than two years from now'),
            ('Don\'t know','Don\'t know')
            ],'5. When do you plan to have your next child?'),

        'unprotectedsex' : fields.boolean('timed unprotected sex'), 
        'takeart' : fields.boolean('take PrEP'),
        'prep4partner' : fields.boolean('ART for my partner'),
        'others_3' : fields.boolean('Others:'),
        'fertility' : fields.selection([('yes', 'Yes'),('no','No'),('nopartner','no current partner')],'6. Have you discussed your fertility desires with your current partner'),
        
        'riskofgivinghivtopartner':fields.selection([
            ('High risk','High risk'),
            ('Low risk','Low risk'),
            ('No risk','No risk'),
            ('Moderate risk','Moderate risk'),
            ('Don\'t know','Don\'t know')
            ],'7. In general, what do you think is your risk of giving HIV to your partner?'),
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
