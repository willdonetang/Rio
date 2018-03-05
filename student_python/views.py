from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from django.views import generic

from student_python.models import Contacts


def index(request):
    return render(template_name='student_python/index.html')


class IndexView(generic.ListView):
    template_name = "student_python/index.html"
    context_object_name = "latest_contacts_list"

    def get_queryset(self):
        return Contacts.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
