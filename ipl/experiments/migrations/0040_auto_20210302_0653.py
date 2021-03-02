# Generated by Django 3.1.7 on 2021-03-02 05:53

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0039_auto_20210302_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='demographic_data_page_tpl',
            field=tinymce.models.HTMLField(default='{% extends "experiments/base.html" %} {% block title %}Persönliche Angaben{% endblock %} {% block content %}\n<div class="container">\n    <div class="row">\n        <div class="col text-center">\n            <h1>Persönliche Angaben</h1>\n        </div>\n    </div>\n    <div class="row">\n        <div class="col">\n            <div class="card">\n                <div class="card-body">\n                    {% if error_message %}\n                    <div class="alert alert-danger" role="alert">\n                        {{ error_message }}\n                    </div>{% endif %}\n\n                    <form action="{% url \'experiments:subjectFormSubmit\' experiment.id %}" method="post" novalidate>\n                        {% csrf_token %}\n                        <p class="card-text">\n                            Bitte füllen Sie die Felder unten aus. Sie müssen mindestens alle mit einem * versehenen Felder ausfüllen, um an der Studie teilnehmen zu können.\n                        </p>\n                        <p><br><span class="asterix">* Pflichtfeld</span></p>\n                        {% for field in subject_data_form %}\n                        {% if field.name == \'resolution_w\' or field.name == \'resolution_h\' %}\n                            {{ field }}\n                        {% else %}\n                        <div class="q-item" value="{{ forloop.counter }}">\n                            {% if field.field.required %}\n                            <div class="field-wrapper question-required">\n                                {{ field.errors }}\n                                <label class="label-inline">{{ field.label }} <span class="asterix">*</span></label>\n                            {% else %}\n                            <div class="field-wrapper">\n                                {{ field.errors }}\n                                <label class="label-inline">{{ field.label }}</label>\n                            {% endif %}\n                                <div class="form-field-body">\n                                    {{ field }}\n                                </div>\n                                <small class="form-text text-muted">{{ field.help_text }}</small>\n                            </div>\n                        </div><br>\n                        {% endif %}\n                        {% endfor %}\n                        <button type="submit" class="btn btn-primary">Weiter</button>\n                    </form>\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n{% endblock %}', verbose_name='demographic data page template'),
        ),
    ]