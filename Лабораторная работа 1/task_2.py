# TODO Найдите количество книг, которое можно разместить на дискете
info_V_disket = 1.44 * 1024 * 1024
kolvo_pages = 100
kolvo_strok = 50
kolvo_simv = 25
simv = 4
kniga = simv * kolvo_simv * kolvo_strok * kolvo_pages
vsego = int(info_V_disket // kniga)
print("Количество книг, помещающихся на дискету:", vsego)