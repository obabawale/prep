from openerp.osv import osv, fields
from openerp import tools

class screening_demographics(osv.Model):
    _name = "screening.demographics"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'dateofbirth' : fields.date('1. Date of birth'),
        'age' : fields.integer('Age'),
        'gender' : fields.selection([('male','Male'),('female','Female')],'2. Gender of the respondent'),

        'respondentmarried' : fields.selection([('yes','YES'),('no','NO')],'3. Is the respondent married to the study partner?'),

        'beenmarried' : fields.integer('4. How long has the respondent been married to the study partner?'),
        
        'rank' : fields.selection([
            ('no-co-wife','No Co-wife'),
            ('firstwife','First wife'),
            ('secondwife','Second wife'),
            ('thirdwifeormore','Third wife or more')
            ],'5. What is the rank of the wife'),

        'areyou' : fields.selection([('yes','YES'),('no','NO')],'6. Are you and your study partner married?'),

        'doyou' : fields.selection([('yes','YES'),('no','NO')],'7. Do you and your study partner live together?'),
        'livingtogether' : fields.integer('8. How long have you been living together?'),
        'livingchildren' : fields.integer('9a. How many living children does the respondent have?'),
        'childrenthat' : fields.integer('b. How many children of the respondent had died?'),
        'childrendoes' : fields.integer('c. How many living children does the respondent have with the study partner?'),
        'morechildren' : fields.selection([('yes','YES'),('no','NO')],'10. Does the respondent want more children with the study partner?'),
        'havesex' : fields.date('11. When did you first have sex with your study partner?'),
        'hivstatus' : fields.date("12. How long have you known that your partners HIV status was different from your own?"),
        'ethnicgroup' : fields.char("13. What is the respondents ethnic group or tribe?"),
        'highesteducation' : fields.selection([('No_education','No education'),('Primary','Primary level'),('Secondary','Secondary level'),('Tertiary','Tertiary or higher level'),('Koranic','Koranic education')],'14. What is your highest education level attained?'),
        'monthlyincome' : fields.integer('15. What is the respondent monthly income (average over the last 3 months)?'),
        'electricity' : fields.boolean('a. Is there electricity?'),
        'television' : fields.boolean('b. Is there television?'),
        'refrigerator' : fields.boolean('c. Is there a refrigerator?'),
        'runningwater' : fields.boolean('d. Is there running water?'),
        'concretecement' : fields.boolean('e. Is there concrete/cement floor and walls?'),
        'sleep' : fields.boolean('f. Do you sleep on a mattress?'),
        'household' : fields.boolean('g. Does your household have a car?'),
        'mobile' : fields.boolean('h. Do you have a personal mobile phone?'),
        'rooms' : fields.integer('i. How many rooms are in the house?'),
        'peoplelive' : fields.integer('j. How many people live in the house?'),
        'occupation' : fields.selection([('Not_working','Not working'),('Skilled','Skilled manual'),('Trade/sales','Trade/sales'),('Student','Student'),('Professional','Professional'),('Farmer_fishermen','Farmer, animal raising, fishermen'),('Services','Services')],'17. What is your main occupation?'),
        'oother2' : fields.char('Other: specify'),
        'health_decisions' : fields.selection([
            ('myself','My self'),
            ('mypartner','My partner'),
            ('someoneelse','someone else')],
            '18. Who usually makes decisions regarding your health?'),
        'specify_who' : fields.char("Specify"),
        'permission' : fields.selection([('yes','YES'),('no','NO'),('It_depends','It depends where I go')],'19. If you want to go out, do you need the permission of your partner?'),
        'manybottles' : fields.integer('20. How many bottles of alcoholic drinks does the respondent consume per week?'),
    }
