# Generated by Django 2.2.7 on 2019-11-09 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_auto_20191108_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_memberships', to='subject.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_group', to='accounts.TeacherProfileInfo')),
            ],
            options={
                'unique_together': {('course', 'user')},
            },
        ),
        migrations.CreateModel(
            name='StudentMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_memberships', to='subject.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_group', to='accounts.StudentProfileInfo')),
            ],
            options={
                'unique_together': {('course', 'user')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ManyToManyField(blank=True, related_name='tutor', to='subject.TeacherMember'),
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='student', to='subject.StudentMember'),
        ),
    ]
