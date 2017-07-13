from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_partnerphysicalexamination(osv.Model):
    _name = "enrollment.partnerphysicalexamination"
    _columns = {
        'visitdate': fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
        'height': fields.char('1. Height (Enrollment only)'),
        'weight': fields.char('2. Weight'),
        'temperature': fields.char('3. Temperature'),
        'bloodpressure': fields.char('4. Blood Pressure'),
        'resprate': fields.char('5. Respiratory Rate'),
        'pulserate': fields.char('6. Pulse Rate'),
        'gud': fields.selection([('yes','Yes'),('no','No'),('notdone','Not done')],'7. Genital ulcer disease (GUD)'),
        "vaginitis": fields.selection([('yes','Yes'),('no','No'),('notdone','Not done')],'8. Vaginitis or vaginal discharge'),
        'cervicitis' : fields.selection([('yes','Yes'),('no','No'),('notdone','Not done')],'9. Cervicitis or cervical discharge'),
        'pelvic': fields.selection([('yes','Yes'),('no','No'),('notdone','Not done')],'10. Pelvic inflammatory disease (PID)'),
        'urethritis': fields.selection([('yes','Yes'),('no','No'),('notdone','Not done')],'11. Urethritis or urethral discharge'),
        'circumcision_status':fields.selection([
            ('fullycircum','Fully circumcised'),
            ('partiallycircum','Partially circumcised'),
            ('notcircum','Not circumcised')
            ], '12. Circumcision status'),
        'treatforgen': fields.selection([('yes','Yes'),('no','No')],'13. Treatment given for a genital tract infection'),
        'list': fields.char('A. List medications:'),
        'gingivitis': fields.boolean('gingivitis/periodontitis'),
        'thrush': fields.boolean('Thrush'),
        'ulcer': fields.boolean('Ulcer'),
        'oralhair': fields.boolean('oral hairy leukoplakia'),
        'kaposi': fields.boolean('Kaposi Sarcoma'),
        'others': fields.char('Others:'),
        'tenderness':fields.selection([('yes','Yes'),('no','No')],'15. Abdominal tenderness'),
        'hepatomegaly':fields.selection([('yes','Yes'),('no','No')],'16. Hepatomegaly'),
        'splenomegaly':fields.selection([('yes','Yes'),('no','No')],'17. Splenomegaly'),
        'jaundice':fields.selection([('yes','Yes'),('no','No')],'18. jaundice'),
        'peripheral':fields.selection([('yes','Yes'),('no','No')],'19. Peripheral edema'),
        'othersigns':fields.selection([('yes','Yes'),('no','No')],'20. Other physical signs'),
        'specifysigns':fields.selection([('yes','Yes'),('no','No')],'20a. Specify other signs'),
        'zoster':fields.boolean('Zoster'),
        'urticaria':fields.boolean('urticaria'),
        'macular':fields.boolean('diffuse macular, maculopapular, or morbilliform rash'),
        'lesions':fields.boolean('target lesions'),
        'others_2':fields.boolean('Others'),
        'lymphenlarg':fields.selection([('yes','Yes'),('no','No')],'22. Lymph node enlargement?'),
        'site_of_lymphnode':fields.selection([
            ('cervical','Cervical'),
            ('inguinal','Inguinal'),
            ('auxillary','Auxillary'),
            ('other','Others')
            ],'a. site(s) of lymp node'),        
        'specify':fields.char('Others (specify)'),
        'lymphnode': fields.char('b. Size of largest lymph node'),
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

