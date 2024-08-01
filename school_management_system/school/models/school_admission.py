# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class StudentAdmission(models.Model):
    _name = 'school.admission'
    _description = 'Admission detail'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'student_full_name'

    # name_seq = fields.Char(string="Student number", copy="False", default="New")
    student_full_name = fields.Char(string='Full Name', compute='_compute_fullname')
    first_name = fields.Char(help='Students first name')
    last_name = fields.Char(help='Students last name')
    # gender=fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    enrollment_no = fields.Char(help='student unqiue number', copy="False")
    registration_date = fields.Date(default=fields.date.today())
    admission_line_ids = fields.One2many("admission.line", "school_reg_id")
    get_student_reference = fields.Many2one('school.student', string="Student Refernce")
    full_name = fields.Char(string='Refrence Full Name', related="get_student_reference.full_name")
    dob = fields.Date(help='Students dob', related="get_student_reference.dob")
    ad_ids = fields.Many2one('school.standard')
    admin_student_address=fields.Char(string="Address")
    admin_statusbar=fields.Selection([('draft','Draft'),('in process','In Process'),('done','Done'),('cancel','Cancelled')],default='draft',string='status',required=True)
    # student_count = fields.Integer(compute='_compute_student_count')

# Button which is putted in the status bar
    def action_in_process(self):
        for rec in self:
            rec.admin_statusbar = 'in process'

    def action_done(self):
        for rec in self:
            rec.admin_statusbar = 'done'

    def action_cancel(self):
        for rec in self:
            rec.admin_statusbar='cancel'




    def action_open_admission(self):
        print(("heloo smART BUTTON---------------------------------"))
#Unlink Method in odoo
    # def unlink(self):
    #     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #     return super(StudentAdmission,self).unlink()

#This is the copy function
#in this i have used in the admission section in which the user make the duplicate of any student they can  easily known that they hAVE MAKE which stduent record  duplicae from the record.    # @api.returns('self', lambda value: value.id)
    # def copy(self, default=None):
    #     if default is None:
    #         default = {}
    #
    #     if not default.get('enrollment_no'):
    #         default['enrollment_no'] = self.student_full_name + "(copy)"
    #     milestone_copy = super(StudentAdmission, self).copy(default)
    #     return milestone_copy



# sql constrains :- In this Constrains if the first name is repeated by the user to enter than its show the error or we can say constrains
#     _sql_constraints = [
#         ('first_name', 'unique (first_name)', 'Name must be unique.')
#     ]

    # user_id = fields.Many2one('res.partner' , string="Customer")
    # customer_phone_no = fields.Char(string="Customer Phone No" ,related="user_id.phone")


#This Constraints Is Called Python Constraints
    # check dob according to today date if user enter the date of birth is greater than the today date then they shoe the valdation
    @api.constrains('dob')
    def _check_dob(self):
        if self.dob:
            if self.dob > date.today():
                raise ValidationError(_('You cannot  select dob beacuse the selected dob is not valid.'))

    @api.onchange('afg_id')
    def onchange_student_dob(self):
        if self.afg_id:
            self.dob = self.afg_id.dob
            self.full_name = self.afg_id.full_name

    # @api.onchange('user_id')
    # def onchange_user(self):
    #     if self.user_id:
    #         self.customer_phone_no = self.user_id.phone

    class StudentAdmissionline(models.Model):
        _name = 'admission.line'
        _description = 'Admission Line'

        school_reg_id = fields.Many2one('school.admission', string="School Admission")
        first_name = fields.Char()
        # last_name=fields.Char()
        # dob=fields.Date()

    # @api.depends('first_name','last_name')
    def _compute_fullname(self):
        for rec in self:
            rec.student_full_name = f"{rec.first_name} {rec.last_name}"



        # sequence number which is genertaed each and every time when the new admission is created

    @api.model
    def create(self, vals):
        if vals.get('enrollment_no', 'New') == 'New':
            vals['enrollment_no'] = self.env['ir.sequence'].next_by_code('school.student.sequence') or 'New'
        result = super(StudentAdmission, self).create(vals)                           #After the Super we want to give the class name for which class we are making the create methdd. # here super is used to collect all data from all the models after that it move to forward step.
        print("vals",vals)                                                             # vals is used to show the curent record whic is inserted in mode or we can seee what change swe have made in the the fields of that model
        print("result",result)                                                          # result is used the show the  curent record object .
        return result


    # def _compute_student_count(self):
    #     student_obj = self.env['school.admission'].search_count(
    #         [('id', '=', self.id)])
    #     for record in self:
    #         record.student_count = student_obj.id

    # smart button subject
    def show_subject(self):
        return {
            'name': _('Student'),
            'res_model': 'school.admission',
            'view_mode': 'tree',
            'context': {},
            'domain': [('id', '=', self.id)],
            'target': 'current',
            'type': 'ir.actions.act_window',
        }

