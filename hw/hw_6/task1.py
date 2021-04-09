coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

# new_dict = dict(zip(coin, code))

new_dict = {}

for k, v in zip(coin, code):
    new_dict[k] = v

print(new_dict)
