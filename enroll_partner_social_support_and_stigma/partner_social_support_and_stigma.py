from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_partnersocialsupport(osv.Model):
    _name = "enrollment.partnersocialsupport"
    _columns = {  
    'visitdate' : fields.date('Visit date'), 
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
    'getvisit':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'1. I get visits from friends and relatives'),
	'getadvice':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'2. I get useful advice about important things in my life'),
	'getchances':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'3. I get chances to talk to someone about problems at work or with my housework'),
	'gettotalk':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'4. I get chances to talk to someone I trust about my personal and family problems'),
	'havepeople':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'5. I have people who care what happens to me'),
	'getlove':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'6. I get love and affection'),
	'getsupport':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'7. I get support with house related work'),
	'getmoney':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'8. I get/would get help with money in an emergency'),
	'gettransport':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'9. I get help when I need transportation'),
	'getsickhelp':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'10. I get help when I am sick'),
	'relyfinance':fields.selection([('all_time','All of the time'),('a_lot','A lot of the time'),('some_time','Some of the time'),('not_at_all','Not at all')],'11. My family, friends and/or community rely on me financially'),
	'relyemotion':fields.selection([('all_time','All of the time'),('a_lot','A lot of the time'),('some_time','Some of the time'),('not_at_all','Not at all')],'12. My family, friends and/or community rely on me emotionally'),
	'losefriends':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'13. I would lose friends'),
	'disownme':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'14. My family would disown or neglect me'),
	'outcast':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'15. My community would treat me like an outcast'),
	'getsacked':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'16. I would be treated badly at work or get sacked'),
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