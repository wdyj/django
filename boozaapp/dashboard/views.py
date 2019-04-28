from django.shortcuts import render
from dashboard.models import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def calc_before_date(start, end) :
    """
    Args :
        start, end => datetime
    Returns :
        b_start, b_end => datetime
    """
    
    # interval 계산
    if start.month > end.month :
        period = (12+end.month) - start.month
    else :
        period = end.month - start.month
    
    #
    if period in (0,1) :
        period = 1
    
    # b_end가 start를 넘어설 경우 -> 한 달 더 빼기
    if start.month != end.month and start.day < end.day :
        period += 1
    
    b_start = start - relativedelta(months=period)
    b_end = end - relativedelta(months=period)
    
#    if b_end > start :
#        b_start = start - relativedelta(months=1)
#        b_end = end - relativedelta(months=1)
    
    return b_start, b_end