def solution(ip_addrs, langs, scores):
    visited = [0]*len(ip_addrs)
    result = 0
    for i in range(len(ip_addrs)):
        ip_count = 0
        lang_count = 0
        score_count = 0
        for j in range(i+1, len(ip_addrs)):
            if not visited[j]:
                if ip_addrs[i] == ip_addrs[j]:
                    visited[j] = 1
                    ip_count += 1
                    if langs[i] == langs[j]:
                        lang_count += 1
                        if scores[i] == scores[j]:
                            score_count += 1
                    elif langs[i] in ['C', 'C++', 'C#'] and langs[j] in ['C', 'C++', 'C#']:
                        lang_count += 1
                        if scores[i] == scores[j]:
                            score_count += 1
        print(ip_count, lang_count, score_count)
        if ip_count >= 3:
            result += ip_count+1
        elif lang_count == 2:
            result += 3
        elif score_count == 1:
            result += 2
    answer = len(ip_addrs)-result
    print(answer)
    return answer


solution(["5.5.5.5", "155.123.124.111", "10.16.125.0", "155.123.124.111", "5.5.5.5", "155.123.124.111", "10.16.125.0", "10.16.125.0"], ["Java", "C++", "Python3", "C#", "Java", "C", "Python3", "JavaScript"], [294, 197, 373, 45, 294, 62, 373, 373])