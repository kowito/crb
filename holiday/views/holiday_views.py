from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from holiday.models import Holiday


class HolidayView(object):
    model = Holiday

    def get_template_names(self):
        """Nest templates within holiday directory."""
        tpl = super(HolidayView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'holiday'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class HolidayDateView(HolidayView):
    date_field = 'start_date'
    month_format = '%m'


class HolidayBaseListView(HolidayView):
    paginate_by = 10


class HolidayArchiveIndexView(
    HolidayDateView, HolidayBaseListView, ArchiveIndexView):
    pass


class HolidayCreateView(HolidayView, CreateView):
    pass


class HolidayDateDetailView(HolidayDateView, DateDetailView):
    pass


class HolidayDayArchiveView(
    HolidayDateView, HolidayBaseListView, DayArchiveView):
    pass


class HolidayDeleteView(HolidayView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('holiday_holiday_list')


class HolidayDetailView(HolidayView, DetailView):
    pass


class HolidayListView(HolidayBaseListView, ListView):
    pass


class HolidayMonthArchiveView(
    HolidayDateView, HolidayBaseListView, MonthArchiveView):
    pass


class HolidayTodayArchiveView(
    HolidayDateView, HolidayBaseListView, TodayArchiveView):
    pass


class HolidayUpdateView(HolidayView, UpdateView):
    pass


class HolidayWeekArchiveView(
    HolidayDateView, HolidayBaseListView, WeekArchiveView):
    pass


class HolidayYearArchiveView(
    HolidayDateView, HolidayBaseListView, YearArchiveView):
    make_object_list = True



