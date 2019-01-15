from django.shortcuts import render
from clientApp.forms import ClientExpenseForm
from clientApp.models import ClientExpense
from django.contrib.auth.decorators import login_required



@login_required(login_url='signin')
def dashBoard(request):

    message = ''
    form = ClientExpenseForm()
    if request.method == 'POST':

        form = ClientExpenseForm(request.POST)

        if form.is_valid():

            clientExpense = ClientExpense()
            clientExpense.client = request.user
            clientExpense.title = form.cleaned_data['title']
            clientExpense.amount = form.cleaned_data['amount']
            clientExpense.currency = form.cleaned_data['currency']
            clientExpense.description = form.cleaned_data['description']
            clientExpense.save()
            form = ClientExpenseForm()
            message = "created successfully.."

    return render(request, 'dashBoard.html', {'form':form , 'msg':message})
@login_required(login_url='signin')
def read(request):

    data = ClientExpense.objects.filter(client_id=request.user.id)
    return render(request, 'expenseList.html', {'data':data})

@login_required(login_url='signin')
def viewAll(request):
    data = ClientExpense.objects.all()
    return render(request , 'viewAll.html' , {'data':data})


def viewRow(request):
    resultSet = ClientExpense.objects.get(id=request.GET['id'])
    return render(request, 'viewRow.html' , {'data':resultSet})



