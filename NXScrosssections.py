#Run in Python 3.12.9 with the Extensible Periodic Table repository cloned inside VSC
import periodictable
import matplotlib.pyplot as plt
import numpy as np
from periodictable import elements


ree_yttrium_data = {}
rare_earths_yttrium = ["La", "Ce", "Pr", "Nd", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Y"]
#Call on attributes from neutron scattering (.NSF) portion of the Extensible Periodic Table
#Displays total and absorption cross sections
for element in periodictable.elements:
    if element.symbol in rare_earths_yttrium:
        atomic_number = element.number
        absorption_xs = getattr(element.neutron, 'absorption', None)
        total_xs = getattr(element.neutron, 'total', None)
        ree_yttrium_data[atomic_number] = {
            'symbol': element.symbol,
            'absorption': absorption_xs,
            'total': total_xs
        }
        print (f"Element: {element.name}")
        if absorption_xs is not None:
            print(f"Absorption Cross Section: {absorption_xs} barns")
        if total_xs is not None:
            print (f"Total Scattering Section: {total_xs} barns")

#Data sorting for charts--charts have to be separated for legibility
sorted_data = dict(sorted(ree_yttrium_data.items()))
atomic_numbers = list(sorted_data.keys())
absorption_values = [data['absorption'] for data in sorted_data.values()]
total_values = [data['total'] for data in sorted_data.values()]
labels = [sorted_data[num]['symbol'] for num in atomic_numbers]

#Chart 1: Absorption Cross-Sections
fig_abs, ax_abs = plt.subplots(figsize=(12, 6))
#ax_abs.stem(atomic_numbers, absorption_values, markerfmt='skyblue')
ax_abs.scatter(atomic_numbers, absorption_values, color='tomato')
ax_abs.set_xlabel('Atomic Number')
ax_abs.set_ylabel('Absorption Cross-Section (barns)')
ax_abs.set_title('Neutron Absorption Cross-Sections for Rare Earths and Yttrium')
ax_abs.set_xticks(atomic_numbers)
ax_abs.set_xticklabels(labels)
fig_abs.tight_layout()
plt.show()

#Chart 2: Total Scattering Cross-Sections
fig_total, ax_total = plt.subplots(figsize=(12, 6))
ax_total.scatter(atomic_numbers, total_values, color='forestgreen')
ax_total.set_xlabel('Atomic Number')
ax_total.set_ylabel('Total Scattering Cross-Section (barns)')
ax_total.set_title('Neutron Total Scattering Cross-Sections for Rare Earths and Yttrium')
ax_total.set_xticks(atomic_numbers)
ax_total.set_xticklabels(labels)
fig_total.tight_layout()
plt.show()
        
print ("There are two charts. The first that appears is absorption scattering cross section; close this to see total scattering cross section.")