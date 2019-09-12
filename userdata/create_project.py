import os
import shutil

from add_db_fonts import add_db_fonts, red, blue, green

example_content = 'ExampleContent'

blue('Create a new project')
red('Be sure to stash your changes before executing this script, otherwise the creation of a new project won`t work')

project_name = input(f'Project Name? E.g. T1000\n')

shutil.copytree(os.path.join(example_content), project_name)

with open(os.path.join(project_name, 'usersetup.tex'), 'r') as file_user_setup:
    user_setup = file_user_setup.read()

language = int(input('Choose Language: English with German Parts (0) Fully German (1)\n'))
user_setup = user_setup.replace(
    [
        r'''    %\setdefaultlanguage{english}
%\setotherlanguage[variant=german, spelling=new, latesthyphen=false]{german}''',
        r'''    %\setdefaultlanguage[variant=german, spelling=new, latesthyphen=false]{german}'''
    ][language],
    [
        r'''    \setdefaultlanguage{english}
\setotherlanguage[variant=german, spelling=new, latesthyphen=false]{german}''',
        r'''    \setdefaultlanguage[variant=german, spelling=new, latesthyphen=false]{german}'''
    ][language]
)

student_name = input('Student name\n')
matr_num = input('Enrolment Number (Matr.-Num.)\n')
course = input('Course (e.g. MA-TINF123 AI123)\n')
company = input('Company (e.g. DB Systel GmbH)\n')
company_location = input('Company Location (e.g. Frankfurt am Main)\n')
title = input('Report title\n')
time_range = input('Time range in weeks\n')
handoverdate = input('Hand over date (date)\n')
city = input('City\n')

document_type = ['Internship', 'Study', 'Bachelor'][
    int(input('Document Type: Internship (0), Study (1), Bachelor (2)\n'))]

if document_type == 'Internship':
    for field_name, old, new in zip(
            [
                'Report Module (e.g. T1_1000)',
                'Report start (date)',
                'Report end (date)',
                'Department',
                'Department (long)',
                'Company Manager',
            ], [
                r"\newcommand{\reportmodule}{T...000}",
                r"\newcommand{\reportstart}{01.01.1970}",
                r"\newcommand{\reportend}{01.01.1970}",
                r"\newcommand{\department}{F.I...}",
                r"\newcommand{\longdepartment}{...}",
                r"\newcommand{\companymanager}{...}",
            ], [
                "\\newcommand{\\reportmodule}{T..",
                "\\newcommand{\\reportstart}{01.01",
                "\\newcommand{\\reportend}{01.01",
                "\\newcommand{\\department}{F.I",
                "\\newcommand{\\longdepartment}{",
                "\\newcommand{\\companymanager}{",
            ]):
        input_field_value = input(field_name + '\n')
        user_setup = user_setup.replace(old, new + input_field_value + '}')

elif document_type == 'Internship':
    for field_name, old, new in zip(
            [
                'Report semester',
                'Professor',
            ], [
                r"\newcommand{\reportsemester}{...th}",
                r"\newcommand{\prof}{Prof.Dr....}",
            ], [

                r"\newcommand{\reportsemester}{",
                r"\newcommand{\prof}{",
            ]):
        input_field_value = input(field_name + '\n')
        user_setup = user_setup.replace(old, new + input_field_value + '}')

elif document_type == 'Internship':
    for field_name, old, new in zip(
            [
                'Academic degreee',
                'Company Manager',
                'Professor',
            ], [
                r"\newcommand{\academicdegree}{Bachelor of Science}",
                r"\newcommand{\companymanager}{M. Sc. ...}",
                r"\newcommand{\prof}{Prof. Dr. ...}",
            ], [

                r"\newcommand{\academicdegree}{"
                r"\newcommand{\companymanager}{"
                r"\newcommand{\prof}{"
            ]):
        input_field_value = input(field_name + '\n')
        user_setup = user_setup.replace(old, new + input_field_value + '}')

report_kind = input('Kind of report (e.g. T1000)\n')

for old, new in zip(
        [
            r"\newcommand{\studentname}{Max Mustermann}",
            r"\newcommand{\matrikelno}{123456}",
            r"\newcommand{\kurs}{MA-TINF...}",
            r"\newcommand{\companyname}{DB Systel GmbH}",
            r"\newcommand{\companylocation}{Frankfurt am Main}",
            r"\newcommand{\reporttitle}{Wie erstelle ich einen sch{\"o}nen Praxisbericht}",
            r"\newcommand{\timerange}{... Wochen}",
            r"\newcommand{\handoverdate}{01.01.1970}",
            r"\newcommand{\city}{...}",
        ], [
            f"\\newcommand{{\\studentname}}{{{student_name}}}",
            f"\\newcommand{{\\matrikelno}}{{{matr_num}}}",
            f"\\newcommand{{\\kurs}}{{{course}}}",
            f"\\newcommand{{\\companyname}}{{{company}}}",
            f"\\newcommand{{\\companylocation}}{{{company_location}}}",
            f"\\newcommand{{\\reporttitle}}{{{title}}}",
            f"\\newcommand{{\\timerange}}{{{time_range} Wochen}}",
            f"\\newcommand{{\\handoverdate}}{{{handoverdate}}}",
            f"\\newcommand{{\\city}}{{{city}}}",
        ]
):
    user_setup = user_setup.replace(old, new)


# change project name in setup file
with open('setup.tex', 'r') as setup_file:
    setup_contents = setup_file.read()

with open('setup.tex', 'w') as setup_file:
    setup_file.write(setup_contents.replace(example_content, project_name))

if input('Would you like to add DB fonts? ("y" if yes)\n') == 'y':
    add_db_fonts()
    user_setup = user_setup.replace('%DbFont', 'DbFont')

with open(os.path.join(project_name, 'usersetup.tex'), 'w') as file_user_setup:
    file_user_setup.write(user_setup)

green("Finished! You can now compile the main.tex file in the root of the repository or "
      "make some additional changes to your setup by editing usersetup.tex")
