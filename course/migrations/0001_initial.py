# Generated by Django 3.2.11 on 2022-02-21 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('room_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='教室名', max_length=100, unique=True, verbose_name='教室名')),
                ('is_common', models.BooleanField(default=True, help_text='是否可作为自习室', verbose_name='是否自习室')),
            ],
            options={
                'verbose_name': '教室',
                'verbose_name_plural': '教室',
            },
        ),
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('info_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('period', models.IntegerField(help_text='从2007.9算起的第?学期', verbose_name='时期')),
                ('semester', models.IntegerField(choices=[(1, '大一上'), (2, '大一下'), (3, '大二上'), (4, '大二下'), (5, '大三上'), (6, '大三下'), (7, 'S1'), (8, 'S2'), (9, 'S3'), (10, 'S4'), (11, 'S5'), (12, 'S6'), (13, 'S7'), (14, 'S8')], help_text='从大一上算起的第?学期 ∈ [1,14]', verbose_name='学期')),
                ('code', models.CharField(blank=True, default='', help_text='课程编号(如CS21,ES22)', max_length=100, null=True)),
                ('ch_name', models.CharField(help_text='课程中文名', max_length=100, unique=True, verbose_name='中文名')),
                ('en_name', models.CharField(blank=True, help_text='课程英语名', max_length=100, null=True, verbose_name='English')),
                ('fr_name', models.CharField(blank=True, help_text='课程法语名', max_length=100, null=True, verbose_name='Français')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('type_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='类型名', max_length=100, unique=True, verbose_name='类型名')),
                ('color', models.CharField(help_text='颜色，六位字符，例如：FFFFFF', max_length=6, verbose_name='颜色')),
            ],
            options={
                'verbose_name': '课程类型',
                'verbose_name_plural': '课程类型',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('period', models.IntegerField(help_text='从2007.9算起的第?学期', verbose_name='时期')),
                ('semester', models.IntegerField(choices=[(1, '大一上'), (2, '大一下'), (3, '大二上'), (4, '大二下'), (5, '大三上'), (6, '大三下'), (7, 'S1'), (8, 'S2'), (9, 'S3'), (10, 'S4'), (11, 'S5'), (12, 'S6'), (13, 'S7'), (14, 'S8')], help_text='从大一上算起的第?学期 ∈ [1,14]', verbose_name='学期')),
                ('name', models.CharField(help_text='分组名称，例如：PA', max_length=100, verbose_name='分组名称')),
            ],
            options={
                'verbose_name': '分组',
                'verbose_name_plural': '分组',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('content', models.CharField(help_text='对本次变动的描述', max_length=255, verbose_name='描述')),
                ('link', models.TextField(blank=True, help_text='点击通知时跳转链接', null=True, verbose_name='链接')),
                ('priority', models.IntegerField(default=1, help_text='数字越大优先级越高', verbose_name='优先级')),
                ('validity', models.BooleanField(default=True, help_text='是否生效', verbose_name='是否生效')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='这条记录的更新时间', verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '系统通知',
                'verbose_name_plural': '系统通知',
            },
        ),
        migrations.CreateModel(
            name='SemesterConfig',
            fields=[
                ('config_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('current_period', models.IntegerField(help_text='从2007.9算起的第?学期', verbose_name='当前时期')),
                ('week1_monday_date', models.DateTimeField(help_text='本学期第一周星期一的日期', verbose_name='学期开始日期')),
                ('max_week', models.IntegerField(default=20, help_text='本学期共计多少周', verbose_name='最大周数')),
            ],
            options={
                'verbose_name': '学期信息配置',
                'verbose_name_plural': '学期信息配置',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='授课教师姓名', max_length=100, unique=True, verbose_name='姓名')),
                ('slug', models.CharField(blank=True, max_length=300, null=True)),
                ('validity', models.BooleanField(default=True, help_text='是否参与当前教学计划', verbose_name='是否生效')),
            ],
            options={
                'verbose_name': '授课教师',
                'verbose_name_plural': '授课教师',
            },
        ),
        migrations.CreateModel(
            name='CoursePlan',
            fields=[
                ('plan_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('method', models.CharField(choices=[('Course', '理论课'), ('TD', '习题课'), ('TP', '实验课'), ('DS', '考试')], help_text='Course/TD/TP/DS', max_length=8, verbose_name='授课方式')),
                ('groups', models.ManyToManyField(help_text='M2M Plan&Group', related_name='group_plan', to='course.Group', verbose_name='分组')),
                ('info', models.ForeignKey(help_text='FK-CourseInfo', on_delete=django.db.models.deletion.CASCADE, related_name='info_plan', to='course.courseinfo', verbose_name='课程信息')),
                ('teacher', models.ForeignKey(help_text='FK-Teacher', on_delete=django.db.models.deletion.CASCADE, related_name='teacher_plan', to='course.teacher', verbose_name='授课教师')),
            ],
            options={
                'verbose_name': '教学计划',
                'verbose_name_plural': '教学计划',
            },
        ),
        migrations.AddField(
            model_name='courseinfo',
            name='type',
            field=models.ForeignKey(help_text='FK-CourseType', on_delete=django.db.models.deletion.CASCADE, related_name='type_info', to='course.coursetype', verbose_name='课程类型'),
        ),
        migrations.CreateModel(
            name='CourseChangeLog',
            fields=[
                ('log_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('action', models.CharField(choices=[('Create', '新增'), ('Update', '更新'), ('Delete', '删除')], help_text='新增/更新/删除', max_length=8, verbose_name='动作')),
                ('description', models.CharField(blank=True, help_text='对本次变动的描述', max_length=255, null=True, verbose_name='描述')),
                ('update_time', models.DateTimeField(auto_now_add=True, help_text='该变动发生的时间', verbose_name='更新时间')),
                ('color', models.CharField(blank=True, help_text='颜色，六位字符，例如：FFFFFF', max_length=6, null=True, verbose_name='颜色')),
                ('period', models.IntegerField(blank=True, help_text='从2007.9算起的第?学期', null=True, verbose_name='时期')),
                ('semester', models.IntegerField(blank=True, choices=[(1, '大一上'), (2, '大一下'), (3, '大二上'), (4, '大二下'), (5, '大三上'), (6, '大三下'), (7, 'S1'), (8, 'S2'), (9, 'S3'), (10, 'S4'), (11, 'S5'), (12, 'S6'), (13, 'S7'), (14, 'S8')], help_text='从大一上算起的第?学期 ∈ [1,14]', null=True, verbose_name='学期')),
                ('code', models.CharField(blank=True, default='', help_text='课程编号(如CS21,ES22)', max_length=100, null=True)),
                ('ch_name', models.CharField(blank=True, help_text='课程中文名', max_length=100, null=True, verbose_name='中文名')),
                ('en_name', models.CharField(blank=True, help_text='课程英语名', max_length=100, null=True, verbose_name='English')),
                ('fr_name', models.CharField(blank=True, help_text='课程法语名', max_length=100, null=True, verbose_name='Français')),
                ('method', models.CharField(choices=[('Course', '理论课'), ('TD', '习题课'), ('TP', '实验课'), ('DS', '考试')], default='Course', help_text='Course/TD/TP/DS', max_length=8, verbose_name='授课方式')),
                ('group_ids', models.CharField(blank=True, help_text='group_id(s),以字符串储存列表', max_length=100, null=True, verbose_name='分组')),
                ('teacher_name', models.CharField(blank=True, help_text='授课教师姓名', max_length=200, null=True, verbose_name='教师名')),
                ('plan', models.ForeignKey(help_text='FK-CoursePlan', on_delete=django.db.models.deletion.CASCADE, related_name='plan_log', to='course.courseplan', verbose_name='教学计划')),
            ],
            options={
                'verbose_name': '课程更新日志',
                'verbose_name_plural': '课程更新日志',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('date', models.DateField(help_text='这节课的上课日期', verbose_name='这节课的上课日期')),
                ('which_lesson', models.IntegerField(choices=[(1, '第1,2节课'), (2, '第3,4节课'), (3, '第5,6节课'), (4, '第7,8节课'), (5, '第9,10节课')], help_text='第?节课，∈[1,5]', verbose_name='第?节课')),
                ('note', models.CharField(blank=True, default=None, help_text='补充说明', max_length=255, null=True, verbose_name='备注')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='这条记录的更新时间', verbose_name='更新时间')),
                ('color', models.CharField(blank=True, help_text='颜色，六位字符，例如：FFFFFF', max_length=6, null=True, verbose_name='颜色')),
                ('period', models.IntegerField(blank=True, help_text='从2007.9算起的第?学期', null=True, verbose_name='时期')),
                ('semester', models.IntegerField(blank=True, choices=[(1, '大一上'), (2, '大一下'), (3, '大二上'), (4, '大二下'), (5, '大三上'), (6, '大三下'), (7, 'S1'), (8, 'S2'), (9, 'S3'), (10, 'S4'), (11, 'S5'), (12, 'S6'), (13, 'S7'), (14, 'S8')], help_text='从大一上算起的第?学期 ∈ [1,14]', null=True, verbose_name='学期')),
                ('code', models.CharField(blank=True, default='', help_text='课程编号(如CS21,ES22)', max_length=100, null=True)),
                ('ch_name', models.CharField(blank=True, help_text='课程中文名', max_length=100, null=True, verbose_name='中文名')),
                ('en_name', models.CharField(blank=True, help_text='课程英语名', max_length=100, null=True, verbose_name='English')),
                ('fr_name', models.CharField(blank=True, help_text='课程法语名', max_length=100, null=True, verbose_name='Français')),
                ('method', models.CharField(choices=[('Course', '理论课'), ('TD', '习题课'), ('TP', '实验课'), ('DS', '考试')], default='Course', help_text='Course/TD/TP/DS', max_length=8, verbose_name='授课方式')),
                ('group_ids', models.CharField(blank=True, help_text='group_id(s),以字符串储存列表', max_length=100, null=True, verbose_name='分组')),
                ('teacher_name', models.CharField(blank=True, help_text='授课教师姓名', max_length=200, null=True, verbose_name='教师名')),
                ('room_name', models.CharField(blank=True, help_text='教室名', max_length=100, null=True, verbose_name='教室名')),
                ('plan', models.ForeignKey(help_text='FK-CoursePlan', on_delete=django.db.models.deletion.CASCADE, related_name='plan_course', to='course.courseplan', verbose_name='教学计划')),
                ('room', models.ForeignKey(help_text='FK-Classroom', on_delete=django.db.models.deletion.CASCADE, related_name='room_course', to='course.classroom', verbose_name='教室')),
            ],
            options={
                'verbose_name': '排课记录',
                'verbose_name_plural': '排课记录',
            },
        ),
    ]
