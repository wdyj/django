from django.shortcuts import render
from dashboard.models import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.db.models import Sum

def read_event_list() :
    """
    이벤트리스트 읽어오는 함수
    Args :
        event_list : 이벤트 객체
    Returns :
        event_list
    """
    event_list = EventList.objects.all()
    return event_list

def calc_before_date(start, end) :
    """
    동기간 계산 함수
    Args :
        start, end : 시작일, 종료일 (Type : datetime)
        b_start, b_end : 동기간 시작일, 종료일 (Type : datetime)
    Returns :
        b_start, b_end
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

def calc_sales_data(start,end,b_start,b_end,channel) :
    """
    매출 데이터 계산 함수
    Args :
        data, b_data : 매출 데이터 객체
        total, b_total : 총 매출액
        rate_total : 동기간 대비 매출액 변화율
        num, b_num : 총 매출건수
        rate_num : 동기간 대비 매출건수 변화율
    Returns :
        data, rate_total, rate_num
    """
    # 매출 데이터 가져오기
    if channel == '거장들의투자공식' :
        data = SalesInfoV2.objects.filter(start_time__range=[start, end])
        b_data = SalesInfoV2.objects.filter(start_time__range=[b_start, b_end])
    
        # 총 매출액 계산
        total = data.aggregate(Sum('total'))['total__sum']
        b_total = b_data.aggregate(Sum('total'))['total__sum']
        rate_total = round((total/b_total - 1) * 100,2)

        # 총 결제건수 계산 
        num = len(data)
        b_num = len(b_data)
        rate_num = round((num/b_num - 1) * 100,2)
    
    elif channel == '핫스탁코리아' :
        data = HskCashPurchase.objects.filter(created_time__range=[start, end])
        b_data = HskCashPurchase.objects.filter(created_time__range=[b_start, b_end])
        
        # 총 매출액 계산
        total = data.aggregate(Sum('price_total'))['price_total__sum']
        b_total = b_data.aggregate(Sum('price_total'))['price_total__sum']
        rate_total = round((total/b_total - 1) * 100,2)

        # 총 결제건수 계산 
        num = len(data)
        b_num = len(b_data)
        rate_num = round((num/b_num - 1) * 100,2)

    return data, rate_total, rate_num