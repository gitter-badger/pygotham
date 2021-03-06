"""Admin for schedule-related models."""

from pygotham.admin.utils import model_view
from pygotham.schedule import models

# This line is really long because pep257 needs it to be on one line.
__all__ = ('DayModelView', 'RoomModelView', 'SlotModelView', 'PresentationModelView')

CATEGORY = 'Schedule'


DayModelView = model_view(
    models.Day,
    'Days',
    CATEGORY,
    column_default_sort='date',
    column_filters=('event.slug', 'event.name'),
    column_list=('date', 'event'),
    form_columns=('event', 'date'),
)


RoomModelView = model_view(
    models.Room,
    'Rooms',
    CATEGORY,
    column_default_sort='order',
    form_columns=('name', 'order'),
)


SlotModelView = model_view(
    models.Slot,
    'Slots',
    CATEGORY,
    column_default_sort='start',
    column_filters=('day', 'day.event.slug', 'day.event.name'),
    column_list=(
        'day', 'rooms', 'kind', 'start', 'end', 'presentation',
        'content_override',
    ),
    form_columns=('day', 'rooms', 'kind', 'start', 'end', 'content_override'),
)


PresentationModelView = model_view(
    models.Presentation,
    'Presentations',
    CATEGORY,
)
