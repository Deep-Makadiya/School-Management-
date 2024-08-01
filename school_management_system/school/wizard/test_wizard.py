from odoo import models, fields, api, _


class StudentDatawizard(models.TransientModel):
    _name='create.studentdata.wizard'
    _description = 'student data'

    # Student_first_name=fields.Many2one('school.admission',string='First Name')
    # last_name=fields.Char(related="Student_first_name.last_name",string="Last Name")
    first_name = fields.Char(help='Students first name')
    last_name = fields.Char(help='Students last name')


    def student_profile_created(self):
        # print("The Button Is clicked !!!!!!!!xxx")
        vals= {
            'first_name':self.first_name,
            'last_name':self.last_name,
        }
        # print("vals.............",vals)
        self.env['school.admission'].create(vals)
