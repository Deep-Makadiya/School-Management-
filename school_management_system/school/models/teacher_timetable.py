# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class teachertimetable(models.Model):
    _name = 'teacher.timetable'
    _description = 'Teacher TimeTable data'
    _rec_name = 'faculty'

    Period=fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    Class=fields.Char(help='Students class')
    section=fields.Selection([('a','A'),('b','B'),('c','C'),('d','D')])
    subjects=fields.Many2one('school.subject')
    faculty=fields.Many2one('school.faculty')
    teach_time=fields.Many2one('school.standard')
