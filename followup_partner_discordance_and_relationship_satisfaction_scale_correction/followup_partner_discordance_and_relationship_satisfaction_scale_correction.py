from openerp.osv import osv, fields
from openerp import tools

class followup_partnerdiscordance(osv.Model):
    _name = "followup.partnerdiscordance"
    _columns = {
    'visit_date':fields.date("Visit date"),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'howdifficult':fields.selection([('notatall','not at all'),('alittle','a little'),('quiteabit','quite a bit'),('extremely','Extremely')],'1. How difficult was it for you to learn that your partner has HIV while you do not?'),
    'challenge':fields.selection([('nochallenge','no challenge'),("alittlechallenge","A little challenge"),("a lotofchallenge","Quite a lot of challenge"),("ahugechallenge","A huge challenge")],'2. How much of a challenge did this discovery create for your relationship?'),
    'managing':fields.selection([('1','not well'),('2','fairly well'),('3','well'),('4','Very  well')],'3. How well are you managing the situation now?'),
    'separation':fields.selection([('1','All the time'),('2','Most of the time'),('3','More oftenthan not'),('4','Occasionally'),('5','Rarely'),('6','Never')],'4. How often do you discuss or have you considered divorce, separation, or terminating your partnership?'),
    'verbaldisagree':fields.selection([('1','All the time'),('2','Most of the time'),('3','More oftenthan not'),('4','Occasionally'),('5','Rarely'),('6','Never')],'5. How often do you or your partner leave the house after a verbal disagreement?'),
    'goingwell':fields.selection([('1','All the time'),('2','Most of the time'),('3','More oftenthan not'),('4','Occasionally'),('5','Rarely'),('6','Never')],'6. In general, how often do you think that things between you and your partner are going well?'),
    'confidein':fields.selection([('1','All the time'),('2','Most of the time'),('3','More oftenthan not'),('4','Occasionally'),('5','Rarely'),('6','Never')],'7. Do you confide in your partner?'),
    'everregret':fields.selection([('1','All the time'),('2','Most of the time'),('3','More oftenthan not'),('4','Occasionally'),('5','Rarely'),('6','Never')],'8. Do you ever regret that you entered a relationship with your partner?'),
    'quarrel':fields.selection([('1','All the time'),('2','Most of the time'),('3','More oftenthan not'),('4','Occasionally'),('5','Rarely'),('6','Never')],'9. How often do you and your partner quarrel?'),
    'upset':fields.selection([('1','All the time'),('2','Most of the time'),('3','More oftenthan not'),('4','Occasionally'),('5','Rarely'),('6','Never')],'10. How often do you and your partner annoy /upset each other?'),
    'affectionate':fields.selection([('1','every day'),('2','Almost every day'),('3','occasionally'),('4','Rarely '),('5','Never')],'11. Are you and your partner affectionate?'),
    'exunhappy':fields.boolean("Extremely unhappy"),
    'funhappy':fields.boolean("Fairly unhappy"),
    'aliunhappy':fields.boolean("A little unhappy"),
    'unhappy':fields.boolean("Unhappy"),
    'vhappy':fields.boolean("very happy"),
    'exhappy':fields.boolean("extremely happy"),
    'perfect':fields.boolean("Perfect"),
    'goanylength':fields.selection([('1','strongly agree'),('2','agree'),('3','disagree'),('4','strongly disagree')],'i. I want desperately for the partnership to succeed and would go almost any length to see that it does.'),
    'doallican':fields.selection([('1','strongly agree'),('2','agree'),('3','disagree'),('4','strongly disagree')],'ii. I want very much for my partnership to succeed and will do all I can to see that it does.'),
    'willdofair':fields.selection([('1','strongly agree'),('2','agree'),('3','disagree'),('4','strongly disagree')],'iii. I want very much for my partnership to succeed and will domy fair share to see that it does.'),
    'cantdomuch':fields.selection([('1','strongly agree'),('2','agree'),('3','disagree'),('4','strongly disagree')],'iv. It would be nice if my partnership succeeded, but I cant do much more than I am doing now to help it succeed.'),
    'refusetodo':fields.selection([('1','strongly agree'),('2','agree'),('3','disagree'),('4','strongly disagree')],'v. It would be nice if my partnership succeeded, but I refuse to do any more than I am doing now to keep it going.'),
    'neversucceed':fields.selection([('1','strongly agree'),('2','agree'),('3','disagree'),('4','strongly disagree')],'vi. My partnership can never succeed, and there is no more that I can do to keep it going.'),
    } 
