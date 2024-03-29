from django.urls import path
from django.views.decorators.cache import never_cache

from .views import *

urlpatterns = [
    path('profile/confirm_email/ajax_resend_message/', 
         never_cache(ajax_resend_message_for_confirm_email), 
         name='user_confirm_email_resend_message'),
    path('profile/confirm_email/', 
         never_cache(ConfirmEmailUser.as_view()), 
         name='user_confirm_email'),
    path('profile/change_email/', ChangeEmailUser.as_view(), name='user_change_email'),
    path('profile/change_password/', UserChangePassword.as_view(), name='user_change_password'),
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('profile/', never_cache(UserProfile.as_view()), name='user_profile'),
    path('user_favorite_products/', 
        never_cache(UserFavoriteProducts.as_view()),
        name='user_favorite_products'),
    path('ajax_delete_product_from_favorite/',
         never_cache(ajax_delete_product_from_favorite),
         name='ajax_delete_product_from_favorite'),
    path('user_favorite_brands/',
         never_cache(UserFavoriteBrands.as_view()),
         name='user_favorite_brands'),
    path('ajax_delete_brand_from_favorite/',
         never_cache(ajax_delete_brand_from_favorite),
         name='ajax_delete_brand_from_favorite'),
    path('purchase_history_user/',
        never_cache(PurchaseHistoryForUser.as_view()),
        name='purchase_history_user'),
    path('left_feedback/',
         never_cache(UserLeftFeedbacks.as_view()),
         name='left_feedback')
]
