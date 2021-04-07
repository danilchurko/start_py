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
        else:
            count_nechet += 1


print('Count: {}'.format(count))
print('Sum all numbs: {}'.format(sum_num))
print('Composition: {}'.format(comp))
print('AVG: {:.2f}'.format(avg))
print('MAX numbr + indx = [{}] {}'.format(max_num_indx, max_num))
print('Second MAX: {}'.format(second_max_num))
print('Even - {} | NotEven - {}'.format(coun_chet, count_nechet))
print('Meat MAX times: {}'.format(coun_max))
