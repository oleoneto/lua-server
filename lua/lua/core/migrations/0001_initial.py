# Generated by Django 2.1.7 on 2019-04-26 21:26

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import lua.core.models.helpers.assignment
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('photo', models.ImageField(blank=True, upload_to='users/profiles/')),
                ('internal_email', models.EmailField(blank=True, max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_users',
                'ordering': ['-created_at'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('answer', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_assignment_question_answers',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('due_date', models.DateTimeField(default=lua.core.models.helpers.assignment.get_due_date)),
                ('points', models.IntegerField(default=100, help_text='Specify how many points this assignment is worth')),
                ('public', models.BooleanField(default=True)),
                ('access_code', models.UUIDField(default=uuid.uuid4, help_text='Code for students searching for your course', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_assignments',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AssignmentFile',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, upload_to=lua.core.models.helpers.assignment.assignment_filepath)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='files', to='core.Assignment')),
            ],
            options={
                'db_table': 'school_assignment_files',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AssignmentType',
            fields=[
                ('id', models.PositiveIntegerField(choices=[(1, 'Homework'), (2, 'Quiz'), (3, 'Project'), (4, 'Report'), (5, 'Essay'), (6, 'Test')], primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_assignment_types',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_comments',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, help_text='What this course is about', max_length=700)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_courses',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CourseOffer',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('start_date', models.DateField(help_text='Date when classes will begin')),
                ('end_date', models.DateField(help_text='Date when classes will end')),
                ('enrollment_limit', models.PositiveIntegerField(default=50, help_text='Limit the number of students in course')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='offers', to='core.Course')),
            ],
            options={
                'db_table': 'school_course_offers',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_offer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='enrollments', to='core.CourseOffer')),
            ],
            options={
                'db_table': 'school_enrollments',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Event', max_length=144)),
                ('day', models.DateField(help_text='Day of the event', verbose_name='Day of the event')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='Starting time')),
                ('end_time', models.TimeField(help_text='Final time', verbose_name='Final time')),
                ('notes', ckeditor.fields.RichTextField(blank=True, help_text='Textual Notes', null=True, verbose_name='Textual Notes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Event',
                'db_table': 'core_events',
                'ordering': ['day', 'start_time', 'title'],
            },
        ),
        migrations.CreateModel(
            name='FileSubmission',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=lua.core.models.helpers.assignment.assignment_submission_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='file_submissions', to='core.Assignment')),
            ],
            options={
                'db_table': 'school_assignment_file_submissions',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Gradebook',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_offer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='gradebooks', to='core.CourseOffer')),
            ],
            options={
                'db_table': 'school_gradebooks',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GradebookAssignmentEntry',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('grade', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='gradebook_entries', to='core.Assignment')),
                ('gradebook', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assignment_entries', to='core.Gradebook')),
            ],
            options={
                'db_table': 'school_gradebook_assignment_entries',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GradebookNoteEntry',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('note', models.TextField(max_length=700)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gradebook', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='note_entries', to='core.Gradebook')),
            ],
            options={
                'db_table': 'school_gradebook_note_entries',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('is_active', models.BooleanField(default=True, help_text='Activate or deactivate instructor account')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_user_instructors',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='LearningLevel',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'Knowledge'), (2, 'Comprehension'), (3, 'Application'), (4, 'Analysis'), (5, 'Synthesis'), (6, 'Evaluation'), (7, 'Critical Thinking')], primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_learning_levels',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='LearningObjective',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='What should we call this learning objective?', max_length=250)),
                ('description', models.TextField(help_text='Describe what this learning objective seeks to accomplish')),
                ('is_optional', models.BooleanField(default=False, help_text='Set this if the objective is not mandatory')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_learning_objectives',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='LearningObjectiveFile',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('learning-objectives', models.FileField(upload_to='learning-objectives/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('learning_objective', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='files', to='core.LearningObjective')),
            ],
            options={
                'db_table': 'school_learning_objective_files',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='LearningOutcome',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('is_graded', models.BooleanField(default=True, help_text='Specifies if the outcome counts towards overall grade')),
                ('grade_requirement', models.PositiveIntegerField(default=100, help_text='Minimum passing grade for your students')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('learning_levels', models.ManyToManyField(blank=True, related_name='outcomes', to='core.LearningLevel')),
                ('learning_objective', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='outcomes', to='core.LearningObjective')),
            ],
            options={
                'db_table': 'school_learning_objective_outcomes',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('content', ckeditor.fields.RichTextField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('is_draft', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_lectures',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('option', models.CharField(blank=True, max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_assignment_question_options',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('content', ckeditor.fields.RichTextField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('is_draft', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_posts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('question', ckeditor.fields.RichTextField()),
                ('number', models.PositiveIntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='questions', to='core.Assignment')),
            ],
            options={
                'db_table': 'school_assignment_questions',
                'ordering': ['-created_at', 'number'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(3, 'Student'), (2, 'Faculty'), (1, 'Staff')], primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_roles',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('level', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_teacher_specialties',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(editable=False, max_length=30, unique=True)),
                ('date_of_birth', models.DateField(blank=True)),
                ('is_active', models.BooleanField(default=True, help_text='Active or deactivate student account')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_students',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='StudyPlan',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_plans', to='core.Instructor')),
                ('learning_objectives', models.ManyToManyField(blank=True, related_name='study_plans', to='core.LearningObjective')),
            ],
            options={
                'db_table': 'school_student_plans',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')], primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'school_terms',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Waitlist',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_offer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='waitlists', to='core.CourseOffer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='waitlists', to='core.Student')),
            ],
            options={
                'db_table': 'school_waitlists',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_guest_users',
            },
            bases=('core.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='plans',
            field=models.ManyToManyField(help_text='Individual study plans for student', to='core.StudyPlan'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='student_account', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='flags',
            field=models.ManyToManyField(blank=True, related_name='post_flags', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='options', to='core.Question'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='lectures', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lecture',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='lecture_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='instructor',
            name='specialties',
            field=models.ManyToManyField(blank=True, related_name='instructors', to='core.Specialty'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='teacher_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gradebook',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='gradebooks', to='core.Student'),
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='event_invitations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='enrollments', to='core.Student'),
        ),
        migrations.AddField(
            model_name='courseoffer',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='courses_taught', to='core.Instructor'),
        ),
        migrations.AddField(
            model_name='courseoffer',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='courses_offered', to='core.Term'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='flags',
            field=models.ManyToManyField(blank=True, related_name='comment_flags', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.Post'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignment_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assignments', to='core.AssignmentType'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assignments', to='core.Course'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answers', to='core.Question'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='waitlist',
            unique_together={('student', 'course_offer')},
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('assignment', 'number')},
        ),
        migrations.AddField(
            model_name='guest',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='guests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('student', 'course_offer')},
        ),
    ]
