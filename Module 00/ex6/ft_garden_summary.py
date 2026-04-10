# ************************************************************************* #
#                                                                           #
#                                                         :::      :::::::: #
#    ft_garden_summary.py                               :+:      :+:    :+: #
#                                                     +:+ +:+         +:+   #
#    By: bpavlows <bpavlows@student.42porto.com>    +#+  +:+       +#+      #
#                                                 +#+#+#+#+#+   +#+         #
#    Created: 2026/02/23 09:23:29 by bpavlows          #+#    #+#           #
#    Updated: 2026/02/23 09:23:29 by bpavlows         ###   ########.fr     #
#                                                                           #
# ************************************************************************* #

def ft_garden_summary():
    name = input('Enter garden name: ')
    num = int(input('Enter number of plants: '))
    print(f"Garden: {name}")
    print(f"Plants: {num}")
    print("Status: Growing well!")
