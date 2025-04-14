import subprocess


def test_integration_with_real_logs(temp_log_file):
    """
    Интеграционный тест с реальными логами.
    """
    result = subprocess.run(
        ['python', 'main.py', str(temp_log_file), '--report', 'handlers'],
        capture_output=True,
        text=True
    )

    assert 'Total requests: 2' in result.stdout
    assert '/api/v1/reviews/' in result.stdout
    assert '/admin/dashboard/' in result.stdout
    assert 'INFO' in result.stdout
    assert 'ERROR' in result.stdout
