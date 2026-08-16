from pathlib import Path

base = Path(__file__).resolve().parent
files = {
    'accounts/templates/base.html': '''{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Job Portal{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <header class="site-header">
        <div class="container header-bar">
            <a class="brand" href="{% url 'home' %}">JobPortal</a>
            <nav>
                <a href="{% url 'job-list' %}">Jobs</a>
                {% if user.is_authenticated %}
                    <a href="{% url 'my-jobs' %}">My Jobs</a>
                    <a href="{% url 'my-applications' %}">Applications</a>
                    <a href="{% url 'job-create' %}">Post Job</a>
                {% endif %}
            </nav>
            <div class="user-links">
                {% if user.is_authenticated %}
                    <span class="user-label">Hello, {{ user.username }}</span>
                    <a class="button secondary" href="{% url 'logout' %}">Logout</a>
                {% else %}
                    <a class="button secondary" href="{% url 'login' %}">Login</a>
                    <a class="button primary" href="{% url 'signup' %}">Sign Up</a>
                {% endif %}
            </div>
        </div>
    </header>

    <main class="container">
        {% if messages %}
            <div class="messages">
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }}">{{ message }}</div>
                {% endfor %}
            </div>
        {% endif %}
        {% block content %}{% endblock %}
    </main>

    <footer class="site-footer">
        <div class="container">
            <p>Built for job seekers and employers. 2026.</p>
        </div>
    </footer>
</body>
</html>
''',
    'accounts/templates/home.html': '''{% extends 'base.html' %}
{% block title %}Home | JobPortal{% endblock %}
{% block content %}
    <section class="hero">
        <div class="hero-copy">
            <h1>Find your next opportunity.</h1>
            <p>Browse jobs, post positions, and connect with the right talent.</p>
            <div class="hero-actions">
                <a class="button primary" href="{% url 'job-list' %}">Browse Jobs</a>
                <a class="button secondary" href="{% url 'signup' %}">Create Account</a>
            </div>
        </div>
        <div class="hero-visual">
            <div class="feature-card">
                <h2>Post jobs quickly.</h2>
                <p>Create listings in seconds and manage applicants from your dashboard.</p>
            </div>
        </div>
    </section>
{% endblock %}
''',
    'accounts/templates/accounts/signup.html': '''{% extends 'base.html' %}
{% block title %}Sign Up | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <h1>Create your account</h1>
        <p>Register as an employer or job seeker to start using the portal.</p>
        <form method="post" class="form-card">
            {% csrf_token %}
            {{ form.as_p }}
            <button class="button primary" type="submit">Sign Up</button>
        </form>
        <p class="form-footer">Already have an account? <a href="{% url 'login' %}">Login here</a>.</p>
    </section>
{% endblock %}
''',
    'accounts/templates/accounts/login.html': '''{% extends 'base.html' %}
{% block title %}Login | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <h1>Login</h1>
        <form method="post" class="form-card">
            {% csrf_token %}
            {{ form.as_p }}
            <button class="button primary" type="submit">Login</button>
        </form>
        <p class="form-footer"><a href="{% url 'password-reset' %}">Forgot password?</a></p>
        <p class="form-footer">Don't have an account? <a href="{% url 'signup' %}">Sign up</a>.</p>
    </section>
{% endblock %}
''',
    'accounts/templates/accounts/password_change.html': '''{% extends 'base.html' %}
{% block title %}Change Password | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <h1>Change Password</h1>
        <form method="post" class="form-card">
            {% csrf_token %}
            {{ form.as_p }}
            <button class="button primary" type="submit">Update Password</button>
        </form>
    </section>
{% endblock %}
''',
    'accounts/templates/accounts/password_change_done.html': '''{% extends 'base.html' %}
{% block title %}Password Changed | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <h1>Password Changed</h1>
        <p>Your password has been updated successfully.</p>
        <a class="button primary" href="{% url 'job-list' %}">Back to Jobs</a>
    </section>
{% endblock %}
''',
    'accounts/templates/accounts/password_reset.html': '''{% extends 'base.html' %}
{% block title %}Reset Password | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <h1>Password Reset</h1>
        <p>Enter your email address and we'll send instructions to reset your password.</p>
        <form method="post" class="form-card">
            {% csrf_token %}
            {{ form.as_p }}
            <button class="button primary" type="submit">Send Reset Link</button>
        </form>
    </section>
{% endblock %}
''',
    'accounts/templates/accounts/password_reset_done.html': '''{% extends 'base.html' %}
{% block title %}Reset Sent | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <h1>Reset Email Sent</h1>
        <p>Check your email for password reset instructions.</p>
    </section>
{% endblock %}
''',
    'accounts/templates/accounts/password_reset_confirm.html': '''{% extends 'base.html' %}
{% block title %}Set New Password | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <h1>Set a New Password</h1>
        <form method="post" class="form-card">
            {% csrf_token %}
            {{ form.as_p }}
            <button class="button primary" type="submit">Save Password</button>
        </form>
    </section>
{% endblock %}
''',
    'accounts/templates/accounts/password_reset_complete.html': '''{% extends 'base.html' %}
{% block title %}Password Reset Complete | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <h1>Password Reset Complete</h1>
        <p>Your password has been reset successfully. You may now <a href="{% url 'login' %}">login</a>.</p>
    </section>
{% endblock %}
''',
    'jobs/templates/jobs/job_list.html': '''{% extends 'base.html' %}
{% block title %}Jobs | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <div class="page-header">
            <div>
                <h1>Available Jobs</h1>
                <p>Explore current openings and apply with one click.</p>
            </div>
            <a class="button primary" href="{% url 'job-create' %}">Post a Job</a>
        </div>

        <div class="grid-list">
            {% if all_jobs %}
                {% for job in all_jobs %}
                    <article class="job-card">
                        <h2><a href="{% url 'job-detail' job.pk %}">{{ job.title }}</a></h2>
                        <p class="meta">Posted by {{ job.posted_by.username }} · {{ job.date_posted|date:'M d, Y' }}</p>
                        <p>{{ job.description|truncatechars:160 }}</p>
                        <div class="card-bottom">
                            <span class="badge">${{ job.salary }}</span>
                            <a class="button secondary" href="{% url 'job-detail' job.pk %}">View details</a>
                        </div>
                    </article>
                {% endfor %}
            {% else %}
                <p>No jobs are available right now. Check back soon or post a new opening.</p>
            {% endif %}
        </div>

        {% if is_paginated %}
            <div class="pagination">
                {% if page_obj.has_previous %}
                    <a href="?page={{ page_obj.previous_page_number }}" class="button secondary">Previous</a>
                {% endif %}
                <span>Page {{ page_obj.number }} of {{ paginator.num_pages }}</span>
                {% if page_obj.has_next %}
                    <a href="?page={{ page_obj.next_page_number }}" class="button secondary">Next</a>
                {% endif %}
            </div>
        {% endif %}
    </section>
{% endblock %}
''',
    'jobs/templates/jobs/job_detail.html': '''{% extends 'base.html' %}
{% block title %}{{ job.title }} | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <div class="page-header">
            <div>
                <h1>{{ job.title }}</h1>
                <p class="meta">Posted by {{ job.posted_by.username }} · {{ job.date_posted|date:'M d, Y' }}</p>
            </div>
            <div class="detail-actions">
                <span class="badge">${{ job.salary }}</span>
                {% if user == job.posted_by %}
                    <a class="button secondary" href="{% url 'job-update' job.pk %}">Edit</a>
                    <a class="button danger" href="{% url 'job-delete' job.pk %}">Delete</a>
                {% endif %}
            </div>
        </div>

        <div class="job-body">
            <h2>About this role</h2>
            <p>{{ job.description }}</p>
        </div>

        {% if user.is_authenticated %}
            {% if applied %}
                <div class="alert alert-success">You have already applied to this role.</div>
            {% else %}
                <form method="post" action="{% url 'apply-job' job.pk %}">
                    {% csrf_token %}
                    <button class="button primary" type="submit">Apply Now</button>
                </form>
            {% endif %}
        {% else %}
            <p class="notice">Please <a href="{% url 'login' %}">log in</a> to apply for this job.</p>
        {% endif %}
    </section>
{% endblock %}
''',
    'jobs/templates/jobs/job_form.html': '''{% extends 'base.html' %}
{% block title %}{% if form.instance.pk %}Edit Job{% else %}Post Job{% endif %} | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <h1>{% if form.instance.pk %}Edit Job{% else %}Post a Job{% endif %}</h1>
        <form method="post" class="form-card">
            {% csrf_token %}
            {{ form.as_p }}
            <button class="button primary" type="submit">Save Job</button>
        </form>
    </section>
{% endblock %}
''',
    'jobs/templates/jobs/job_confirm_delete.html': '''{% extends 'base.html' %}
{% block title %}Delete Job | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <h1>Delete Job</h1>
        <p>Are you sure you want to delete the job “{{ object.title }}”?</p>
        <form method="post">
            {% csrf_token %}
            <button class="button danger" type="submit">Yes, delete</button>
            <a class="button secondary" href="{% url 'job-detail' object.pk %}">Cancel</a>
        </form>
    </section>
{% endblock %}
''',
    'jobs/templates/jobs/my_jobs_list.html': '''{% extends 'base.html' %}
{% block title %}My Jobs | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <div class="page-header">
            <div>
                <h1>My Posted Jobs</h1>
                <p>Review and manage the jobs you've posted.</p>
            </div>
            <a class="button primary" href="{% url 'job-create' %}">New Job</a>
        </div>

        {% if my_jobs %}
            <div class="grid-list">
                {% for job in my_jobs %}
                    <article class="job-card">
                        <h2><a href="{% url 'job-detail' job.pk %}">{{ job.title }}</a></h2>
                        <p class="meta">{{ job.date_posted|date:'M d, Y' }}</p>
                        <p>{{ job.description|truncatechars:140 }}</p>
                        <div class="card-bottom">
                            <a class="button secondary" href="{% url 'job-update' job.pk %}">Edit</a>
                            <a class="button danger" href="{% url 'job-delete' job.pk %}">Delete</a>
                        </div>
                    </article>
                {% endfor %}
            </div>
        {% else %}
            <p>You haven't posted any jobs yet.</p>
        {% endif %}
    </section>
{% endblock %}
''',
    'jobs/templates/jobs/my_applications_list.html': '''{% extends 'base.html' %}
{% block title %}My Applications | JobPortal{% endblock %}
{% block content %}
    <section class="page-card">
        <div class="page-header">
            <div>
                <h1>My Applications</h1>
                <p>Track the jobs you've applied to and their status.</p>
            </div>
        </div>

        {% if my_applications %}
            <div class="grid-list">
                {% for application in my_applications %}
                    <article class="job-card">
                        <h2><a href="{% url 'job-detail' application.job.pk %}">{{ application.job.title }}</a></h2>
                        <p class="meta">Applied on {{ application.date_applied|date:'M d, Y' }}</p>
                        <p>{{ application.job.description|truncatechars:140 }}</p>
                    </article>
                {% endfor %}
            </div>
        {% else %}
            <p>You have not applied to any jobs yet.</p>
        {% endif %}
    </section>
{% endblock %}
''',
    'accounts/static/css/style.css': ''':root {
    color-scheme: dark;
    --bg: #0f172a;
    --surface: #111827;
    --surface-2: #1f2937;
    --text: #e2e8f0;
    --muted: #94a3b8;
    --primary: #47b5ff;
    --danger: #f87171;
    --radius: 18px;
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    min-height: 100%;
    background: radial-gradient(circle at top, rgba(71, 181, 255, 0.14), transparent 28%),
                linear-gradient(180deg, #020617 0%, #0b1226 100%);
    color: var(--text);
}

body {
    line-height: 1.6;
}

a {
    color: var(--primary);
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

.container {
    width: min(1120px, calc(100% - 2rem));
    margin: 0 auto;
    padding: 1rem 0;
}

.site-header {
    background: rgba(15, 23, 42, 0.95);
    border-bottom: 1px solid rgba(148, 163, 184, 0.1);
    backdrop-filter: blur(10px);
    position: sticky;
    top: 0;
    z-index: 50;
}

.header-bar {
    display: flex;
    gap: 1rem;
    align-items: center;
    justify-content: space-between;
}

.brand {
    font-weight: 700;
    font-size: 1.4rem;
    letter-spacing: -0.05em;
}

nav {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.user-links {
    display: flex;
    gap: 0.75rem;
    align-items: center;
}

.user-label {
    color: var(--muted);
    font-size: 0.95rem;
}

.button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border: 1px solid transparent;
    border-radius: 999px;
    padding: 0.8rem 1.2rem;
    font-weight: 600;
    transition: transform 0.2s ease, background-color 0.2s ease, border-color 0.2s ease;
    cursor: pointer;
}

.button:hover {
    transform: translateY(-1px);
}

.button.primary {
    background: var(--primary);
    color: #0b1120;
}

.button.secondary {
    background: rgba(255,255,255,0.05);
    color: var(--text);
    border-color: rgba(148,163,184,0.16);
}

.button.danger {
    background: var(--danger);
    color: #111827;
}

.hero {
    display: grid;
    gap: 2rem;
    grid-template-columns: 1.2fr 0.8fr;
    align-items: center;
    padding: 3rem 0;
}

.hero-copy h1,
.page-card h1,
.job-card h2 {
    margin: 0 0 1rem;
    font-size: clamp(2rem, 3vw, 3rem);
}

.hero-copy p,
.page-card p,
.job-card p,
.form-footer {
    color: var(--muted);
    margin: 0 0 1.25rem;
}

.hero-actions {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.feature-card {
    background: linear-gradient(180deg, rgba(71,181,255,0.14), rgba(255,255,255,0.04));
    border: 1px solid rgba(148,163,184,0.12);
    border-radius: var(--radius);
    padding: 2rem;
}

.site-footer {
    border-top: 1px solid rgba(148,163,184,0.1);
    padding: 2rem 0 3rem;
    text-align: center;
    color: var(--muted);
}

.page-card {
    background: rgba(15, 23, 42, 0.95);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: var(--radius);
    padding: 2rem;
    margin: 2rem 0;
}

.page-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.form-card {
    display: grid;
    gap: 1rem;
}

.form-card p {
    margin: 0;
}

.form-card input[type='text'],
.form-card input[type='email'],
.form-card input[type='password'],
.form-card input[type='number'],
.form-card textarea,
.form-card select {
    width: 100%;
    padding: 0.95rem 1rem;
    border-radius: 14px;
    border: 1px solid rgba(148,163,184,0.16);
    background: rgba(15,23,42,0.9);
    color: var(--text);
}

.form-card textarea {
    min-height: 150px;
    resize: vertical;
}

.grid-list {
    display: grid;
    gap: 1.5rem;
}

.job-card {
    background: rgba(15, 23, 42, 0.9);
    border: 1px solid rgba(148, 163, 184, 0.12);
    border-radius: 20px;
    padding: 1.5rem;
}

.job-card h2 {
    margin-bottom: 0.5rem;
    font-size: 1.45rem;
}

.job-card .meta,
.job-body .meta {
    color: var(--muted);
    font-size: 0.95rem;
    margin-bottom: 1rem;
}

.card-bottom {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    margin-top: 1.5rem;
    flex-wrap: wrap;
}

.badge {
    background: rgba(71, 181, 255, 0.14);
    color: var(--primary);
    border-radius: 999px;
    padding: 0.6rem 0.9rem;
    font-weight: 700;
}

.detail-actions {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
    align-items: center;
}

.alert {
    border-radius: 16px;
    padding: 1rem 1.2rem;
    margin-bottom: 1.5rem;
}

.alert-success {
    background: rgba(34,197,94,0.12);
    border: 1px solid rgba(34,197,94,0.25);
    color: #d1fae5;
}

.alert-danger {
    background: rgba(248,113,113,0.12);
    border: 1px solid rgba(248,113,113,0.25);
    color: #fee2e2;
}

.notice {
    color: var(--muted);
}

.pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin-top: 2rem;
    flex-wrap: wrap;
}

.form-footer {
    color: var(--muted);
    margin-top: 1rem;
}

@media (max-width: 860px) {
    .hero {
        grid-template-columns: 1fr;
    }
    .page-header,
    .header-bar {
        flex-direction: column;
        align-items: stretch;
    }
    nav {
        justify-content: center;
    }
}
'''
}

for path_str, content in files.items():
    path = base / path_str
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')

print(f"Written {len(files)} files to {base}")
