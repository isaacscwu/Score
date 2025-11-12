scores = list(map(int, input().split()))
average=sum(scores)/len(scores)
print(average)

fail_count = sum(1 for s in scores if s < 60)
max_score = max(scores)
min_score = min(scores)

print(fail_count)
print(max_score, min_score)
