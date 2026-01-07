def juft_topish(royxat):
    return [x for x in royxat if x % 2 == 0]

def toq_topish(royxat):
    return [x for x in royxat if x % 2 !=0]

def musbot_topish(royxat):
    return [x for x in royxat if x > 0]


from royxat import juft_topish, toq_topish, musbot_topish

royxat = [12, -5, 8, -3, 15, 20, -7]

print("juft", juft_topish(royxat))
print("toq", toq_topish(royxat))
print("musbat", musbot_topish(royxat))
