# ************************************************************************* #
#                                                                           #
#                                                         :::      :::::::: #
#    ft_plot_area.py                                    :+:      :+:    :+: #
#                                                     +:+ +:+         +:+   #
#    By: bpavlows <bpavlows@student.42porto.com>    +#+  +:+       +#+      #
#                                                 +#+#+#+#+#+   +#+         #
#    Created: 2026/02/21 10:28:30 by bpavlows          #+#    #+#           #
#    Updated: 2026/02/21 10:37:45 by bpavlows         ###   ########.fr     #
#                                                                           #
# ************************************************************************* #

def ft_plot_area():
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    area = length * width
    print(f"Plot area: {area}")
