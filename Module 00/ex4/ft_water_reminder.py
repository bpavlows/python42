# ************************************************************************* #
#                                                                           #
#                                                         :::      :::::::: #
#    ft_water_reminder.py                               :+:      :+:    :+: #
#                                                     +:+ +:+         +:+   #
#    By: bpavlows <bpavlows@student.42porto.com>    +#+  +:+       +#+      #
#                                                 +#+#+#+#+#+   +#+         #
#    Created: 2026/02/21 11:19:54 by bpavlows          #+#    #+#           #
#    Updated: 2026/02/21 11:22:46 by bpavlows         ###   ########.fr     #
#                                                                           #
# ************************************************************************* #

def ft_water_reminder():
    day = int(input('Days since last watering: '))
    if (day > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
