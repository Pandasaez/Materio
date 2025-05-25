from django.views.generic import TemplateView
from .models import College, Organization, OrgMember, Program, Student
from web_project import TemplateLayout
from django.shortcuts import render
from django.db.models.functions import TruncDate
from django.db.models import Count
import json


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to dashboards/urls.py file for more pages.
"""


class DashboardsView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['colleges_count'] = College.objects.count()
        context['organizations_count'] = Organization.objects.count()
        context['programs_count'] = Program.objects.count()
        context['students_count'] = Student.objects.count()
        
        
        
        students = Student.objects.select_related('program').all()[:8]

        context['student_data1'] = {
            'firstname': students[0].firstname,
            'middlename': students[0].middlename,
            'lastname': students[0].lastname,
            'student_id': students[0].student_id,
            'program_name': students[0].program.prog_name,
        }
        
        context['student_data2'] = {
            'firstname': students[1].firstname,
            'middlename': students[1].middlename,
            'lastname': students[1].lastname,
            'student_id': students[1].student_id,
            'program_name': students[1].program.prog_name,
        }
        
        context['student_data3'] = {
            'firstname': students[2].firstname,
            'middlename': students[2].middlename,
            'lastname': students[2].lastname,
            'student_id': students[2].student_id,
            'program_name': students[2].program.prog_name,
        }
        
        context['student_data4'] = {
            'firstname': students[3].firstname,
            'middlename': students[3].middlename,
            'lastname': students[3].lastname,
            'student_id': students[3].student_id,
            'program_name': students[3].program.prog_name,
        }
        
        context['student_data5'] = {
            'firstname': students[4].firstname,
            'middlename': students[4].middlename,
            'lastname': students[4].lastname,
            'student_id': students[4].student_id,
            'program_name': students[4].program.prog_name,
        }
        
        context['student_data6'] = {
            'firstname': students[5].firstname,
            'middlename': students[5].middlename,
            'lastname': students[5].lastname,
            'student_id': students[5].student_id,
            'program_name': students[5].program.prog_name,
        }
        
        context['student_data7'] = {
            'firstname': students[6].firstname,
            'middlename': students[6].middlename,
            'lastname': students[6].lastname,
            'student_id': students[6].student_id,
            'program_name': students[6].program.prog_name,
        }
        
        context['student_data8'] = {
            'firstname': students[7].firstname,
            'middlename': students[7].middlename,
            'lastname': students[7].lastname,
            'student_id': students[7].student_id,
            'program_name': students[7].program.prog_name,
        }
        
        
        daily_counts = (
            Student.objects
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('date')
        )
        context['student_chart_labels'] = json.dumps([str(item['date']) for item in daily_counts])
        context['student_chart_data'] = json.dumps([item['count'] for item in daily_counts])
        return context
