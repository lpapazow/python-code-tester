from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from .exampletests import Testw1t1, Testw1t2, Testw1t3, Testw1t4, Testw2t3
import os

def run_tests(code_str, submission_id, code_day):
    #Create the file first
    f= open("codetester/htmlparser/tempcode.py","a")
    f.write(code_str)
    f.close()
    
    test_class_name = 'Test'+code_day
    example_tests = TestLoader().loadTestsFromTestCase(eval(test_class_name))
    suite = TestSuite([example_tests])
    runner = HTMLTestRunner(output='../codetester/templates/reports/'+str(submission_id), template='reporttemplate/template.html')
    result = runner.run(suite)

    f=open("codetester/htmlparser/tempcode.py","a")
    f.truncate(0)
    f.close()
    return result

def get_report_file_path(submission_id):
    html_files = [f for f in os.listdir('codetester/templates/reports/' + submission_id) if f.endswith('.html')]
    if len(html_files) != 1:
        raise ValueError('should be only one html file in the current directory')
    filename = html_files[0]
    report_dir = 'reports/' + submission_id + "/"
    return report_dir + filename

def calculate_success_rate(tests_result):
   all_tests = len(tests_result.successes) + len(tests_result.failures) + len(tests_result.errors)
   return int(100*len(tests_result.successes)/all_tests)