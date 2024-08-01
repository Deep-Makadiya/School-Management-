# -*- coding: utf-8 -*-
{
    'name': "school_management_system",

    'summary': """""",

    'description': """""",
    'author': "Cravit",
    'website': "https://www.cravit.nl",
    'category': 'Uncategorized',
    'sequence': -100,
    'version': '17.0.1.0.0',
    'depends': ['base', 'mail'],

    # always loaded
    'data': [

        'security/test_module_security.xml',
        'security/ir.model.access.csv',
        'report/school_management_system_templeates.xml',
        'report/school_management_system_report.xml',
        'report/faculty_profile_templates.xml',
        'report/faculty_profile_report.xml',


        'Data/student_timetable_cron.xml',
        'wizard/test_wizard_view.xml',
        # 'security/test_module_security.xml',
        'views/school_admission.xml',
        'views/school_student.xml',
        'views/school_faculty.xml',
        'views/school_subject.xml',

        'views/student_timetable.xml',
        'views/teacher_timetable.xml',
        'views/school_standard.xml',
        'views/student_attendance.xml',
        'views/student_exam_attendance.xml',
        'views/student_fees.xml',
        'views/student_mark.xml',
        # 'views/student_mark_views.xml',
        'views/menu.xml',

        # 'wizard/test_wizard_view.xml',
    ],
    'installable': True,
    'application': False,
}
