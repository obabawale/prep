from openerp.osv import osv, fields
from openerp import tools, api

class couple_eligibility(osv.Model):
    _name = "couple.eligibility"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'indexgender' : fields.selection([('male','Male'),('female','Female')],'Index Gender:'),
        'partnergender' : fields.selection([('male','Male'),('female','Female')],'Partner Gender:'),
        'ageof' : fields.selection([('4','4'),('1','1'),('0','0')],'Age of HIV-1 uninfected partner:'),
        'numberof' : fields.selection([('2','2'),('1','1'),('0','0')],'Number of children within the couple:'),
        'circumcisionstatus' : fields.selection([('1','1'),('0','0')],'Circumcision status of male HIV-1 uninfected partner:'),
        'marriedand' : fields.selection([('1','1'),('0','0')],'Married and/or cohabitating:'),
        'unprotectedsex' : fields.selection([('1','1'),('0','0')],'Unprotected sex within partnership,prior 30 days:'),
        'plasmaviral' : fields.selection([('3','3'),('1','1'),('0','0')],'HIV-1 plasma viral load, HIV-1 infected partner:'),
        'total' : fields.integer('Total', compute='_calculate_total', store=True),
        'infectedpartner' : fields.char('2. HIV-1 infected partner CD4 count'),
        'couple_eligibility_status' : fields.selection([
            ('didnotcompletescreening','did not complete screening'),
            ('eligiblebutdidnotenroll','eligible but did not enroll'),
            ('eligibleandenrolled','eligible and enrolled'),
            ('noteligible','not eligible')
            ],'3. What is the eligibility status of the couple?'),
        'whynotenroll': fields.char('Why didn\'t the couple enroll?'),
        'indexparticipant' : fields.selection([('Y','Y'),('N','N'),('ND','ND')],'a. Index participant is taking ARVs.'),
        'Partnerparticipant' : fields.selection([('Y','Y'),('N','N'),('ND','ND')],'b. Partner participant does not meet clinical eligibility criteria'),
        'participantdoes' : fields.selection([('Y','Y'),('N','N'),('ND','ND')],'c. Partner participant does not meet renal eligibility criteria'),
        'hashepatitis' : fields.selection([('Y','Y'),('N','N'),('ND','ND')],'d. Partner participant has hepatitis B infection'),
        'ispregnant' : fields.selection([('Y','Y'),('N','N'),('ND','ND')],'e. Partner participant is pregnant or breastfeeding'),
        'tomaintain' : fields.selection([('Y','Y'),('N','N'),('ND','ND')],'f. Participant(s) do not plan to maintain the relationship'),
        'Participantshave' : fields.selection([('Y','Y'),('N','N'),('ND','ND')],'g. Participants have not had sex with each other at least 6 times in the last 3 months.'),
        'otherreason' : fields.selection([('Y','Y'),('N','N'),('ND','ND')],'h. Other reason, including investigator decision. Specify below'),
        } 

    @api.one
    @api.depends('ageof', 'numberof', 'circumcisionstatus', 'marriedand', 'unprotectedsex', 'plasmaviral')
    def _calculate_total(self):
        total = int(self.ageof) + int(self.numberof) + int(self.circumcisionstatus) + int(self.marriedand) + int(self.unprotectedsex) + int(self.plasmaviral)
        self.total = total
