# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class standardData(models.Model):
    _name = 'school.standard'
    _description = 'student standard'
    _rec_name = 'standard'

    standard = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'),('4', '4'), ('5', '5'), ('6', '6'),('7', '7'), ('8', '8'), ('9', '9'),('10', '10'), ('11', '11'), ('12', '12')])
    division=fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C'),('d','D')])
    student_ids = fields.One2many('school.student','std_id')
    admin_ids=fields.One2many('school.admission','ad_ids',string="Admin student")
    faculty_ids=fields.One2many('school.faculty','faculty_id')
    faculty_table=fields.One2many('teacher.timetable','teach_time')
