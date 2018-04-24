from django.urls import path

from hijos.treasure import views

app_name = 'treasure'
urlpatterns = [
    path(
        'lodges/<int:pk>/lodgeaccounts/',
        view=views.LodgeAccountsByLodgeList.as_view(),
        name='lodgeaccount-list'
    ),
    path(
        'lodgeaccounts/add/',
        view=views.LodgeAccountCreateView.as_view(),
        name='lodgeaccount-create'
    ),
    path(
        'lodgeaccounts/<int:pk>/',
        view=views.LodgeAccountDetailView.as_view(),
        name='lodgeaccount-detail'
    ),
    path(
        'lodges/<int:pk>/periods/',
        view=views.PeriodsByLodgeList.as_view(),
        name='period-list'
    ),
    path(
        'periods/add/',
        view=views.PeriodCreateView.as_view(),
        name='period-create'
    ),
    path(
        'periods/<int:pk>/',
        view=views.PeriodDetailView.as_view(),
        name='period-detail'
    ),
    path(
        'lodges/<int:pk>/invoices/',
        view=views.InvoicesByLodgeList.as_view(),
        name='invoice-list'
    ),
    path(
        'invoices/add/',
        view=views.InvoiceCreateView.as_view(),
        name='invoice-create'
    ),
    path(
        'invoices/<int:pk>/',
        view=views.InvoiceDetailView.as_view(),
        name='invoice-detail'
    ),
    path(
        'lodges/<int:pk>/deposits/',
        view=views.DepositsByLodgeList.as_view(),
        name='deposit-list'
    ),
    path(
        'deposits/add/',
        view=views.DepositCreateView.as_view(),
        name='deposit-create'
    ),
    path(
        'deposits/<int:pk>/',
        view=views.DepositDetailView.as_view(),
        name='deposit-detail'
    ),
    path(
        'lodges/<int:pk>/charges/',
        view=views.ChargesByLodgeList.as_view(),
        name='charge-list'
    ),
    path(
        'charges/add/',
        view=views.ChargeCreateView.as_view(),
        name='charge-create'
    ),
    path(
        'charges/<int:pk>/',
        view=views.ChargeDetailView.as_view(),
        name='charge-detail'
    ),
    path(
        'lodges/<int:pk>/grandlodgedeposits/',
        view=views.GrandLodgeDepositsByLodgeList.as_view(),
        name='grandlodgedeposit-list'
    ),
    path(
        'grandlodgedeposits/add/',
        view=views.GrandLodgeDepositCreateView.as_view(),
        name='grandlodgedeposit-create'
    ),
    path(
        'grandlodgedeposits/<int:pk>/',
        view=views.GrandLodgeDepositDetailView.as_view(),
        name='grandlodgedeposit-detail'
    ),
    path(
        'lodges/<int:pk>/ingresses/',
        view=views.LodgeAccountIngressesByLodgeList.as_view(),
        name='lodgeaccountingress-list'
    ),
    path(
        'ingresses/add/',
        view=views.LodgeAccountIngressCreateView.as_view(),
        name='lodgeaccountingress-create'
    ),
    path(
        'ingresses/<int:pk>/',
        view=views.LodgeAccountIngressDetailView.as_view(),
        name='lodgeaccountingress-detail'
    ),
    path(
        'lodges/<int:pk>/egresses/',
        view=views.LodgeAccountEgressesByLodgeList.as_view(),
        name='lodgeaccountegress-list'
    ),
    path(
        'egresses/add/',
        view=views.LodgeAccountEgressCreateView.as_view(),
        name='lodgeaccountegress-create'
    ),
    path(
        'egresses/<int:pk>/',
        view=views.LodgeAccountEgressDetailView.as_view(),
        name='lodgeaccountegress-detail'
    ),
    path(
        'lodges/<int:pk>/transfers/',
        view=views.LodgeAccountTransfersByLodgeList.as_view(),
        name='lodgeaccounttransfer-list'
    ),
    path(
        'transfers/add/',
        view=views.LodgeAccountTransferCreateView.as_view(),
        name='lodgeaccounttransfer-create'
    ),
    path(
        'transfers/<int:pk>/',
        view=views.LodgeAccountTransferDetailView.as_view(),
        name='lodgeaccounttransfer-detail'
    )
]
