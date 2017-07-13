from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_saferconception(osv.Model):
    _name = "enrollment.saferconception"
    _columns = {
        'visit_date':fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
        'malecircum1':fields.boolean('a. Male circumcision'),
        'artifiinsem1':fields.boolean('b. Artificial insemination'),
        'spermwash1':fields.boolean('c. Sperm washing'),
        'selfinsem1':fields.boolean('d. Self insemination'),
        'usecondoms1':fields.boolean('e. Use condoms except during the most fertile days'),
        'usePrEP1':fields.boolean('f. Use PrEP'),
        'useARVs1':fields.boolean('g. Have my partner use the ARVs'),
        'treatSTI1':fields.boolean('h. Get treatment for STIs'),
        'commet1':fields.boolean('i. Comment'),
        'none1':fields.boolean('j. None'),
        'malecircum2':fields.boolean('a. Male circumcision'),
        'artifiinsem2':fields.boolean('b. Artificial insemination'),
        'spermwash2':fields.boolean('c. Sperm washing'),
        'selfinsem2':fields.boolean('d. Self insemination'),
        'usecondoms2':fields.boolean('e. Use condoms except during the most fertile days'),
        'usePrEP2':fields.boolean('f. Use PrEP'),
        'useARVs2':fields.boolean('g. Have my partner use the ARVs'),
        'treatSTI2':fields.boolean('h. Get treatment for STIs'),
        'commet2':fields.boolean('i. Comment'),
        'none2':fields.boolean('j. None'),
        'malecircum3':fields.boolean('a. Male circumcision'),
        'artifiinsem3':fields.boolean('b. Artificial insemination'),
        'spermwash3':fields.boolean('c. Sperm washing'),
        'selfinsem3':fields.boolean('d. Self insemination'),
        'usecondoms3':fields.boolean('e. Use condoms except during the most fertile days'),
        'usePrEP3':fields.boolean('f. Use PrEP'),
        'useARVs3':fields.boolean('g. Have my partner use the ARVs'),
        'treatSTI3':fields.boolean('h. Get treatment for STIs'),
        'commet3':fields.boolean('i. Comment'),
        'none3':fields.boolean('j. None'),
        'malecircum4':fields.boolean('a. Male circumcision'),
        'artifiinsem4':fields.boolean('b. Artificial insemination'),
        'spermwash4':fields.boolean('c. Sperm washing'),
        'selfinsem4':fields.boolean('d. Self insemination'),
        'usecondoms4':fields.boolean('e. Use condoms except during the most fertile days'),
        'usePrEP4':fields.boolean('f. Use PrEP'),
        'useARVs4':fields.boolean('g. Have my partner use the ARVs'),
        'treatSTI4':fields.boolean('h. Get treatment for STIs'),
        'commet4':fields.boolean('i. Comment'),
        'none4':fields.boolean('j. None'),
        'babyHIV':fields.selection([('yes','Yes'),('no','No'),('dont_know','Don\'t know')],'5. If a woman has HIV, her baby will always be born with HIV'),
        'transmit':fields.selection([('yes','Yes'),('no','No'),('dont_know','Don\'t know')],'6. An HIV infected person taking ARVs is less likely to transmit HIV during sex than an infected person not taking ARVs'),
        'redchances':fields.selection([('yes','Yes'),('no','No'),('dont_know','Don\'t know')],'7. Circumcision reduces the chances that a man can become infected with HIV'),
        'mancircum':fields.selection([('yes','Yes'),('no','No'),('dont_know','Don\'t know')],'8. If a man is circumcised, the woman cannot become infected with HIV from him'),
        'fertile':fields.selection([('yes','Yes'),('no','No'),('dont_know','Don\'t know')],'9. A woman is most fertile about 2 weeks after her period.'),
        'fromsemen':fields.selection([('yes','Yes'),('no','No'),('dont_know','Don\'t know')],"10. Sperm washing is a service offered at some hospitals that can remove HIV from a mans semen so that his partner can become pregnant without getting HIV"),
        'uninfected':fields.selection([('yes','Yes'),('no','No'),('dont_know','Don\'t know')],'11. An HIV uninfected man with an infected female partner can make her pregnant without putting his penis inside (by inserting semen into her vagina with a needle-less syringe).'),
        'negative':fields.selection([('yes','Yes'),('no','No'),('dont_know','Don\'t know')],'12. When the partner of an HIV infected person tests negative, the test has made a mistake.'),
        'withoutcond':fields.selection([('yes','Yes'),('no','No'),('dont_know','Don\'t know')],'13. If an HIV infected man has sex without condoms with an HIV uninfected woman even once, she will definitely become infected with HIV.'),
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

