def stock_span(prices):
    stack = []
    spans = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] <= price:
            stack.pop()
        span = i + 1 if not stack else i - stack[-1]
        spans.append(span)
        stack.append(i)
    return spans