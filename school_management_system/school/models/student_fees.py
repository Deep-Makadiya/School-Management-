from odoo import models, fields, api, _
from datetime import timedelta

class Studentfees(models.Model):
    _name = 'student.fees'
    _description = 'student Fees'
    _rec_name = 'student_name'

    student_name = fields.Many2one('school.student', string='Student')
    tuition_fee = fields.Float(string='Tuition Fee')
    exam_fee = fields.Float(string='Exam Fee')
    total_fee = fields.Float(string='Total', compute='_compute_total_fee', store=True)

    fees_entrollement=fields.Char(string="Enrollement")
    fees_fullname=fields.Char(string="Full Name")



    @api.depends('tuition_fee', 'exam_fee')
    def _compute_total_fee(self):
        for receipt in self:
            receipt.total_fee = receipt.tuition_fee + receipt.exam_fee


    @api.onchange('student_name')
    def get_student_entrollement(self):
        if self.student_name:
            self.fees_entrollement=self.student_name.entrollment_no



    @api.onchange('student_name')
    def get_student_fullname(self):
        if self.student_name:
            self.fees_fullname=self.student_name.full_name