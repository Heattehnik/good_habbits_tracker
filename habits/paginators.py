from rest_framework.pagination import PageNumberPagination


class HabitsPaginator(PageNumberPagination):
    page_size = 5


class PlacesPaginator(PageNumberPagination):
    page_size = 5