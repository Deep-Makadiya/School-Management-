from odoo import models, fields, api, _


class studentmark(models.Model):
    _name = "students.marks"
    _description = "Students Marks"

    student_name_id = fields.Many2one('school.student', string='Student')
    exam_name = fields.Char(string="Exam Name")
    class_id = fields.Many2one('school.standard', string="Class")
    total_mark = fields.Integer(string="Total Marks", default="0")
    total_pass_mark = fields.Integer(string="Total Marks", default="33")
    obtain_mark = fields.Integer(string="Obtain Mark")
    total_percentage=fields.Integer(string="Percentage", compute='_compute_total_percentage')

    @api.depends('obtain_mark', 'total_mark')
    def _compute_total_percentage(self):
        for record in self:
            if record.total_mark:
                record.total_percentage = (record.obtain_mark / record.total_mark) * 100
            else:
                record.total_percentage = 0.0