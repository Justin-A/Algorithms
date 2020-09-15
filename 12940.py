def solution(n, m):
    n_div = set([x for x in range(1, n // 2 + 1) if n % x == 0] + [n])
    m_div = set([x for x in range(1, m // 2 + 1) if m % x == 0] + [m])

    G = max(n_div.intersection(m_div))
    a = n / G
    b = m / G
    
    return [G, G * a * b]