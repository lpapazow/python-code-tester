from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Submission
from django.utils import timezone
from .htmlparser import tester
import sys

def index(request):
    if Submission.objects.order_by('-id')[:1].first():
        next_submission_id = Submission.objects.order_by('-id')[:1].first().id + 1
        print(next_submission_id)
        latest_submission_list = Submission.objects.order_by('-pub_date')[:5]
        context = {
            'next_submission_id': next_submission_id,
            'latest_submission_list': latest_submission_list,
        }
        return render(request, 'codetester/index.html', context)
    else:
        return render(request, 'codetester/index.html', {})

def results(request, submission_id):
    context={}
    if request.method == 'POST':
        code_text=request.POST.get('code_text')
        code_day=request.POST.get('code_day')
        tests_result=tester.run_tests(code_text, submission_id, code_day)
        success_rate = tester.calculate_success_rate(tests_result)
        submission_instance = Submission.objects.create(submission_code=code_text, pub_date=timezone.now(), score=success_rate)
    else:
        submission_instance = Submission.objects.get(pk=submission_id)
        code_text = submission_instance.submission_code
    context = {
        'code_text': code_text
    }
    
    report_file_path = tester.get_report_file_path(submission_id)
    return render(request, report_file_path, context)

