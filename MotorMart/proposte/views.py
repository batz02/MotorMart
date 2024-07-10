from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Proposta
from annunci.models import Annuncio
from .forms import CreaProposta


@login_required
def listing_detail(request, pk):
    annuncio = get_object_or_404(Annuncio, pk=pk)
    if request.method == 'POST':
        if 'submit_proposal' in request.POST:
            form = CreaProposta(request.POST, annuncio=annuncio)
            if form.is_valid():
                proposal = form.save(commit=False)

                if proposal.prezzo < annuncio.prezzo:
                    proposal.annuncio = annuncio
                    proposal.utente = request.user
                    proposal.save()
                    messages.success(request, "Proposta inviata")
                    return redirect('annunci:details', pk=pk)
                else:
                    messages.success(request, "Importo non valido")
                    return redirect('proposte:proposals', pk=pk)
            else:
                messages.error(request, "Errore nell'inserimento della proposta")
        return redirect('annunci:details', pk=pk)
    
    proposals = Proposta.objects.filter(annuncio=annuncio)
    form = CreaProposta(annuncio=annuncio)
    return render(request, 'proposte/proposta.html', {'listing': annuncio, 'form': form, 'proposals': proposals})

@login_required
def accept_proposal(request, proposal_id):
    proposal = get_object_or_404(Proposta, pk=proposal_id, annuncio__utente=request.user)
    proposal.accettata = True
    annuncio = get_object_or_404(Annuncio, pk=proposal.annuncio_id)
    annuncio.venduto = True
    annuncio.prezzo_acquisto = proposal.prezzo
    annuncio.compratore = proposal.utente.id
    annuncio.save()
    proposal.save()
    messages.success(request, "Proposta accettata")
    return redirect('annunci:details', pk=proposal.annuncio.pk)


@login_required
def reject_proposal(request, proposal_id):
    proposal = get_object_or_404(Proposta, pk=proposal_id, annuncio__utente=request.user)
    proposal.accettata = False
    proposal.save()
    messages.success(request, "Proposta rifiutata")
    return redirect('annunci:details', pk=proposal.annuncio.pk)
