initial_string = 'EhbiTRTadaridak8IVP5UKxw2s0DS1OXP87CsELsCC0nesibiricusPnH75jFCAog7dMYH1oI9p4Z7JMWvEsqiSXD73AVVvtOrSmb9W7jGLtGjXulJxxa8o5n4eobYFEOVB5TRXZUspStbgbv3GIA0gHwSk6k8TIWzKeUwxWYaEncNknHrX3sQWXA7t.'
a = 6
b = 13
c = 45
d = 53
final_string = ''

for n in range(a, b+1):
    final_string += initial_string[n]

final_string += ' '

for n in range(c, d+1):
    final_string += initial_string[n]

print(final_string)
