from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from employees.forms import CreateEmployee
from .models import HireCard
from .forms import CandidateUpdateForm

def candidates_list(request):
    candidates = HireCard.objects.all()
    context = {
        'title': 'Кандидаты',
        'candidates_list': candidates,
        'candidates_amount': candidates.count(),
    }
    return render(request, 'candidates/candidates-list.html', context=context)

def candidate_info(request, candidate_id):
    candidate = get_object_or_404(HireCard,pk=candidate_id)
    context = {
        'title': 'Информация о кандидате',
        'candidate': candidate,
    }
    return render(request, 'candidates/candidate-info.html', context=context)

def delete_candidate(request, candidate_id):
    candidate = get_object_or_404(HireCard, pk=candidate_id)
    if candidate.status in [
        candidate.HireStatus.OFFER,
        candidate.HireStatus.DECLINED
    ]:
        candidate.delete()
        messages.success(request, 'Кандидат успешно удалён.')
        return redirect('candidates:candidates')
    messages.error(request, 'Этого кандидата пока нельзя удалить.')
    return redirect('candidates:candidate-info', candidate_id=candidate.pk)

def edit_candidate(request, candidate_id):
    candidate = get_object_or_404(HireCard, pk=candidate_id)
    if request.method == 'POST':
        old_status = candidate.status
        form = CandidateUpdateForm(request.POST, request.FILES or None, instance=candidate)
        if form.is_valid():
            updated_candidate = form.save()
            if (old_status != HireCard.HireStatus.DECLINED
                and candidate.status == HireCard.HireStatus.DECLINED):
                updated_candidate.delete()
                messages.success(request, 'Кандидат успешно удалён.')
                return redirect('candidates:candidates')
            elif (old_status != HireCard.HireStatus.OFFER
                and candidate.status == HireCard.HireStatus.OFFER):
                return redirect('candidates:transfer-candidate', candidate_id=candidate.pk)
            messages.success(request,'Данные о кандидате успешно обновлены.')
            return redirect('candidates:candidate-info.html', candidate_id=candidate.pk)
    else:
        form = CandidateUpdateForm(instance=candidate)
    context = {
        'form': form,
        'candidate': candidate,
    }
    return render(request,'candidates:candidate-info', context=context)

def candidate_to_employee(request, candidate_id):
    candidate = get_object_or_404(HireCard, pk=candidate_id)
    if candidate.status != HireCard.HireStatus.OFFER:
        messages.error(request, 'Кандидат должен получить оффер, чтобы перейти в штаб сотрудников.')
        return redirect("candidates:candidate-info", candidate_id=candidate.pk)

    if request.method == 'POST':
        form = CreateEmployee(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)

            employee.name = candidate.name
            employee.surname = candidate.surname
            employee.middle_name = candidate.middle_name
            employee.birthdate = candidate.birthdate

            employee.save()
            candidate.delete()
            messages.success(request,"Новый сотрудник успешно создан.")
            return redirect("employees:employee-info", employee_id = employee.pk)
    else:
        form = CreateEmployee()
    context = {
        'title': 'Информация о новом сотруднике',
        'form': form,
        'candidate': candidate,
    }
    return render(request, 'candidates/candidate-info.html', context=context)
