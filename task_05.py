#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Checking the blood pressure."""

INPUTMSG = raw_input('What is your blood pressure? ')
INPUTMSG = int(INPUTMSG)

if INPUTMSG <= 89:
    MYSTATUS = 'Low.'
elif INPUTMSG >= 90 and INPUTMSG <= 119:
    MYSTATUS = 'Ideal.'
elif INPUTMSG >= 120 and INPUTMSG <= 139:
    MYSTATUS = 'Warning!'
elif INPUTMSG >= 140 and INPUTMSG <= 159:
    MYSTATUS = 'High.'
else:
    MYSTATUS = 'Emergency!'

MYRESULT = 'Your status is currently: {}'.format(MYSTATUS)
print MYRESULT
