# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import timedelta

class Studentexamattendance(models.Model):
    _name = 'student.examattendance'
    _description = 'student ExamAttendance'
    _rec_name = 'exam_academic_year'


    exam_academic_year=fields.Selection([('2020-2021','2020-2021'),('2021-2022','2021-2022'),('2022-2023','2022-2023'),('2023-2024','2023-2024')])
    exam_standard=fields.Many2one('school.standard',string="class")
    exam_division=fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C'),('d','D')])
    exam_name=fields.Selection([('mid sem','Mid Sem'),('half year','Half Year'),('final year','Final Year')])
    exam_subject=fields.Many2one('school.subject',string="Subject")
    exam_starttime=fields.Datetime(string="Start Time", required=True)
    exma_endtime=fields.Datetime(string="End Time",store=True,readonly=True,compute='_compute_end_time')
    exam_student = fields.One2many('school.student','student_exam')
    Student_first_name=fields.Char(string="Name")
    exam_attendance=fields.Selection([('present','Present'),('absent','Absent')])
    exam_reamrks=fields.Char(string="Remarks")



    @api.depends('exam_starttime')
    def _compute_end_time(self):
        for exam in self:
            if exam.exam_starttime:
                exam_starttime = fields.Datetime.from_string(exam.exam_starttime)
                exma_endtime = exam_starttime + timedelta(hours=1)  # Assuming exam duration is 1 hour, adjust as needed
                exam.exma_endtime = exma_endtime





    @api.onchange('exam_standard')
    def get_student_examattendance(self):
        if self.exam_standard:
            self.exam_student=self.exam_standard.student_ids