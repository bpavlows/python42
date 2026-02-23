# ************************************************************************* #
#                                                                           #
#                                                         :::      :::::::: #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+: #
#                                                     +:+ +:+         +:+   #
#    By: bpavlows <bpavlows@student.42porto.com>    +#+  +:+       +#+      #
#                                                 +#+#+#+#+#+   +#+         #
#    Created: 2026/02/21 11:23:20 by bpavlows          #+#    #+#           #
#    Updated: 2026/02/21 11:48:14 by bpavlows         ###   ########.fr     #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_iterative():
    day = int(input('Days until harvest: '))
    cont = 1
    while (cont <= day):
        print(f"Day {cont}")
        cont += 1
    print("Harvest time!")
