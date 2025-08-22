from api.spectacular.urls import urlpatterns as doc_urls
from todo_list.urls import urlpatterns as todo_urls
from users.urls import urlpatterns as users_url

app_name = 'api'

urlpatterns = []
urlpatterns += doc_urls
urlpatterns += todo_urls
urlpatterns += users_url
