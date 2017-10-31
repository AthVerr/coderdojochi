from django.views.generic.list import ListView

from coderdojochi.models import (
    Guardian,
)


class AdminGuardianListView(ListView):

    model = Guardian

    template_name = 'admin_guardians_list.html'

    def get_queryset(self):

        return Guardian.objects.filter(
            is_active=True,
            # is_public=True,
        ).order_by('user__date_joined')


