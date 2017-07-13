from openerp.osv import osv, fields
from openerp import tools

class followup_partner_social_support_and_stigma(osv.Model):
	_name = "followuppartner.socialsupport"
	_columns = {
	'visit_date':fields.date('Visit Date'),
	'partner_id': fields.many2one('res.partner', 'Sceening ID'),
	'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'getvisit':fields.selection([('1','As much as I would like'),('2','Less than I would like'),('3','Much less than I would like'),('4','Never')],'1. I get visits from friends and relatives.'),
	'getadvice':fields.selection([('1','As much as I would like'),('2','Less than I would like'),('3','Much less than I would like'),('4','Never')],'2. I get useful advice about important things in my life.'),
	'getchances':fields.selection([('1','As much as I would like'),('2','Less than I would like'),('3','Much less than I would like'),('4','Never')], '3. I get chances to talk to someone about problems at workor with my housework.'),
	'gettotalk':fields.selection([('1','As much as I would like'),('2','Less than I would like'),('3','Much less than I would like'),('4','Never')], '4. I get chances to talk to someone I trust about mypersonal and family problems.'),
	'havepeople':fields.selection([('1','As much as I would like'),('2','Less than I would like'),('3','Much less than I would like'),('4','Never')], '5. I have people who care what happens to me.'),
	'getlove':fields.selection([('1','As much as I would like'),('2','Less than I would like'),('3','Much less than I would like'),('4','Never')], '6. I get love and affection.'),
	'getsupport':fields.selection([('1','As much as I would like'),('2','Less than I would like'),('3','Much less than I would like'),('4','Never')], '7. I get support with house related work.'),
	'gethelp':fields.selection([('1','As much as I would like'),('2','Less than I would like'),('3','Much less than I would like'),('4','Never')], '8. I get / would get help with money in an emergency.'),
	'gettransport':fields.selection([('1','As much as I would like'),('2','Less than I would like'),('3','Much less than I would like'),('4','Never')], '9. I get help when I need transportation.'),
	'helpsick':fields.selection([('1','As much as I would like'),('2','Less than I would like'),('3','Much less than I would like'),('4','Never')], '10. I get help when I am sick.'),
	'relyfina':fields.selection([('1','All of the time'),('2','A lot of the time'),('3','Some of the time'),('4','Not at all')], '11. My family, friends, and / or community rely on me financially.'),
	'relyemot':fields.selection([('1','All of the time'),('2','A lot of the time'),('3','Some of the time'),('4','Not at all')],'12. My family, friends, and /or community rely on me emotionally.'),
	'losefriends':fields.selection([('Strongly_agree','Strongly agree'),('Agree','Agree'),('Disagree','Disagree'),('Strongly_disagree','Strongly disagree')],'13. I would lose friends.'),
	'disownme':fields.selection([('Strongly_agree','Strongly agree'),('Agree','Agree'),('Disagree','Disagree'),('Strongly_disagree','Strongly disagree')],'14. My family would disown or neglect me.'),
	'anoutcast':fields.selection([('Strongly_agree','Strongly agree'),('Agree','Agree'),('Disagree','Disagree'),('Strongly_disagree','Strongly disagree')],'15. My community would treat me like an outcast.'),
	'getsacked':fields.selection([('Strongly_agree','Strongly agree'),('Agree','Agree'),('Disagree','Disagree'),('Strongly_disagree','Strongly disagree')],'16.	I would be treated badly at work or get sacked. (NA)'),
	}
