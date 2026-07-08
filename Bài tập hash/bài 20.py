def compare_prime_buckets(keys):
    m_power = [0] * 16
    m_prime = [0] * 17
    for k in keys:
        m_power[k % 16] += 1
        m_prime[k % 17] += 1
    return m_power, m_prime