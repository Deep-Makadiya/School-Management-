# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from datetime import date


class facultydata(models.Model):
    _name = 'school.faculty'
    _description = 'faculty detail'
    _rec_name = 'full_name'

    full_name = fields.Char(string='Full Name', compute='_compute_facultyfullname')
    first_name = fields.Char(help='Students first name')
    last_name = fields.Char(help='Students last name')
    dob = fields.Date(help='Students dob')
    Fac_Regist_no=fields.Char(string="Faculty ID" , copy="false")
    Fac_age=fields.Integer(string="Age" , compute="_compute_FAculty_age",inverse='inverse_compute_FAculty_age' )
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    # address=fields.Text(help='Students address')
    Qualification = fields.Char(help='Students Qualification')
    faculty_id = fields.Many2one('school.standard', string='Standard')
    subject_faculty = fields.Many2many('school.subject', string='Subject')
    joining_date = fields.Date()
    Experince = fields.Char(string='Faculty Experince', compute='_compute_Experince')




    # Search () method is used to fetch or search the records from any specific model.
    # this function is called the search function this search function here i used to search the faaculty on the basis of the gender
    # def check_orm(self):
    #     search_var= self.env['school.faculty'].search([('gender','=','female')])
    #     print("search_var---------------------",search_var)
    #     for rec in search_var:
    #         print("full_name-----------------",rec.full_name,"gender----------------",rec.gender)


    #The search_count() method returns the number of records matching the search domain.
    # this method is called the search_count method .the search_count method is used to count the total number of the id which  is present in the model.
    # def check_orm(self):
    #     search_var = self.env['school.faculty'].search_count([('gender', '=', 'female')])
    #     print("search_var---------------------", search_var)



   #Browse method is used to get record set from database id or list of ids.
   #this method is called the browse method . By using the browse method i can only known the  condition which i have puted in ther function or i can put the id on the browse function which o want to browse the id.
    # def check_orm(self):
    #     search_var = self.env['school.faculty'].browse([('gender', '=', 'female')])
    #     print("search_var---------------------", search_var)


    #The ref() method is a crucial utility for developers seeking to access records based on their XML ID. By providing the xml_id in the format <module.id>, developers can effortlessly retrieve the corresponding record.
    #this function is called the ref function . the ref function is used if any record is made using the xml in external form view than to get that external id we are using the ref function
    # def check_orm(self):
    #     search_var = self.env.ref('school.faculty_data_form_view')
    #     print("search_var---------------------", search_var.type,"name------------",search_var.name)


    #unlink method delete the record based on the given ID
    # Unlink Method in odoo . This unliunk method is used to delete the record from  the model
    # def check_orm(self):
    #     print("HElo------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #     return super(facultydata,self).unlink()


    #The 'copy' method generates a new record that mirrors the exact content of the original record. The line ". copy({'name': 'Duplicate'})" invokes the copy method on the product record.
    # #in this i have used in the faculty section in which the user make the duplicate of any faculty they can  easily known that they hAVE MAKE which faculty record  duplicae from the record.
    # def check_orm(self):
    #     search_var = self.env['school.faculty']
    #     search_var.copy()



    # create function
    #Invoked when a new record is being added to a model

    # def check_orm(self):
    #     create_var = self.env['school.faculty'].create([])
    #     print("create_var------------------------------",create_var)



    #write function
    #Triggered when an existing record is being modified or updated.
    # def check_orm(self):
    #     write_var= self.env['school.faculty'].write([])
    #     print("write_var--------------",write_var)




    # sequence number which is genertaed each and every time when the new admission is created
    @api.model
    def create(self, vals):
        if vals.get('Fac_Regist_no', 'New') == 'New':
            vals['Fac_Regist_no'] = self.env['ir.sequence'].next_by_code('school.faculty.sequence') or 'New'
        result = super(facultydata, self).create(vals)                           #After the Super we want to give the class name
        print("vals",vals)                                                       # vals is used to show the curent record whic is inserted in mode or we can seee what change swe have made in the the fields of that model
        print("result",result)                                                   # result is used the show the  curent record object .
        return result



    # validation error in faculty dob if user selected the date the preseent time
    @api.constrains('dob')
    def _check_dob(self):
        if self.dob:
            if self.dob > date.today():
                raise ValidationError(_('You cannot  select dob beacuse the selected dob is not valid.'))

    # Making THE Faculty Full name on the basis of first_name and last_name
    @api.depends('first_name', 'last_name')
    def _compute_facultyfullname(self):
        for rec in self:
            if rec.first_name and rec.last_name:
                # rec.full_name = f"{rec.first_name} {rec.last_name}"
                rec.full_name = rec.first_name + " " + rec.last_name
            else:
                rec.full_name = ""

    # Counting Faculty Experince on the basis of joinning date
    @api.depends('joining_date')
    def _compute_Experince(self):
        self.Experince = False
        for rec in self:
            rec.Experince = relativedelta(date.today(), rec.joining_date).years

    # Counting Faculty Age on the basis of dob
    @api.depends('dob')
    def _compute_FAculty_age(self):
        self.Fac_age = False
        for rec in self:
            rec.Fac_age = relativedelta(date.today(), rec.dob).years



    # This Function is used to inverse the age function to the the date of birth field in which we enter the age i will get the date of birth according to the age
    @api.depends('Fac_age')
    def inverse_compute_FAculty_age(self):
        today = date.today()
        for rec in self:
            rec.dob = today - relativedelta(years=rec.Fac_age)













    # first_name(char), last_name(char), dob(date), address(text)
    # Qualification(char)

    # standard=fields.Selection()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # fields.(Char, Float, Integer, Text, Html, Boolean, Monetary, Date, Datetime, Selection, Many2one, One2many, Many2many)
    # 'sale.order', string="Test", store=True/False, compute="method_name", domain, readonly=True/False, help="message"
    # tree, form, search, kanban, graph, pivot

