from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_indexsocialsupport(osv.Model):
    _name = "enrollment.indexsocialsupport"
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
        'tellpeople':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'13. It is dificult to tell other people about my HIV infection'),
        'feelimmoral':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'14. Being HIV-positive makes me feel immoral'),
        'feelguilty':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'15. I feel guilty that I am HIV-positive'),
        'feelashamed':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'16. I feel ashamed that I am HIV-positive'),
        'feelworthless':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'17. I sometimes feel worthless that I am HIV-positive'),
        'myownfault':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'18. It is my own fault that I am HIV-positive'),
        'hidestatus':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'19. I hide my HIV status from others'),
        'feelcertain':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'20. I feel certain that I can tell all sex partners that I have HIV'),
        } 

    @api.multi
    @api.depends('partner_id.couple', 'partner_id.ips')
    def _compute_enrollment_id(self):
        self.ensure_one()
        if not (self.partner_id.couple and self.partner_id.ips):
            raise exceptions.ValidationError('Please update the couple and I/P fields!')
        #else
        if self.partner_id.ips == 'I' or self.partner_id.ips == 'i':
            self.enrollment_id = '000' + str(self.partner_id.couple) + 'A'
        if self.partner_id.ips == 'P' or self.partner_id.ips == 'p':
            self.enrollment_id = '000' + str(self.partner_id.couple) + 'B'