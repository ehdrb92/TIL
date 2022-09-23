# Django migration 적용내역 확인하기

Django 사용시 makemigrations를 한 이후 해당 내역이 migration이 되었는지 확인할 수 있다.

```
python manage.py showmigraions

admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
 [X] 0012_alter_user_first_name_max_length
blog1
 [X] 0001_initial
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
instagram
 [X] 0001_initial
 [X] 0002_post_is_public
sessions
 [X] 0001_initial
```

**python manage.py showmigrations**를 입력하면 각 앱 별로 migration이 된 내역을 확인할 수 있다.