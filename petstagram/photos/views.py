from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


class PhotoAddView(CreateView):
    model = Photo
    form_class = PhotoAddForm
    success_url = reverse_lazy('home')
    template_name = 'photos/photo-add-page.html'


class PhotoEditView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('photo-details', kwargs={'pk': self.kwargs['pk']})


class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'photos/photo-delete-page.html'
    success_url = reverse_lazy('home')


#def photo_delete(request, pk: int):
    #Photo.objects.get(pk=pk).delete()
    #return redirect('home')


class PhotoDetailsView(DetailView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['likes'] = self.object.like_set.all()
        context['comments'] = self.object.comment_set.all()
        context['comment_form'] = CommentForm()

        return context
