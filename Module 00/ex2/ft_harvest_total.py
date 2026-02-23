# ************************************************************************* #
#                                                                           #
#                                                         :::      :::::::: #
#    ft_harvest_total.py                                :+:      :+:    :+: #
#                                                     +:+ +:+         +:+   #
#    By: bpavlows <bpavlows@student.42porto.com>    +#+  +:+       +#+      #
#                                                 +#+#+#+#+#+   +#+         #
#    Created: 2026/02/21 10:57:42 by bpavlows          #+#    #+#           #
#    Updated: 2026/02/21 11:01:15 by bpavlows         ###   ########.fr     #
#                                                                           #
# ************************************************************************* #

def ft_harvest_total():
    day1 = int(input('Day 1 harvest: '))
    day2 = int(input('Day 2 harvest: '))
    day3 = int(input('Day 3 harvest: '))
    total = day1 + day2 + day3
    print(f"Total harvest: {total}")
