from django.urls import path
from . import views

app_name = 'manuscripts'

urlpatterns = [    
    # 네비게이션에서 쓰는 이름들
    path("submission/", views.submission, name="submission"),
    path("ai-reviewer/", views.ai_reviewer_view, name="ai_reviewer"),
    path("editorial/", views.editorial_view, name="editorial"),
    path("publication/", views.publication_view, name="publication"),
    path("dashboard/", views.dashboard_view, name="dashboard"),

    path("gallery/", views.gallery_view, name="gallery"),    
    path("history/", views.history_view, name="history"),
    path("news/", views.news_view, name="news"),
]