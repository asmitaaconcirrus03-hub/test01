unblock_request_email_template = '''
Subject: Unblock Request for Submission ID: {{ submission_id }}

Dear {{ user_name }},

A request has been made to unblock Submission ID: {{ submission_id }}.

Requester: {{ requester_name }}
Reason: {{ reason }}

You can review the submission here: {{ submission_url }}

Thanks,
The System
'''

submission_blocked_email_template = '''
Subject: Submission Blocked: {{ submission_id }}

Dear {{ user_name }},

Your submission with ID: {{ submission_id }} has been blocked.

Reason: {{ reason }}
Blocked by: {{ blocker_name }}

If you believe this was a mistake, you can request an unblock here: {{ unblock_request_url }}

Thanks,
The System
'''
