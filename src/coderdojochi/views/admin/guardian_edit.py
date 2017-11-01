from coderdojochi.forms import CDCModelForm, GuardianEditForm
from coderdojochi.models import Guardian, CDCUser
from django.views.generic import UpdateView


class AdminGuardianEditView(UpdateView):

    model = Guardian
    # fields = ['user__first_name', 'last_name', 'email', 'phone', 'zip']
    fields = ['phone', 'zip']
    template_name = 'edit.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
            # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        elif slug is not None:
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        else:
            raise AttributeError("Generic detail view %s must be called with "
                                 "either an object pk or a slug."
                                 % self.__class__.__name__)
        obj = Guardian.objects.get(id=self.kwargs['pk'])

        return obj
