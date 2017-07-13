from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_sexbehaviour(osv.Model):
    _name = "enrollment.sexbehaviour"
    _columns = {
    'visit_date':fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
    'last_sexual_intercouse':fields.selection([
        ('days_ago','Days ago'),
        ('weeks_ago','Weeks ago'),
        ('months_ago','Months ago')
        ],'1. When did you last have sexual intercourse with your study partner?'),
    'use_condom':fields.selection([('yes','Yes'),('no','No')],'A. Did you use condom the last time you had sexual intercourse with your study partner?'),
    'sex_times':fields.char('2. In the last month, how many times did you have sex with your study partner?'),
    'condom_times':fields.char('A. How many times was a condom used?'),
    'sex_individuals':fields.char('3. Besides your partner, how many individuals have you had sex with in the last month?'),
    'new_partners':fields.integer('A. Of these individuals, how many are new sexual partners?'),
    'new_partner_times':fields.integer('B. In the last month, how many times did you have sex with someone other than your study partner?'),
    'times_used_condom':fields.integer('C. How many times was condom used?'),
    'anal_sex':fields.selection([
        ('yes','Yes'),
        ('no','No')
        ],'4. In the past month, did you have anal sex?'),
    'using_birth_control':fields.selection([
        ('yes','Yes'),
        ('no','No')
        ],'5. Are you using any of the following birth control methods? Mark all that apply'),
    'oral':fields.boolean('Oral'),
    'implant':fields.boolean('Implant'),
    'post_menopausal':fields.boolean('Post-menopausal'),
    'iud':fields.boolean('IUD'),
    'tubal_ligation':fields.boolean('Tubal ligation/Hysterectomy'),
    'pregnant':fields.boolean('Pregnant'),
    'injectable':fields.boolean('Injectable'),
    'condom':fields.boolean('Condom'),
    'others':fields.char('Others'),
    'wash_inside_vagina':fields.selection([('yes','Yes'),('no','No')],'6. Do you ever wash the inside of the vagina?'),

    'how_often':fields.selection([
        ('everyday','every day'),
        ('2-6_times_a_week','2-6 times a week'),
        ('Once_a_week','Once a week'),
        ('<once_a_week','< once a week'),
        ],'a. How often do you wash inside the vagina?'),

    'use_to_wash_vagina':fields.selection([
        ('Water','Water'),
        ('soap_and_water','Soap and water'),
        ('other:','Other:'),
        ],'b. What do you use to wash inside the vagina?'),

    'other_used':fields.char('Other'),

    'how_you_wash_vagina':fields.selection([
        ('cloth','cloth'),
        ('finger_only','Finger only'),
        ('other:','Other:'),
        ],'c. How do you wash inside the vagina?'),

    'other':fields.char('Other'),

    'lubrication':fields.selection([('yes','Yes'),('no','No')],'7. Do you use lubrication for sex?'),

    'lubrication_saliva':fields.boolean('saliva'),

    'lubrication_petroleum_jelly':fields.boolean('Petroleum jelly'),

    'lubrication_others':fields.char('others'),
    
    'insert':fields.selection([
        ('yes','Yes'),
        ('no','No')
        ],'8. Do you insert any other substances into the vagina?'),

    'what':fields.char('A. What do you insert?'),

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
    