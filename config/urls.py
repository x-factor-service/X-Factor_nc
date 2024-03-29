
from django.urls import path
from web.views import base_views
from common import views

urlpatterns = [
    path('', views.login, name=''),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout/'),
    path('asset/', base_views.assetweb, name='asset'),
    path('asset_detail/', base_views.assetDetailweb, name='asset_detail'),
    path('asset_detail/paging', base_views.assetDetailweb_paging, name='asset_detail_paging'),
    path('report/', base_views.report, name='report'),
    path('updateform/', views.updateform, name='updateform'),
    path('update/', views.update, name='update'),
    path('dashboard/', base_views.dashboard, name='dashboard'),
    path('reportdaily/', base_views.reportdaily, name='reportdaily'),
    path('reportmonthly/', base_views.reportmonthly, name='reportmonthly'),
    path('reportannual/', base_views.reportannual, name='reportannual'),
    path('NC_banner/', base_views.ncBanner, name='NC_banner'),
    path('customizing/', base_views.customizing, name='customizing'),
    ############################ 팝업 ############################################
    path('osVersion_moreInfo/', base_views.osVersion_moreInfo, name='osVersion_moreInfo'),
    path('osVersion_moreInfo/paging/', base_views.osVersion_moreInfo_paging, name='osVersion_moreInfo_paging'),
    path('serverBandBy_moreInfo/', base_views.serverBandBy_moreInfo, name='serverBandBy_moreInfo'),
    path('serverBandBy_moreInfo/paging/', base_views.serverBandBy_moreInfo_paging, name='serverBandBy_moreInfo_paging'),
    path('runningService_moreInfo/', base_views.runningService_moreInfo, name='runningService_moreInfo'),
    path('runningService_moreInfo/paging/', base_views.runningService_moreInfo_paging, name='runningService_moreInfo_paging'),
    path('runningService_moreInfo/paging2/', base_views.runningService_moreInfo_paging2, name='runningService_moreInfo_paging2'),
    path('memory_moreInfo/', base_views.memory_moreInfo, name='memory_moreInfo'),
    path('memory_moreInfo/paging/', base_views.memory_moreInfo_paging, name='memory_moreInfo_paging'),
    path('cpu_moreInfo/', base_views.cpu_moreInfo, name='cpu_moreInfo'),
    path('cpu_moreInfo/paging/', base_views.cpu_moreInfo_paging, name='cpu_moreInfo_paging'),
    path('disk_moreInfo/', base_views.disk_moreInfo, name='disk_moreInfo'),
    path('disk_moreInfo/paging/', base_views.disk_moreInfo_paging, name='disk_moreInfo_paging'),
    path('physicalServer_moreInfo/', base_views.physicalServer_moreInfo, name='physicalServer_moreInfo'),
    path('physicalServer_moreInfo/paging/', base_views.physicalServer_moreInfo_paging, name='physicalServer_moreInfo_paging'),
    path('gpuServer_moreInfo/', base_views.gpuServer_moreInfo, name='gpuServer_moreInfo'),
    path('gpuServer_moreInfo/paging/', base_views.gpuServer_moreInfo_paging, name='gpuServer_moreInfo_paging'),
    path('alarmCase_moreInfo/', base_views.alarmCase_moreInfo, name='alarmCase_moreInfo'),
    path('alarmCase_moreInfo/paging/', base_views.alarmCase_moreInfo_paging, name='alarmCase_moreInfo_paging'),
    # -------------------------------------- 동훈-------------------------------------
    path('iscsi_moreInfo/', base_views.isci_moreInfo, name='iscsi_moreInfo'),
    path('iscsi_moreInfo/paging/', base_views.iscsi_moreInfo_paging, name='iscsi_moreInfo_paging'),
    # -------------------------------------- 종윤-------------------------------------
    path('connectDestinationIp_moreInfo/', base_views.connectDestinationIp_moreInfo, name='connectDestinationIp_moreInfo'),
    path('connectDestinationIp_moreInfo/paging/', base_views.connectDestinationIp_moreInfo_paging, name='connectDestinationIp_moreInfo_paging'),
    path('connectSourceIp_moreInfo/', base_views.connectSourceIp_moreInfo, name='connectSourceIp_moreInfo'),
    path('connectSourceIp_moreInfo/paging/', base_views.connectSourceIp_moreInfo_paging, name='connectSourceIp_moreInfo_paging'),
    ########################### 유저 가이드 ##########################################
    path('documentation_ug/', base_views.userGuide_docs_ug, name='userGuide_docs_ug'),
    path('specification_ug/', base_views.specification_ug, name='specification_ug'),
    path('start_ug/', base_views.start_ug, name='start_ug'),
    path('dashboard_public_ug/', base_views.dashboard_public_ug, name='dashboard_public_ug'),
    path('dashboard_chart_ug/', base_views.dashboard_chart_ug, name='dashboard_chart_ug'),
    path('dashboard_etc_ug/', base_views.dashboard_etc_ug, name='dashboard_etc_ug'),
    path('weak_public_ug/', base_views.weak_public_ug, name='weak_public_ug'),
    path('weak_windows_ug/', base_views.weak_windows_ug, name='weak_windows_ug'),
    path('weak_linux_ug/', base_views.weak_linux_ug, name='weak_linux_ug'),
    path('setting_ug/', base_views.setting_ug, name='setting_ug'),
    path('report_public_ug/', base_views.report_public_ug, name='report_public_ug'),
    path('report_all_ug/', base_views.report_all_ug, name='report_all_ug'),
    path('technical_support_ug/', base_views.technical_support_ug, name='technical_support_ug'),
    path('faq_ug/', base_views.faq_ug, name='faq_ug'),
    ########################### x-factor-DF ##########################################
    path('webQuery_DF/', base_views.dataFabric_webQuery, name='webQuery_DF'),
    path('monitoring_DF/', base_views.dataFabric_monitoring, name='monitoring_DF'),
    path('Navigator_DF/', base_views.dataFabric_Navigator, name='Navigator_DF'),
    path('setting_DF/', base_views.dataFabric_setting, name='setting_DF'),
]