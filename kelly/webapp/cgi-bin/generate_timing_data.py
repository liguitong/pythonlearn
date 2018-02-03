#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import cgi
import athletemodel
import pickle
import yate

athletes = athletemodel.get_from_store()
form_data = cgi.FieldStorage()

athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach kelly's Timing Data"))
print('Athlete:' + athlete_name + ',DOB: ' + athletes[athlete_name].dob + '.')
print(yate.para('The top times for this athlete are:'))
print(yate.u_list(athletes[athlete_name].top(3)))
print(yate.include_footer({'Home':'/index.html','Select another athlete:':'generate_list.py'}))
