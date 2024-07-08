from django.urls import path

from polls import views as polls_views

app_name = "polls"

# Routing information
urlpatterns = [
    path("", polls_views.index, name="index"),
    path("<int:question_id>/", polls_views.detail, name="detail"),
    path("<int:question_id>/results/", polls_views.results, name="results"),
    path("<int:question_id>/vote/", polls_views.vote, name="vote"),
]

handler404 = "app.views.error_404_view"
handler500 = "app.views.error_500_view"
