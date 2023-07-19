# Generated by Django 4.1.8 on 2023-07-17 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AllergicList",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "allergic_list",
            },
        ),
        migrations.CreateModel(
            name="GiverInfo",
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
                ("location", models.CharField(max_length=5)),
            ],
            options={
                "db_table": "giver_info",
            },
        ),
        migrations.CreateModel(
            name="OrderInfo",
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
                ("need_pair_id", models.IntegerField()),
                ("order_price", models.IntegerField()),
                ("order_date", models.DateTimeField()),
            ],
            options={
                "db_table": "order_info",
            },
        ),
        migrations.CreateModel(
            name="SkillList",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "skill_list",
            },
        ),
        migrations.CreateModel(
            name="UserRelation",
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
                ("relation_name", models.CharField(help_text="相對的關係", max_length=10)),
                (
                    "related",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_user_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_relation_user_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "user_relation",
            },
        ),
        migrations.CreateModel(
            name="UserNeed",
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
                ("need_category", models.CharField(max_length=100)),
                ("need_time", models.JSONField()),
                ("solved", models.BooleanField(default=False)),
                ("status", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("create_by", models.IntegerField()),
                ("update_at", models.DateTimeField(auto_now=True)),
                ("update_by", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_need_user_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "user_need",
            },
        ),
        migrations.CreateModel(
            name="UserInfo",
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
                ("address", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("create_by", models.IntegerField()),
                ("update_at", models.DateTimeField(auto_now=True)),
                ("update_by", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "user_info",
            },
        ),
        migrations.CreateModel(
            name="NeederInfo",
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
                ("age", models.IntegerField()),
                ("birth_date", models.DateTimeField()),
                ("heath_status", models.IntegerField()),
                ("location", models.CharField(max_length=5)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("create_by", models.IntegerField()),
                ("update_at", models.DateTimeField(auto_now=True)),
                ("update_by", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="needer_info_user_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "needer_info",
            },
        ),
        migrations.CreateModel(
            name="GiverTime",
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
                ("need_pair_time", models.DateTimeField()),
                (
                    "giver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="giver_id",
                        to="accounts.giverinfo",
                    ),
                ),
                (
                    "need_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="need_user_id",
                        to="accounts.neederinfo",
                    ),
                ),
            ],
            options={
                "db_table": "need_pair_time",
            },
        ),
        migrations.AddField(
            model_name="giverinfo",
            name="skill",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="skill_list_id",
                to="accounts.skilllist",
            ),
        ),
        migrations.AddField(
            model_name="giverinfo",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="giver_info_user_id",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Allergic",
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
                (
                    "allergic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="allergic_list_id",
                        to="accounts.allergiclist",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="allergic_user_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "allergic",
            },
        ),
    ]