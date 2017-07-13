from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_partnermedicalhistory(osv.Model):
    _name = "enrollment.partnermedicalhistory"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Screening ID", related='partner_id.name'),
        'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),

        ###################################################
        ##  1. Fever
        ##
        ###################################################
        'fever':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Fever'),

        'fever_no_of_days':fields.char('No of Days'),

        'fever_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'fever ongoing'),

        ###################################################
        ##  2. Fatigue
        ##
        ###################################################

        'fatigue':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Fatigue'),

        'fatigue_no_of_days':fields.char('No of Days'),

        'fatigue_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Fatigue ongoing'),

        ###################################################
        ##  3. Sore throat
        ##
        ###################################################

        'sorethroat':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Sore Throat'),

        'sorethroat_no_of_days':fields.char('No of Days'),

        'sorethroat_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Sore Throat ongoing'),

        ###################################################
        ##  4. Rash
        ##
        ###################################################

        'rash':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Rash'),

        'rash_no_of_days':fields.char('No of Days'),

        'rash_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Rash ongoing'),

        ###################################################
        ##  5. Headache
        ##
        ###################################################

        'headache':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Headache'),

        'headache_no_of_days':fields.char('No of Days'),

        'headache_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Headache ongoing'),

        ###################################################
        ##  6. Shortness of breath or cough
        ##
        ###################################################

        'shortbreath':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Shortness of breath or cough'),

        'shortbreath_no_of_days':fields.char('No of Days'),

        'shortbreath_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Shortness of breath or cough ongoing'),

        ###################################################
        ##  7. Abdominal pain
        ##
        ###################################################

        'abdominalpain':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Abdominal pain'),

        'abdominalpain_no_of_days':fields.char('No of Days'),

        'abdominalpain_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Abdominal pain ongoing'),

        ###################################################
        ##  8. Nausea
        ##
        ###################################################

        'nausea':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Nausea'),

        'nausea_no_of_days':fields.char('No of Days'),

        'nausea_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Nausea ongoing'),

        ###################################################
        ##  9. Vomiting
        ##
        ###################################################

        'vomiting':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Vomiting'),

        'vomiting_no_of_days':fields.char('No of Days'),

        'vomiting_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Vomiting ongoing'),

        ###################################################
        ##  10. Diarrhea
        ##
        ###################################################

        'diarrhea':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Diarrhea'),

        'diarrhea_no_of_days':fields.char('No of Days'),

        'diarrhea_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Diarrhea ongoing'),

        ###################################################
        ##  11. Excessive intestinal gas
        ##
        ###################################################

        'excessiveintestinalgas':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Excessive intestinal gas'),

        'excessiveintestinalgas_no_of_days':fields.char('No of Days'),

        'excessiveintestinalgas_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Excessive intestinal gas ongoing'),

        ###################################################
        ##  12. Increased or decreased urinary output
        ##
        ###################################################

        'inc_or_dec_urinary_output':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Increased or decreased urinary output'),

        'inc_or_dec_urinary_output_no_of_days':fields.char('No of Days'),

        'inc_or_dec_urinary_output_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Increased or decreased urinary output'),

        ###################################################
        ##  13. Muscle weakness or pain
        ##
        ###################################################

        'muscle_weakness_or_pain':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Muscle weakness or pain'),

        'muscle_weakness_or_pain_no_of_days':fields.char('No of Days'),

        'muscle_weakness_or_pain_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Muscle weakness or pain'),

        ###################################################
        ##  14. Swelling of the feet
        ##
        ###################################################

        'swelling_of_the_feet':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Swelling of the feet'),

        'swelling_of_the_feet_no_of_days':fields.char('No of Days'),

        'swelling_of_the_feet_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Swelling of the feet'),

        ###################################################
        ##  15. Joint pain
        ##
        ###################################################

        'jointpain':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Joint pain'),

        'jointpain_no_of_days':fields.char('No of Days'),

        'jointpain_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Joint pain'),

        ###################################################
        ##  16. Bone pain
        ##
        ###################################################

        'bonepain':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Bone pain'),

        'bonepain_no_of_days':fields.char('No of Days'),

        'bonepain_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Bone pain'),

        ###################################################
        ##  17. Bone fracture
        ##
        ###################################################

        'bonefracture':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Bone fracture'),

        'bonefracture_no_of_days':fields.char('No of Days'),

        'bonefracture_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Bone fracture'),

        ###################################################
        ##  18. Numbness or tingling in your hands or feet
        ##
        ###################################################

        'numbness':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Numbness or tingling in your hands or feet'),

        'numbness_no_of_days':fields.char('No of Days'),

        'numbness_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Numbness or tingling in your hands or feet'),

        ###################################################
        ##  19. Others
        ##
        ###################################################

        'others':fields.selection([
            ('yes','Yes'),
            ('no','No'),
            ('dontknow',"Don't know")
            ],'Others'),

        'others_no_of_days':fields.char('No of Days'),

        'others_ongoing':fields.selection([
            ('yes','Yes'),
            ('no','No')
            ],'Others'),

        
        ###################################################
        ##  20. Abused
        ##
        ###################################################
        'abused':fields.selection([
            ('yes','yes'),
            ('no','no'),
            ('dontknow',"Don't know")
            ],'20. abused'),
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
