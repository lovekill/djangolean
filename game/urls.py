
from django.conf.urls import patterns,url
from game import views 
urlpatterns = patterns("",
        url(r'^$',views.init,name='init'),
        url(r'^test$',views.testTemp,name='testTemp'),
        url(r'^easy$',views.easyui,name="easyui")
        )
