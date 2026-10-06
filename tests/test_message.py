# test_message.py
import pytest
from message import Message

# Fixture to reuse a test Message instance
@pytest.fixture
def sample_message():
    return Message(
        sender="test@example.com",
        subject="Test Subject",
        recipient="recipient@example.com",
        message="Test content",
        priority=3
    )

# 1. Test initialization
def test_message_initialization(sample_message):
    assert sample_message.sender == "test@example.com"
    assert sample_message.subject == "Test Subject"
    assert sample_message.priority == 3
    assert sample_message.label == ""  # Default value

# 2. Test stars() method
def test_stars(sample_message):
    assert sample_message.stars() == "***"  # Priority 3 → 3 stars
    sample_message.priority = 5
    assert sample_message.stars() == "*****"

# 3. Test info() method formatting
def test_info_format(sample_message):
    expected_output = "***      test@example.com                Test Subject"  # Added extra space
    assert sample_message.info() == expected_output

# 4. Test edge cases
def test_default_priority():
    msg = Message("a", "b", "c", "d")  # No priority specified
    assert msg.priority == 0
    assert msg.stars() == ""  # 0 stars → empty string

# 5. Test label assignment
def test_label_assignment(sample_message):
    sample_message.label = "Important"
    assert "Important" in sample_message.info()



# 6. Test new_message() function in message_manager
def test_new_message():
    import message_manager as msg_mgr

    original_count = len(msg_mgr.messages)

    msg_mgr.new_message(
        "sender@example.com",
        "recipient@example.com",
        "Test Subject",
        "Test content"
    )

    assert len(msg_mgr.messages) == original_count + 1

    new_id = max(msg_mgr.messages.keys())
    new_message = msg_mgr.messages[new_id]

    assert new_message.sender == "sender@example.com"
    assert new_message.recipient == "recipient@example.com"
    assert new_message.subject == "Test Subject"
    assert new_message.content == "Test content"
    assert new_message.priority == 0
