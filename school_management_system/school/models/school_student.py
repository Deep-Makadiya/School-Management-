# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError ,  UserError

class StudentData(models.Model):
    _name = 'school.student'
    _description = 'student data'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'Student_first_name'

    full_name=fields.Char(string='Full Name',compute='_compute_fullname' )
    Student_first_name=fields.Many2one('school.admission',string='First Name')
    last_name=fields.Char(related="Student_first_name.last_name",string="Last Name")
    entrollment_no=fields.Char(string="Enrollement")
    dob=fields.Date(help='Students dob')
    age=fields.Char(help='the age of students',string='age',compute='_compute_age')
    std_id = fields.Many2one('school.standard')
    sdfre_ids = fields.One2many('school.admission','get_student_reference')
    get_admin_student_address=fields.Char(string="Student Address")

    attendance_std=fields.Many2one('student.attendance')
    date = fields.Date(string="Date")
    academic_year=fields.Selection([('2020-2021','2020-2021'),('2021-2022','2021-2022'),('2022-2023','2022-2023'),('2023-2024','2023-2024')])
    attendance_Class=fields.Many2one('school.standard',string="Class")
    atten_division=fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C'),('d','D')])
    session=fields.Selection([('Before Noon','BEFORE NOON'),('After noon','AFTER NOON'),('evening ','EVENING')])
    attendance=fields.Selection([('present','Present'),('absent','Absent')])
    reamrks=fields.Char(string="Remarks")


    student_exam = fields.Many2one('student.examattendance')
    exam_attendance=fields.Selection([('present','Present'),('absent','Absent')])
    exam_reamrks=fields.Char(string="Remarks")





    @api.onchange('Student_first_name')
    def get_student_address(self):
        if self.Student_first_name:
            self.get_admin_student_address = self.Student_first_name.admin_student_address

    @api.onchange('Student_first_name')
    def get_student_address(self):
        if self.Student_first_name:
            self.get_admin_student_address = self.Student_first_name.admin_student_address


    @api.onchange('Student_first_name')
    def get_student_entrollement(self):
        if self.Student_first_name:
            self.entrollment_no=self.Student_first_name.enrollment_no

# calculate the age of student according to dob

    @api.depends('dob')
    def _compute_age(self):
        self.age=False
        for rec in self:
            rec.age = relativedelta(date.today(),rec.dob).years



# This Constraints Is called the python constraints this is used for the validation
# this is for validation in which if student selected dob and time when they are taking admission then they cant be able to fill the form
    @api.constrains('dob')
    def _check_dob(self):
        if self.dob:
            if self.dob > date.today():
                raise UserError(_('You cannot  select dob beacuse the selected dob is not valid.'))


# Write the full name on the basisi of firstname + lastname= fullname
    @api.depends('Student_first_name', 'last_name')
    def _compute_fullname(self):
        for rec in self:
            if rec.Student_first_name.first_name and rec.last_name:
                # rec.full_name = f"{rec.first_name} {rec.last_name}"
                  rec.full_name = rec.Student_first_name.first_name + " " + rec.last_name
            else:
                rec.full_name = ""


# object Button putted in School_student_views
    def action_test(self):
        print("Button Clicked !!!!!!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'You Have Successfully Get The Student Detail',
                'type': 'rainbow_man',
            }
        }


    # smart button subject
    def show_subject(self):
        return {
            'name': _('Subjects'),
            'res_model': 'school.student',
            'view_mode': 'tree',
            'context': {},
            # 'domain': [{'subject_ids', 'in', self.subject_ids}],
            'target': 'current',
            'type': 'ir.actions.act_window',
        }

    # def action_view_details(self):
    #     self.ensure_one()
    #     return {
    #         'name': _('Admission Detailss'),
    #         'view_mode': 'list,form',
    #         'res_model': 'school.admission',
    #         'domain': [('student_full_name', '=', self.full_name)],
    #         'res_id': self.id,
    #         'view_id': False,
    #         'type': 'ir.actions.act_window',
    #         'context': {'default_student': self.id}
    #     }




