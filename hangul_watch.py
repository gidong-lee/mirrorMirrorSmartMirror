# -*- coding: utf-8 -*-
'''
Created on 2016. 9. 3.

@author: jee1lee
'''

import time

_hangul_small_unit_numbers_ = ['', '십', '백', '천']
_hangul_big_unit_numbers_ = ['', '만', '억', '조', '경', '해']
_hangul_numbers_ = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']

def convert_number_to_hangul(num):
    str_num = str(num)
    digit = len(str_num) # 자리수 
        
    # 4단위로 숫자를 자를 회수.
    slice_cnt = digit // 4
    slice_tail = digit % 4
    if (slice_tail != 0): slice_cnt += 1
    slice_nums = []
    endnum = 0
    strlen = 0
    for i in range(slice_cnt) :
        if (i == 0) : 
            startnum = 0
            endnum = 4 - (4 - slice_tail)
            if (endnum == 0): endnum = 4
        if (i != 0) : 
            startnum = endnum
            endnum = startnum + 4
        strlen = len(str_num[startnum : endnum])
        slice_nums.append(str_num[startnum : endnum])

    # 자리수 별로 한글화
    res_nums = '' 
    big_unit_cnt = len(slice_nums)
    for i in range(big_unit_cnt) :
        s_num = slice_nums[i]
         
        small_unit_cnt = len(slice_nums[i])
        for j in range(small_unit_cnt) :
            res_nums += _hangul_numbers_[int(s_num[j])]
            if (int(s_num[j]) != 0) :
                res_nums += _hangul_small_unit_numbers_[small_unit_cnt - j - 1] 
    
        if (int(s_num) != 0) :
            res_nums += _hangul_big_unit_numbers_[big_unit_cnt - i - 1]
    
    res_nums = res_nums.replace('일십', '십').replace('일백', '백').replace('일천', '천')
#     
    return res_nums