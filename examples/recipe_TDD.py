# Capocollo Recipe
#
# C 2021 Stoyanov
#
# 1000 g Pork neck
# 15 g Sea salt
# 10 g Nitrite salt
# 5 g Sugar
# 2 days per 500 g


def nitro_salt(m):
    # 1000/10 = m/x
    try:
        m = int(m)
    except:
        m = 0
    return int(10 * m / 1000)
