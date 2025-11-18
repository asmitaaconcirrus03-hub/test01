def generate_submission_blocked_email(user_name, submission_id, reason, blocker_name, unblock_request_url):
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
    email_body = submission_blocked_email_template.replace("{{ user_name }}", user_name)
    email_body = email_body.replace("{{ submission_id }}", submission_id)
    email_body = email_body.replace("{{ reason }}", reason)
    email_body = email_body.replace("{{ blocker_name }}", blocker_name)
    email_body = email_body.replace("{{ unblock_request_url }}", unblock_request_url)
    return email_body

# Example usage
if __name__ == '__main__':
    user_name = "John Doe"
    submission_id = "12345"
    reason = "Inappropriate content"
    blocker_name = "Jane Smith"
    unblock_request_url = "https://example.com/unblock/12345"

    email = generate_submission_blocked_email(user_name, submission_id, reason, blocker_name, unblock_request_url)
    print(email)
