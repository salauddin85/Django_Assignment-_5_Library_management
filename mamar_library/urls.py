
from django.contrib import admin
from django.urls import path,include
from core.views import ShowsALLBook

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ShowsALLBook.as_view(),name = 'home'),
    path('accounts/',include('accounts.urls')),
    path('books/',include('book.urls')),
    path('category_slug/<slug:category_slug>',ShowsALLBook.as_view(),name = 'category_wise_book'),
    path('borrow/',include('borrow_book.urls')),
    path('Transaction/',include('Transactions.urls')),
    path('return_book/',include('return_book.urls'))

    
    

]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# <slug:category_slug>