from openerp.osv import osv, fields
from openerp import tools

class followupindex_socialsupport(osv.Model):
    _name = "followupindex.socialsupport"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'getvisit':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'I get visits from friends and relatives'),
        'getadvice':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'I get useful advice about important things in my life'),
        'getchances':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'I get chances to talk to someone about problems at work or with my housework'),
        'gettotalk':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'I get chances to talk to someone I trust about my personal and family problems'),
        'havepeople':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'I have people who care what happens to me'),
        'getlove':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'I get love and affection'),
        'getsupport':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'I get support with house related work'),
        'getmoney':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'I get/would get help with money in an emergency'),
        'gettransport':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'I get help when I need transportation'),
        'getsickhelp':fields.selection([('as_much','As much as I would like'),('less_than','Less than I would like'),('much_less','Much less than I would like'),('never','Never')],'I get help when I am sick'),
        'relyfinance':fields.selection([('all_time','All of the time'),('a_lot','A lot of the time'),('some_time','Some of the time'),('not_at_all','Not at all')],'My family, friends and/or community rely on me financially'),
        'relyemotion':fields.selection([('all_time','All of the time'),('a_lot','A lot of the time'),('some_time','Some of the time'),('not_at_all','Not at all')],'My family, friends and/or community rely on me emotionally'),
        'tellpeople':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'It is dificult to tell other people about my HIV infection'),
        'feelimmoral':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'Being HIV-positive makes me feel immoral'),
        'feelguilty':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'I feel guilty that I am HIV HIV-positive'),
        'feelashamed':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'I feel ashamed that I am HIV-positive'),
        'feelworthless':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'I sometimes feel worthless that I am HIV-positive'),
        'myownfault':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'It is my own fault that I am HIV-positive'),
        'hidestatus':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'I hide my HIV status from others'),
        'feelcertain':fields.selection([('strongly_agree','Strongly agree'),('agree','Agree'),('disagree','Disagree'),('strongly_disagree','Strongly disagree')],'I feel certain that I can tell all sex partners that I have HIV'),
    } 
