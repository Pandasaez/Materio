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

        if len(students) >= 2:
            context['student_data1'] = {
                'firstname': students[0].firstname,
                'middlename': students[0].middlename,
                'lastname': students[0].lastname,
                'student_id': students[0].student_id,
                'program_name': students[0].program.prog_name
            }

            context['student_data2'] = {
                'firstname': students[1].firstname,
                'middlename': students[1].middlename,
                'lastname': students[1].lastname,
                'student_id': students[1].student_id,
                'program_name': students[1].program.prog_name
            }
        else:
            context['student_data1'] = None
            context['student_data2'] = None

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
