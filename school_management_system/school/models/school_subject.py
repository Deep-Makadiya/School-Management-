# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SubjectData(models.Model):
    _name = 'school.subject'
    _description = 'subject data'
    _rec_name = 'subject_name'

    subject_name=fields.Char(help='Students subject name')
    subject_code=fields.Char(help='Students subject code')
    # standard=fields.Integer(help='Students Studying in standard')
    # student_id = fields.Many2one('school.student',string='Student')
    faculty_subjectselection=fields.One2many('school.faculty','subject_faculty')
    subjects_standard=fields.Many2one('school.standard')
    # standard=fields.Selection()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # fields.(Char, Float, Integer, Text, Html, Boolean, Monetary, Date, Datetime, Selection, Many2one, One2many, Many2many)
    # 'sale.order', string="Test", store=True/False, compute="method_name", domain, readonly=True/False, help="message"
    # tree, form, search, kanban, graph, pivot
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


    # @api.model
    # def create(self,vals):
    #     res=super(SubjectData,self).create(vals)
    #     print("vals",vals)
    #     # print("res",res)

 