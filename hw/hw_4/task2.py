count, sum_num, avg, max_num, second_max_num, max_num_indx, coun_chet, count_nechet, coun_max = 0, 0, 0, 0, 0, 0, 0, 0, 0
comp = 1

while True:
    n = int(input())
    if n == max_num:
        coun_max += 1

    if n == 0:
        break
    elif n != 0:
        count += 1
        sum_num += n
        comp *= n
        avg = sum_num / count

        if n >= max_num:
            second_max_num = max_num
            max_num = n
            max_num_indx = count
        if second_max_num < n < max_num:
            second_max_num = n

        if n % 2 == 0:
            coun_chet += 1
        if n % 2 != 0:
            count_nechet += 1


print("Count: %d" % count)
print("Sum all numbs: %d" % sum_num)
print("Composition: %d" % comp)
print("AVG: %d" % round(avg, 2))
print("MAX numbr + indx = [", max_num_indx, "]", max_num, sep='')
print("Second MAX: %d" % second_max_num)
print("Even -", coun_chet, "NotEven -", count_nechet)
print("Meat MAX times: %d" % coun_max)
