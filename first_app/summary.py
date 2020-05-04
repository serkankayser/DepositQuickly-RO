from first_app.models import Witdrawal_Form, Deposit_Form

### SUMMARY DEPOSIT ###

def sum_dep():
    deposit_list = Deposit_Form.objects.values()
    dep_comp_sum = 0
    dep_comp_pieces = 0
    dep_inPro_sum = 0
    dep_inPro_pieces = 0
    dep_pending_sum = 0
    dep_pending_pieces = 0

    for summary in deposit_list:
        if summary['status'] == 'Completed':
            dep_comp_sum += summary['amount']
            dep_comp_pieces += 1

        if summary['status'] == 'In Progress':
            dep_inPro_sum += summary['amount']
            dep_inPro_pieces += 1

        if summary['status'] == 'Pending':
            dep_pending_sum += summary['amount']
            dep_pending_pieces += 1

    my_context_dep = {
        'Dep_comp_sum': dep_comp_sum,
        'Dep_comp_pieces': dep_comp_pieces,
        'Dep_inPro_sum': dep_inPro_sum,
        'Dep_inPro_pieces': dep_inPro_pieces,
        'Dep_pending_sum': dep_pending_sum,
        'Dep_pending_pieces': dep_pending_pieces
    }
    return my_context_dep
### FINISH - SUMMARY DEPOSIT ###

### SUMMARY WITHDRAW ###
def sum_wd():
    withdraw_list = Witdrawal_Form.objects.values()
    wd_comp_sum = 0
    wd_comp_pieces = 0
    wd_inPro_sum = 0
    wd_inPro_pieces = 0
    wd_pending_sum = 0
    wd_pending_pieces = 0

    for summary_wd in withdraw_list:
        if summary_wd['status'] == 'Completed':
            wd_comp_sum += summary_wd['amount']
            wd_comp_pieces += 1

        if summary_wd['status'] == 'In Progress':
            wd_inPro_sum += summary_wd['amount']
            wd_inPro_pieces += 1

        if summary_wd['status'] == 'Pending':
            wd_pending_sum += summary_wd['amount']
            wd_pending_pieces += 1

    my_context_wd = {
        'Wd_comp_sum': wd_comp_sum,
        'Wd_comp_pieces': wd_comp_pieces,
        'Wd_inPro_sum': wd_inPro_sum,
        'Wd_inPro_pieces': wd_inPro_pieces,
        'Wd_pending_sum': wd_pending_sum,
        'Wd_pending_pieces': wd_pending_pieces,
    }
    return my_context_wd
### FINISH - SUMMARY WITHDRAW ###
