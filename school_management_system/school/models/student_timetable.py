# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Studenttimetable(models.Model):
    _name = 'school.timetable'
    _description = 'Student Timetable data'
    _rec_name = 'teacher_name'

    # name=fields.Char(string="Name")
    Period=fields.Selection([('1','Period 1'),('2','Period 2'),('3','Period 3'),('4','Period 4'),('5','Period 5')])
    # subject=fields.Many2one('school.subject')
    # faculty=fields.Char(help='faculty')
    teacher_name=fields.Many2one('school.faculty' ,string="faculty Name")
    gender=fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    subjects = fields.Many2many('school.subject')
    standard_id=fields.Many2one('school.standard',string="Standard")





#create method in which the user select the gender than at the prefix of the name aacording too gender the prefix is attached
    @api.model
    def create(self,vals):
        res=super(Studenttimetable,self).create(vals)
        # if vals.get('gender') == 'male':
        #     res['name']='Mr.' + " " + res['name']
        # elif vals.get('gender') == 'female':
        #     res['name']='Mrs.'+ " " + res['name']
        # else:
        #     return  res
        print('vals',vals)
        return res
# By faculty name give the faculty gender by selecting the faculty name
    @api.onchange('teacher_name')
    def onchange_faculty_gender(self):
        self.gender=self.teacher_name.gender

# Geting the faculty subject on the basis of the faculty name
    @api.onchange('teacher_name')
    def get_subject_faculty(self):
        if self.teacher_name:
            self.subjects = self.teacher_name.subject_faculty


# Cron Function Call(Scheduler action Function call)
    def remove_scheduler_student_timetable(self):
        print("Kem Palty!!!!!!!")






