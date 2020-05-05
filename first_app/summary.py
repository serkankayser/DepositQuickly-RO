from first_app.models import Witdrawal_Form, Deposit_Form
from datetime import date

### SUMMARY DEPOSIT - DAILY ###
'''
In depunere se face cautare dupa crearii.
'''
def sum_dep():
    deposit_list = Deposit_Form.objects.values()
    today = date.today().strftime("%d-%m-%Y")
    month = date.today().strftime("%m")
    dep_comp_sum_td = 0
    dep_comp_pieces_td = 0
    dep_inPro_sum_td = 0
    dep_inPro_pieces_td = 0
    dep_pending_sum_td = 0
    dep_pending_pieces_td = 0

    dep_comp_sum_month = 0
    dep_comp_pieces_month = 0
    dep_inPro_sum_month = 0
    dep_inPro_pieces_month = 0
    dep_pending_sum_month = 0
    dep_pending_pieces_month = 0

    ### DAILY ###
    for summary_dp_td in deposit_list:
        td = summary_dp_td['created_date'].strftime("%d-%m-%Y")
        if summary_dp_td['status'] == 'Completed' and td == today:
            dep_comp_sum_td += summary_dp_td['amount']
            dep_comp_pieces_td += 1

        if summary_dp_td['status'] == 'In Progress' and td == today:
            dep_inPro_sum_td += summary_dp_td['amount']
            dep_inPro_pieces_td += 1

        if summary_dp_td['status'] == 'Pending' and td == today:
            dep_pending_sum_td += summary_dp_td['amount']
            dep_pending_pieces_td += 1
    ### DAILY - FINISH ###

    ### MONTHLY ###
    for summary_dp_month in deposit_list:
        mt = summary_dp_month['created_date'].strftime("%m")
        if summary_dp_month['status'] == 'Completed' and mt == month:
            dep_comp_sum_month += summary_dp_month['amount']
            dep_comp_pieces_month += 1

        if summary_dp_month['status'] == 'In Progress' and mt == month:
            dep_inPro_sum_month += summary_dp_month['amount']
            dep_inPro_pieces_month += 1

        if summary_dp_month['status'] == 'Pending' and mt == month:
            dep_pending_sum_month += summary_dp_month['amount']
            dep_pending_pieces_month += 1
    ### MONTHLY - FINISH ###

    my_context_dep = {
        'Dep_comp_sum_td': dep_comp_sum_td,
        'Dep_comp_pieces_td': dep_comp_pieces_td,
        'Dep_inPro_sum_td': dep_inPro_sum_td,
        'Dep_inPro_pieces_td': dep_inPro_pieces_td,
        'Dep_pending_sum_td': dep_pending_sum_td,
        'Dep_pending_pieces_td': dep_pending_pieces_td,

        'Dep_comp_sum_month': dep_comp_sum_month,
        'Dep_comp_pieces_month': dep_comp_pieces_month,
        'Dep_inPro_sum_month': dep_inPro_sum_month,
        'Dep_inPro_pieces_month': dep_inPro_pieces_month,
        'Dep_pending_sum_month': dep_pending_sum_month,
        'Dep_pending_pieces_month': dep_pending_pieces_month
    }
    return my_context_dep
### SUMMARY DEPOSIT - FINISH###

### SUMMARY WITHDRAW ###
'''
In retragere se face cautare dupa data modificarii.
'''
def sum_wd():
    withdraw_list = Witdrawal_Form.objects.values()
    today = date.today().strftime("%d-%m-%Y")
    month = date.today().strftime("%m")
    wd_comp_sum_td = 0
    wd_comp_pieces_td = 0
    wd_inPro_sum_td = 0
    wd_inPro_pieces_td = 0
    wd_pending_sum_td = 0
    wd_pending_pieces_td = 0

    wd_comp_sum_month = 0
    wd_comp_pieces_month = 0
    wd_inPro_sum_month = 0
    wd_inPro_pieces_month = 0
    wd_pending_sum_month = 0
    wd_pending_pieces_month = 0
    ### DAILY ###

    for summary_wd in withdraw_list:
        td = summary_wd['modified_date'].strftime("%d-%m-%Y")
        if summary_wd['status'] == 'Completed' and td == today:
            wd_comp_sum_td += summary_wd['amount']
            wd_comp_pieces_td += 1

        if summary_wd['status'] == 'In Progress' and td == today:
            wd_inPro_sum_td += summary_wd['amount']
            wd_inPro_pieces_td += 1

        if summary_wd['status'] == 'Pending' and td == today:
            wd_pending_sum_td += summary_wd['amount']
            wd_pending_pieces_td += 1

    ### DAILY - FINISH ###

    ### MONTHLY ###

    for summary_wd_month in withdraw_list:
        mt = summary_wd_month['modified_date'].strftime("%m")
        if summary_wd_month['status'] == 'Completed' and mt == month:
            wd_comp_sum_month += summary_wd_month['amount']
            wd_comp_pieces_month += 1

        if summary_wd_month['status'] == 'In Progress' and mt == month:
            wd_inPro_sum_month += summary_wd_month['amount']
            wd_inPro_pieces_month += 1

        if summary_wd_month['status'] == 'Pending' and mt == month:
            wd_pending_sum_month += summary_wd_month['amount']
            wd_pending_pieces_month += 1

    ### MONTHLY - FINISH ###

    my_context_wd = {
        'Wd_comp_sum_td': wd_comp_sum_td,
        'Wd_comp_pieces_td': wd_comp_pieces_td,
        'Wd_inPro_sum_td': wd_inPro_sum_td,
        'Wd_inPro_pieces_td': wd_inPro_pieces_td,
        'Wd_pending_sum_td': wd_pending_sum_td,
        'Wd_pending_pieces_td': wd_pending_pieces_td,

        'Wd_comp_sum_month': wd_comp_sum_month,
        'Wd_comp_pieces_month': wd_comp_pieces_month,
        'Wd_inPro_sum_month': wd_inPro_sum_month,
        'Wd_inPro_pieces_month': wd_inPro_pieces_month,
        'Wd_pending_sum_month': wd_pending_sum_month,
        'Wd_pending_pieces_month': wd_pending_pieces_month,
    }
    return my_context_wd
### SUMMARY WITHDRAW - FINISH ###
