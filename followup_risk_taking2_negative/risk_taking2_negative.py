from openerp.osv import osv, fields
from openerp import tools

class followup_risktaking2_negative(osv.Model):
    _name = "followup.risk.taking2.negative"
    _columns = {    
    'visitdate':fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'Imagine':fields.selection([('yes','Yes'),('no','No')],'1. Imagine I have 10 balls, one of which is red and nine of which are black. If you pick one of these balls without looking, how likely it is that you will pick the red ball? Question to the interviewer: did the respondent said 1 chance out of 10, 10%?'),
    'a':fields.char('a. What is the likelihood that your partner is infected with HIV according to you?'),
    'b':fields.char('b. What is the likelihood that you are infected with HIV according to you?'),
    'c':fields.char('c. What is the likelihood that you use a condom with your partner during the next sexual intercourse?'),
    'd':fields.char('d. What is the probability that you will use a condom for each TEN of the next sexual intercourses with your partner?'),
    'e':fields.char('e. What is the probability that you accept to take PrEP?'),
    'f':fields.char('f. What is your probability that you take PrEP consistently i.e. everyday?'),
    'g':fields.char('g. What is the probability that you will experience side effects while on PrEP?'),
    'h':fields.char('h. What is the probability that you will take PrEP consistently if you experience any mild side effects occur?'),
    'i':fields.char('i. If you do not use PrEP consistently, what is the likelihood that you get infected with HIV in the next year according to you?'),
    'j':fields.char('j. If you use PrEP consistently, what is the likelihood that you get infected with HIV in the next year according to you?'),
    'k':fields.char('k. What is the probability that you will use condom in the next 10 sexual intercourses with your infected partner if you take PrEP?'),
    'l':fields.char('l. What is the probability that you become HIV positive in the next 12 months if your partner consistently use ART?'),
    'm':fields.char('m. If you have one unprotected sexual act with your HIV positive partner, what is the probability that you become infected with HIV as a result?'),
    'n':fields.char('n. If you have one protected sexual act with your HIV positive partner, what is the probability that you become infected with HIV as a result?'),
    }