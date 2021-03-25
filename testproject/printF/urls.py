from django.urls import path, include
from .views import printVals, addVals, storeDB, fetchStore, fetchByID, clearDB, userregistration, signin, signupDjango, signinDjango, signoutDjango

urlpatterns = [
    path('print/', printVals),
    path('add/' ,addVals),
    path('store/', storeDB),
    path('find', fetchStore),
    path('findByID', fetchByID),
    path('deleteByID/<id>', clearDB),
    path('register', userregistration,name="register"),
    path('signin', signin, name="signin"),
    path('signupDjango', signupDjango, name="djangoSignup"),
    path('signinDjango',signinDjango, name="djangoSignin"),
    path('signoutDjango', signoutDjango, name="signoutDjango")
]
