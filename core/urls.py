from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path("logout/", views.user_logout, name="logout"),
    
    
    path('register/', views.register_user, name='register'),
    path('awareness/', views.awareness, name='awareness'),
    path('tools/password-checker/', views.password_checker, name='password_checker'),
    path('tools/', views.tools_home, name='tools'),
    path('tools/password-generator/', views.password_generator, name='password_generator'),
    path('tools/hash-generator/', views.hash_generator, name='hash_generator'),
    path('tools/password-leak-checker/', views.password_leak_checker, name='password_leak_checker'),
    path('tools/pin-generator/', views.pin_generator, name='pin_generator'),
    path('tools/phishing-detector/', views.phishing_detector, name='phishing_detector'),
    path('tools/url-scanner/', views.url_scanner, name='url_scanner'),
    path('tools/malware-checker/', views.malware_checker, name='malware_checker'),
    path('tools/email-analyzer/', views.email_analyzer, name='email_analyzer'),
    path('tools/fake-site-detector/', views.fake_site_detector, name='fake_site_detector'),
    path('tools/ip-finder/', views.ip_finder, name='ip_finder'),
    path('tools/ip-location/', views.ip_location, name='ip_location'),
    path('tools/browser-info/', views.browser_info, name='browser_info'),
    path('tools/device-info/', views.device_info, name='device_info'),
    path('tools/cookies-viewer/', views.cookies_viewer, name='cookies_viewer'),
    path('secret-zone/', views.secret_zone, name='secret_zone'),
    path('secret/secure-keyboard/', views.secure_keyboard, name='secure_keyboard'),
    path('secret/notepad-locker/', views.notepad_locker, name='notepad_locker'),
    path('secret/hacker-terminal/', views.hacker_terminal, name='hacker_terminal'),
    path('secret/fake-virus/', views.fake_virus, name='fake_virus'),
    path('secret/adware-simulator/', views.adware_simulator, name='adware_simulator'),
    path('secret/fake-virus-alert/', views.fake_virus_alert, name='fake_virus_alert'),
    path('secret/fake-windows-update/', views.fake_windows_update, name='fake_windows_update'),
    path('secret/spyware-simulator/', views.spyware_simulator, name='spyware_simulator'),
    path('secret/keylogger-simulator/', views.keylogger_simulator, name='keylogger_simulator'),
    path('secret/spy-camera/', views.spy_camera, name='spy_camera'),
    path('secret/matrix-terminal/', views.matrix_terminal, name='matrix_terminal'),
    path('secret/hacker-typing-test/', views.hacker_typing_test, name='hacker_typing_test'),
    path('secret/ransomware-simulator/', views.ransomware_simulator, name='ransomware_simulator'),
    path('secret/face-scanner/', views.face_scanner, name='face_scanner'),
    path('secret/target-tracker/', views.target_tracker, name='target_tracker'),
    path('quiz/', views.quiz_topics, name='quiz_topics'),
    path('quiz/<int:topic_id>/',views.quiz_page,name='quiz_page'),
    path('quiz/result/',views.quiz_result,name='quiz_result'),
    path('dashboard/',views.user_dashboard,name='dashboard'),
    path(
    'change-password/',
    auth_views.PasswordChangeView.as_view(
        template_name='core/change_password.html'
    ),
    name='change_password'
),
    













    






















]
