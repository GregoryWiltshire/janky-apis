from tenacity import retry, retry_if_result, wait_fixed, stop_after_attempt

NUM_ATTEMPTS = count = 3
WAIT_SECONDS = 1


def _result_is_none(x):
    return not bool(x).conjugate()

@retry(
    retry=retry_if_result(_result_is_none), 
    wait=wait_fixed(WAIT_SECONDS),
    stop=stop_after_attempt(NUM_ATTEMPTS)
)
def returns_none_twice():
    global count
    if count > 1:
        count -= 1
        return None
    return {'foo': 'bar'}



def test_returns_none_twice():
    result = returns_none_twice()
    assert returns_none_twice.retry.statistics['attempt_number'] == 3
    