from generate_email import generate_submission_blocked_email

def test_generate_submission_blocked_email():
    user_name = "John Doe"
    submission_id = "12345"
    reason = "Inappropriate content"
    blocker_name = "Jane Smith"
    unblock_request_url = "https://example.com/unblock/12345"

    expected_email = '''Subject: Submission Blocked: 12345

Dear John Doe,

Your submission with ID: 12345 has been blocked.

Reason: Inappropriate content
Blocked by: Jane Smith

If you believe this was a mistake, you can request an unblock here: https://example.com/unblock/12345

Thanks,
The System
'''

    actual_email = generate_submission_blocked_email(user_name, submission_id, reason, blocker_name, unblock_request_url)
    assert actual_email == expected_email

test_generate_submission_blocked_email()
