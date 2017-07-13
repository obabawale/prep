from openerp.osv import osv, fields
from openerp import tools

class followup_demographics(osv.Model):
    _name = "followup.demographics"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'resgender' : fields.selection([('male','Male'),('female','Female')],'Gender of respondent'),
        'marriedto' : fields.selection([('yes','YES'),('no','NO')],'Is the respondent marriedto the study partner?'),
        'howlong' : fields.char('How long has the respondent been married tothe study partner?'),
        'ifmale' : fields.selection([('nocowife', 'No co-wife'),('firstwife','First wife'),('secondwife', "Second Wife"),('thirdormore','Third wife or more')],'If MALE: What is the rank of the wife\'s respondent among his co-wives?'),
		'iffemale' : fields.selection([('nocowife', 'No co-wife'),('firstwife','First wife'),('secondwife', "Second Wife"),('thirdormore','Third wife or more')],'If FEMALE: What is the rank of the respondent among her co-wives?'),
        'areyoumarried' : fields.selection([('yes', "Yes"),('no','No')],'Are you and your study partner married?'),
        'livetogether' : fields.selection([('yes','Yes'),('no','No')],'Do you and your study partner live together?'),
        'howlong2geda' : fields.char('How long have you been living together?'),
        'livingchild' : fields.char('How many living children does the respondent have?'),
        'deadchild' : fields.char('How many children that the respondent had died?'),
        'howmanyliving' : fields.char('How many living children does the respondent have with the study partner?'),
        'wantmore' : fields.selection([('no','No'),('yes', 'Yes')],'Does the respondent want more children with study partner?'),
        'firstsex' : fields.date('When did you first have sex with your study partner?'),
        'knowhowlong' : fields.date('How long have you known that your partners HIV status was different from your own?'),
        'ethnic' : fields.char('What is the respondents ethnic group or tribe'),
        'educationlevel' : fields.selection([('noeducation','No education'),('primary','Primary level'),('tertorhigher','Tertiary or higher level'),('koranic','Koranic education'),('secondary','Secondary level')],'What is your highest education level attained?'),
        'income' : fields.char('What is the respondent monthly income(average over the last 3 months)?'),
        'house' : fields.selection([('yes','Yes'),('no','No')],'In the respondents house:'),
        'electricity' : fields.selection([('yes','Yes'),('no','No')],'Is there electricity?'),
        'television' : fields.selection([('yes','Yes'),('no','No')],'Is there television?'),
        'refrigerator' : fields.selection([('yes','Yes'),('no','No')],'Is there refrigerator?'),
        'runningwater' : fields.selection([('yes','Yes'),('no','No')],'Is there running water?'),
        'concrete/cement' : fields.selection([('yes','Yes'),('no','No')],'Is there concrete/cement floor and walls?'),
        'mattress' : fields.selection([('yes','Yes'),('no','No')],'Do you sleep on a mattress?'),
        'haveacar' : fields.selection([('yes','Yes'),('no','No')],'Does your household have a car?'),
        'mobilephone': fields.selection([('yes','Yes'),('no','No')],'Do you have a personal mobile phone?'),
       	'roomsinthehouse' : fields.char("How many rooms are in the house?"),
       	'peopleinthehouse' : fields.char('How many people live in the house?'),
       	'occupation' : fields.selection([('not_working','Not working'),('skilledmanual','Skilled manual'),('trades','Trades/Sales'),('student', 'Student'),('professinal','Professional'),('farmer','Farmer, animal raising, fishermen')],'What is your main occupation?'), 
       	'other': fields.char('Other: specify'),
       	'healthdecisions': fields.selection([('myself','Myself'),('my_partner','My partner'),('someonelse',' Someone else')],'Who usually makes decisions regarding your health?'),
       	'goout':fields.selection([('no','No'),('yes','Yes'),('itdepends','It depends where I go')],'If you want to go out, do you need the permission of your partner?'),      	
        'noofdrink': fields.char('How many bottles of drink does the respondent consume per week?'),
    
    } 
