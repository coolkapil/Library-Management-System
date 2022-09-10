from django.core.exceptions import PermissionDenied


class StaffRequiredMixin(object):
    """
        Staff - list of strings, required param
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        else:
            if not request.user.is_staff:
                raise PermissionDenied
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)