# _*_ coding:utf-8 _*_
"""the yate program for test"""
from string import Template
def start_response(resp="text/html"):
    ''' response the content to client'''
    return 'Context-type:' + resp + '\n\n'

def include_header(the_title):
    ''' use the_title replace the template title'''
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return header.substitute(title=the_title)
def include_footer(the_links):
    ''' replace the links in footer template with real link'''
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return footer.substitute(links=link_string)
def start_form(the_url, form_type="POST"):
    '''return a form begin with specified url and method'''
    return '<form action="' + the_url + '" method="' + form_type + '">'
def end_form(submit_msg="Submit"):
    ''' end a form with optional submit message'''
    return '<p></p><input type=submit value="' + submit_msg + '"></form>'
def radio_button(rb_name, rb_value):
    ''' a radio button with specified name and value'''
    return '<input type="radio" name="' + rb_name + '" value="' + rb_value +'">' + rb_value + '<br />'
def radio_button_id(rb_name, rb_value, rb_id):
    return '<input type="radio" name="' + rb_name + '" value="' + str(rb_id) +'">'  + rb_value + '<br />'
def u_list(items):
    ''' an unsorted list '''
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string +='</ul>'
    return u_string
def header(header_text,header_level=2):
    ''' header text '''
    return '<h' + str(header_level) + '>' + header_text + '</h' + str(header_level) +'>'
def para(para_text):
    ''' a paragraph'''
    return '<p>' + para_text + '</p>'
