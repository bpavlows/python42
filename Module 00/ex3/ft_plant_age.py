# ************************************************************************* #
#                                                                           #
#                                                         :::      :::::::: #
#    ft_plant_age.py                                    :+:      :+:    :+: #
#                                                     +:+ +:+         +:+   #
#    By: bpavlows <bpavlows@student.42porto.com>    +#+  +:+       +#+      #
#                                                 +#+#+#+#+#+   +#+         #
#    Created: 2026/02/21 11:12:05 by bpavlows          #+#    #+#           #
#    Updated: 2026/02/21 11:18:56 by bpavlows         ###   ########.fr     #
#                                                                           #
# ************************************************************************* #

def ft_plant_age():
    day = int(input('Enter plant age in days: '))
    if (day > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
