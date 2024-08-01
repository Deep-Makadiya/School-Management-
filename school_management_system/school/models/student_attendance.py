# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Studentattendance(models.Model):
    _name = 'student.attendance'
    _description = 'student Attendance'
    _rec_name = 'date'

    date = fields.Date(string="Date")
    academic_year=fields.Selection([('2020-2021','2020-2021'),('2021-2022','2021-2022'),('2022-2023','2022-2023'),('2023-2024','2023-2024')])
    attendance_Class=fields.Many2one('school.standard',string="Class")
    atten_division=fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C'),('d','D')])
    session=fields.Selection([('Before Noon','BEFORE NOON'),('After noon','AFTER NOON'),('evening ','EVENING')])
    student_attendance_report = fields.One2many('school.student','attendance_std')
    Student_first_name=fields.Char(string="Name")
    attendance=fields.Selection([('present','Present'),('absent','Absent')])
    reamrks=fields.Char(string="Remarks")


    @api.onchange('attendance_Class')
    def get_studentattendance(self):
        if self.attendance_Class:
            self.student_attendance_report=self.attendance_Class.student_ids
            print(self.id)

