from django.conf.urls import url,include
from . import views

urlpatterns=[
    # url(r'^industryledgerform/$',views.industryledgerform,name='industryledgerform'),

    url(r'^poorvillage/$',views.poorvillage,name='poorvillage'),
    url(r'^poorvillagedataform/$',views.poorvillagedataform,name='poorvillagedataform'),
    url(r'^village_template_initial_paginator/$',views.village_template_initial_paginator,name='village_template_initial_paginator'),
    url(r'^village_town_change/$',views.village_town_change,name='village_town_change'),
    url(r'^village_template_query_paginator/$',views.village_template_query_paginator,name='village_template_query_paginator'),

    url(r'^poorhouse/$',views.poorhouse,name='poorhouse'),
    url(r'^poorhousedataform/$',views.poorhousedataform,name='poorhousedataform'),
    url(r'^house_template_initial_paginator/$',views.house_template_initial_paginator,name='house_template_initial_paginator'),
    url(r'^house_town_change/$',views.house_town_change,name='house_town_change'),
    url(r'^house_template_query_paginator/$',views.house_template_query_paginator,name='house_template_query_paginator'),

    url(r'^house_data_modify/$',views.house_data_modify,name='house_data_modify'),
    url(r'^house_data_delete/$',views.house_data_delete,name='house_data_delete'),

    url(r'^poorpeople/$',views.poorpeople,name='poorpeople'),
    url(r'^poorpeopledataform/$',views.poorpeopledataform,name='poorpeopledataform'),
    url(r'^people_template_initial_paginator/$',views.people_template_initial_paginator,name='people_template_initial_paginator'),
    url(r'^people_town_change/$',views.people_town_change,name='people_town_change'),
    url(r'^people_template_query_paginator/$',views.people_template_query_paginator,name='people_template_query_paginator'),

    url(r'^helper/$',views.helper,name='helper'),
    url(r'^helperdataform/$',views.helperdataform,name='helperdataform'),
    url(r'^helper_template_initial_paginator/$',views.helper_template_initial_paginator,name='helper_template_initial_paginator'),
    url(r'^helper_town_change/$',views.helper_town_change,name='helper_town_change'),
    url(r'^helper_template_query_paginator/$',views.helper_template_query_paginator,name='helper_template_query_paginator'),

    url(r'^policy/$',views.policy,name='policy'),
    url(r'^policy_template_query/$',views.policy_template_query,name='policy_template_query'),
]