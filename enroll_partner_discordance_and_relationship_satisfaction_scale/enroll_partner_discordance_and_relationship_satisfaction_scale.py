from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_partnerdiscordance(osv.Model):
    _name = "enrollment.partnerdiscordance"
    _columns = {
        'visitdate' : fields.date('Visit date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
    	'difficult':fields.selection([('not_at_all','Not at all'),('a_little','A little'),('quite_a_bit','Quite a bit'),('extremely','Extremely')],'1. How difficult was it for you to learn that your partner has HIV while you do not?'),
    	'challenge':fields.selection([('no_challenge','No challenge'),('a_little','A little challenge'),('quite_a_lot','Quite a lot of challenge'),('a_huge','A huge challenge')],'2. How much of a challenge did this discovery create for your relationship?'),
        'managing':fields.selection([('not_well','Not well'),('fairly_well','Fairly well'),('well','Well'),('very_well','Very well')],'3. How well are you managing the situation now?'),
        'discussdivorce':fields.selection([('all_the_time','All the time'),('most_time','Most of the time'),('more_often','More often than not'),('occasionally','Occasionally'),('rarely','Rarely'),('never','Never')],'4. How often do you discuss or have you considered divorce, separation, or terminating your partnership'),
        'leave':fields.selection([('all_the_time','All the time'),('most_time','Most of the time'),('more_often','More often than not'),('occasionally','Occasionally'),('rarely','Rarely'),('never','Never')],'5. How often do you or your partner leave the house after a verbal disagreement?'),
        'goingwell':fields.selection([('all_the_time','All the time'),('most_time','Most of the time'),('more_often','More often than not'),('occasionally','Occasionally'),('rarely','Rarely'),('never','Never')],'6. In general, how often do you think that things between you and your partner are going well?'),
        'confide':fields.selection([('all_the_time','All the time'),('most_time','Most of the time'),('more_often','More often than not'),('occasionally','Occasionally'),('rarely','Rarely'),('never','Never')],'7. Do you confide in your partner?'),
        'everregret':fields.selection([('all_the_time','All the time'),('most_time','Most of the time'),('more_often','More often than not'),('occasionally','Occasionally'),('rarely','Rarely'),('never','Never')],'8. Do you ever regret that you entered into a relationship with your partner?'),
        'quarrel':fields.selection([('all_the_time','All the time'),('most_time','Most of the time'),('more_often','More often than not'),('occasionally','Occasionally'),('rarely','Rarely'),('never','Never')],'9. How often do you and your partner quarrel?'),
        'annoy':fields.selection([('all_the_time','All the time'),('most_time','Most of the time'),('more_often','More often than not'),('occasionally','Occasionally'),('rarely','Rarely'),('never','Never')],'10. How often do you and your partner annoy/upset each other?'),
        'affectionate':fields.selection([('every_day','Every day'),('almost_evryday','Almost every day'),('occasionally','Occasionally'),('rarely','Rarely'),('never','Never')],'11. Are you and your partner affectionate?'),
        'degree_of_happiness':fields.selection([
            ('Extremely unhappy','Extremely unhappy'),
            ('Fairly unhappy','Fairly unhappy'),
            ('A little  unhappy','A little  unhappy'),
            ('Happy','Happy'),
            ('very happy','very happy'),
            ('extremely happy','extremely happy'),
            ('Perfect','Perfect')
            ],'12. Degree of happiness'),
        'ratefeel':fields.char('13. Rate your feelings about the future of your partnership'),
        'anylength':fields.selection([('strongly_agree','strongly agree'),('agree','agree'),('disagree','disagree'),('strongly_disagree','strongly disagree')],'14. I want desperately for the partnership to succeed and would go almost any lenght to see that it does'),
        'allIcan':fields.selection([('strongly_agree','strongly agree'),('agree','agree'),('disagree','disagree'),('strongly_disagree','strongly disagree')],'15. I want very much for my partnership to succeed and will do all I can to see that it does'),
        'myfairshare':fields.selection([('strongly_agree','strongly agree'),('agree','agree'),('disagree','disagree'),('strongly_disagree','strongly disagree')],'16. I want very much for my partnership to succeed and will do my fair share to see that it does'),
        'muchmore':fields.selection([('strongly_agree','strongly agree'),('agree','agree'),('disagree','disagree'),('strongly_disagree','strongly disagree')],'17. It would be nice if my partnership succeeded, but I can\'t do much more than I am doing now to help it succeed'),
        'anymore':fields.selection([('strongly_agree','strongly agree'),('agree','agree'),('disagree','disagree'),('strongly_disagree','strongly disagree')],'18. It would be nice if my partnership succeeded, but I refuse to do any more than I am doing now to keep it going'),
        'nomore':fields.selection([('strongly_agree','strongly agree'),('agree','agree'),('disagree','disagree'),('strongly_disagree','strongly disagree')],'19. My partnership can never succeed, and there is no more than I can do to keep it going'),
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
