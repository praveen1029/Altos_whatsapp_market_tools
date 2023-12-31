# Generated by Django 4.2.3 on 2023-12-18 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="apply",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course", models.CharField(max_length=255)),
                ("apply_date", models.DateField(auto_now_add=True, null=True)),
                ("Name", models.CharField(max_length=255)),
                ("Email", models.EmailField(max_length=254)),
                ("Phone", models.CharField(max_length=12)),
                ("place", models.CharField(max_length=255)),
                ("status", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="courses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course_name", models.CharField(max_length=255)),
                ("course_des", models.TextField()),
                ("course_img", models.FileField(upload_to="course")),
                ("course_cre_date", models.DateField(auto_now_add=True, null=True)),
                ("course_vacancy", models.IntegerField(default=0)),
                ("rating", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="enquery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=255)),
                ("enq_date", models.DateField(auto_now_add=True, null=True)),
                ("Email", models.EmailField(max_length=254)),
                ("Phone", models.CharField(max_length=12)),
                ("project", models.CharField(max_length=255)),
                ("message", models.CharField(max_length=255)),
                ("status", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ev_head", models.CharField(max_length=255)),
                ("ev_des", models.TextField(default="")),
                ("ev_des1", models.TextField(default="")),
                ("ev_des2", models.TextField(default="")),
                ("ev_des3", models.TextField(default="")),
                ("ev_img", models.FileField(upload_to="events")),
                ("event_cre_date", models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Gallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gallery_img", models.FileField(upload_to="events")),
                ("img_cre_date", models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Newsupdate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("news_text", models.TextField()),
                ("news_cre_date", models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Poster",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ps_head", models.CharField(max_length=255)),
                ("ps_des", models.TextField(default="")),
                ("ps_des2", models.TextField(default="")),
                ("ps_des3", models.TextField(default="")),
                ("ps_img", models.FileField(upload_to="events")),
                ("ps_cre_date", models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="register",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=255)),
                ("Email", models.EmailField(max_length=254)),
                ("Phone", models.CharField(max_length=12)),
                ("date", models.CharField(max_length=20)),
                ("message", models.CharField(max_length=255)),
                ("status", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("testi_name", models.CharField(max_length=255)),
                ("testi_des", models.CharField(max_length=255)),
                ("testi_img", models.FileField(upload_to="testimonial")),
                ("testi_cre_date", models.DateField(auto_now_add=True, null=True)),
                ("testi_desecri", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="userdata",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=255)),
                ("Email", models.EmailField(max_length=254)),
                ("Phone", models.CharField(max_length=12)),
                ("massage", models.CharField(max_length=255)),
                ("status", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="UserMessages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("send_date", models.DateField(auto_now_add=True, null=True)),
                ("Name", models.CharField(max_length=100)),
                ("Email", models.EmailField(max_length=254)),
                ("subj", models.CharField(max_length=150)),
                ("message", models.CharField(max_length=255)),
                ("send_status", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Vacancys",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("loc", models.CharField(default="", max_length=255)),
                ("post_name", models.CharField(default="", max_length=255)),
                ("post_disc", models.TextField(default="")),
                ("qualific", models.CharField(default="", max_length=255)),
                ("type_job", models.CharField(default="", max_length=150)),
                ("last_date", models.DateField(null=True)),
                ("created_date", models.DateField(auto_now_add=True, null=True)),
                ("job_status", models.CharField(default=0, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Vacancy_Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("appli_loc", models.CharField(default="", max_length=255)),
                ("appli_name", models.CharField(default="", max_length=255)),
                ("appli_email", models.TextField(default="")),
                ("appli_phone", models.CharField(default="", max_length=255)),
                ("appli_date", models.DateField(auto_now_add=True, null=True)),
                ("appli_resume", models.FileField(default="", upload_to="resume")),
                ("appli_status", models.CharField(default=0, max_length=150)),
                (
                    "appli_job",
                    models.ForeignKey(
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.vacancys",
                    ),
                ),
            ],
        ),
    ]
