from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import Witdrawal_Form, Deposit_Form
from first_app.summary import sum_dep, sum_wd
from first_app.forms import NewDepositForm, UserForm, UserProfileInfoForm
from django.views.generic import TemplateView, ListView
import operator
from django.db.models import Q
# LOGIN
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

wd_data_colector = []   # WITHDRAW DATA
dp_data_colector = []   # DEPOSIT DATA
wd_id = []              # SELECTED WD ID
@login_required
def summary_pg(request):

    my_context = {
    'Dep_comp_sum_td': sum_dep()['Dep_comp_sum_td'],
    'Dep_comp_pieces_td': sum_dep()['Dep_comp_pieces_td'],
    'Dep_inPro_sum_td': sum_dep()['Dep_inPro_sum_td'],
    'Dep_inPro_pieces_td': sum_dep()['Dep_inPro_pieces_td'],
    'Dep_pending_sum_td': sum_dep()['Dep_pending_sum_td'],
    'Dep_pending_pieces_td': sum_dep()['Dep_pending_pieces_td'],

    'Dep_comp_sum_month': sum_dep()['Dep_comp_sum_month'],
    'Dep_comp_pieces_month': sum_dep()['Dep_comp_pieces_month'],
    'Dep_inPro_sum_month': sum_dep()['Dep_inPro_sum_month'],
    'Dep_inPro_pieces_month': sum_dep()['Dep_inPro_pieces_month'],
    'Dep_pending_sum_month': sum_dep()['Dep_pending_sum_month'],
    'Dep_pending_pieces_month': sum_dep()['Dep_pending_pieces_month'],

    'Wd_comp_sum_td': sum_wd()['Wd_comp_sum_td'],
    'Wd_comp_pieces_td': sum_wd()['Wd_comp_pieces_td'],
    'Wd_inPro_sum_td': sum_wd()['Wd_inPro_sum_td'],
    'Wd_inPro_pieces_td': sum_wd()['Wd_inPro_pieces_td'],
    'Wd_pending_sum_td': sum_wd()['Wd_pending_sum_td'],
    'Wd_pending_pieces_td': sum_wd()['Wd_pending_pieces_td'],

    'Wd_comp_sum_month': sum_wd()['Wd_comp_sum_month'],
    'Wd_comp_pieces_month': sum_wd()['Wd_comp_pieces_month'],
    'Wd_inPro_sum_month': sum_wd()['Wd_inPro_sum_month'],
    'Wd_inPro_pieces_month': sum_wd()['Wd_inPro_pieces_month'],
    'Wd_pending_sum_month': sum_wd()['Wd_pending_sum_month'],
    'Wd_pending_pieces_month': sum_wd()['Wd_pending_pieces_month'],
    }

    return render(request, 'first_app/summary.html', context=my_context)

@login_required
def wd_list_pg(request):
    withdraw_list = Witdrawal_Form.objects.order_by('-id')

    # Count withdrawals
    counter = 0
    for wd in withdraw_list:
        counter += 1
    # FINISH - Count withdrawals

    my_context = {
        'Witdrawal_Form': withdraw_list,
        'Sum': counter,
    }

    return render(request, 'first_app/wd_list_pg.html', context=my_context)

@login_required
def dp_list_pg(request):
    deposit_list = Deposit_Form.objects.order_by('-id')

    # Count withdrawals
    counter = 0
    for dep in deposit_list:
        counter += 1
    # FINISH - Count withdrawals

    my_context = {
        'Deposit_Form': deposit_list,
        'Sum': counter,
    }

    return render(request, 'first_app/dp_list_pg.html', context=my_context)


# SEARCH IN WITHDRAW LIST
class SearchResultsView_wd(ListView):
    model = Witdrawal_Form
    template_name = 'first_app/wd_list_pg.html'

    def get_queryset(self):
        wd_data_colector.clear()
        counter = 0
        # SEARCH FOR INPUT
        query_name_wd = self.request.GET.get('q')
        object_list_input_wd = Witdrawal_Form.objects.filter(Q(name__icontains=query_name_wd)).order_by('-id')
        val_input_wd = object_list_input_wd.values()
        # SEARCH FOR INPUT - FINISH

        # SEARCH FOR BANK
        query_bank_wd = self.request.GET.get('q3')
        object_list_bank_wd = Witdrawal_Form.objects.filter(Q(bank_name__icontains=query_bank_wd)).order_by('-id')
        val_bank_wd = object_list_bank_wd.values()
        # SEARCH FOR BANK - FINISH

        # SEARCH FOR STATUS
        query_status_wd = self.request.GET.get('q4')
        object_list_status_wd = Witdrawal_Form.objects.filter(Q(status__icontains=query_status_wd)).order_by('-id')
        val_status_wd = object_list_status_wd.values()
        # SEARCH FOR STATUS - FINISH

        # SEARCH FOR DATE
        query_cr_date1_wd = self.request.GET.get('q1')
        query_cr_date2_wd = self.request.GET.get('q2')

        if query_cr_date1_wd and query_cr_date2_wd:
            object_list_cr_date_wd = Witdrawal_Form.objects.filter(created_date__range=[query_cr_date1_wd, query_cr_date2_wd])
            val_cr_date_wd = object_list_cr_date_wd.values()

            for obj in val_input_wd & val_bank_wd & val_status_wd & val_cr_date_wd:
                if not obj in wd_data_colector:
                    wd_data_colector.append(obj)
                    counter += 1
            wd_data_colector.append(counter)
            return wd_data_colector
        # SEARCH FOR DATE - FINISH

        for obj in val_input_wd & val_bank_wd & val_status_wd:
            if not obj in wd_data_colector:
                wd_data_colector.append(obj)
                counter += 1
        wd_data_colector.append(counter)
        return wd_data_colector


