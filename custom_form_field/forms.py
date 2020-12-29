import logging

from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import ExtraInfo


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['student_group'].required = True

    class Meta(object):
        model = ExtraInfo
        fields = ('student_group',)
        labels = {'student_group': _("Student group"),}
        help_text = {'student_group': _("Please enter your group"),}