# SEARCH IN WITHDRAW LIST --- FINISH

# SEARCH IN DEPOSIT LIST
class SearchResultsView_dp(ListView):
    model = Deposit_Form
    template_name = 'first_app/dp_list_pg.html'
    def get_queryset(self):
        dp_data_colector.clear()
        counter = 0
        # SEARCH FOR INPUT
        query_name_dp = self.request.GET.get('s1')
        object_list_input_dp = Deposit_Form.objects.filter(Q(name__icontains=query_name_dp)).order_by('-id')
        if len(object_list_input_dp) == 0:
            object_list_input_dp = Deposit_Form.objects.filter(Q(username__icontains=query_name_dp)).order_by('-id')
        val_input_dp = object_list_input_dp.values()
        # SEARCH FOR INPUT - FINISH

        # SEARCH FOR BANK
        query_bank_dp = self.request.GET.get('s3')
        object_list_bank_dp = Deposit_Form.objects.filter(Q(bank_name__icontains=query_bank_dp)).order_by('-id')
        val_bank_dp = object_list_bank_dp.values()
        # SEARCH FOR BANK - FINISH

        # SEARCH FOR STATUS
        query_status_dp = self.request.GET.get('s4')
        object_list_status_dp = Deposit_Form.objects.filter(Q(status__icontains=query_status_dp)).order_by('-id')
        val_status_dp = object_list_status_dp.values()
        # SEARCH FOR STATUS - FINISH

        # SEARCH FOR DATE
        query_cr_date1_dp = self.request.GET.get('s2-1')
        query_cr_date2_dp = self.request.GET.get('s2-2')
        if query_cr_date1_dp and query_cr_date2_dp:
            object_list_cr_date_dp = Deposit_Form.objects.filter(created_date__range=[query_cr_date1_dp, query_cr_date2_dp])
            val_cr_date_dp = object_list_cr_date_dp.values()
            for obj in val_input_dp & val_bank_dp & val_status_dp & val_cr_date_dp:
                if not obj in dp_data_colector:
                    dp_data_colector.append(obj)
                    counter += 1
            dp_data_colector.append(counter)
            return dp_data_colector
        # SEARCH FOR DATE - FINISH

        for obj in val_input_dp & val_bank_dp & val_status_dp:
            if not obj in dp_data_colector:
                dp_data_colector.append(obj)
                counter += 1
        dp_data_colector.append(counter)
        return dp_data_colector
# SEARCH IN DEPOSIT LIST --- FINISH

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            reqistered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html',
                            {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered
                            })

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('summary_pg'))
            else:
                return HttpResponse("Account not Active!")
        else:
            # IF USERNAME OR PASSWORD INCORECT
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'first_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def dp_form(request):

    form = NewDepositForm()

    if request.method == "POST":
        # Deposit_Form.bank_name = request.POST.get('bank_name')
        form = NewDepositForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            ###### GET DEPOSIT DATA ######
            dp_data_colector = Deposit_Form.objects.values()
            # for data in dp_data_colector:
            #     print(data.get('bank_name'))
            ###### GET DEPOSIT DATA - FINISH ######
            return HttpResponseRedirect(reverse('selectValue'))
    return render(request, 'first_app/dp_form.html',{})

def sl_value(request):
    withdraw_list = Witdrawal_Form.objects.order_by('-id')
    deposit_list = Deposit_Form.objects.order_by('-id')[0]

    my_context = {
        'Witdrawal_Form': withdraw_list,
        'Deposit_Form': deposit_list,
    }


    if request.method == "POST":
        obj = Deposit_Form.objects.latest('id')
        selected_wd_id = request.POST.get('btn_cek')
        wd_filtered = Witdrawal_Form.objects.filter(id=selected_wd_id)

        for obj_wd in wd_filtered:
            obj.amount = obj_wd.amount
            obj.save()
            obj_wd.status = 'In Progress'
            obj_wd.save()
            wd_id.clear()
            wd_id.append(obj_wd.id)

        return HttpResponseRedirect(reverse('sendMoney'))
    return render(request, 'first_app/value.html', context=my_context)

def send_money(request):
    withdraw_list = Witdrawal_Form.objects.order_by('-id')
    deposit_list = Deposit_Form.objects.order_by('-id')[0]

    for selected_wd in withdraw_list:
        if wd_id[0] == selected_wd.id:
            withdraw_list = selected_wd
    my_context = {
        'Witdrawal_Form': withdraw_list,
        'Deposit_Form': deposit_list,
    }
    if request.method == "POST":
        obj = Deposit_Form.objects.latest('id')
        wd_filtered = Witdrawal_Form.objects.filter(id=wd_id[0])

        for obj_wd in wd_filtered:
            obj.amount = obj_wd.amount
            obj.status = 'Completed'
            obj.save()
            obj_wd.status = 'Completed'
            obj_wd.save()
            wd_id.clear()
            wd_id.append(obj_wd.id)
        return render(request, 'first_app/done.html')
    return render(request, 'first_app/get_bank_info.html', context=my_context)
