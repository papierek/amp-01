
# coding: utf-8

# In[2]:

#amp params
speakers_impedance = 8 #ohms
target_output_power = 40 # wats

#LM3886 - consult with datasheet
amp_voltage_drop = 4
max_supply_voltage_pp = 84 #V |Vcc|+|Vee|
safety_margin = 0.90 # 10 %
passive_current = 0.085 # A

#trafo regulation
variation_in_main = 1.1
trafo_regulation = 1.06
trafo_v_rms_out = 24
trafo_v_peak_out = trafo_v_rms_out * 1.41 #V

import math
v_pk_output = math.sqrt(2*speakers_impedance*target_output_power)
print("Maximum output signal voltage:\t{0:.2f}V".format(v_pk_output))
required_voltage = (v_pk_output + amp_voltage_drop) * trafo_regulation * 1.1

print("Required supply voltage:\t{0:.2f}V".format(required_voltage))
print("Trafo output peak voltage:\t{0:.2f}V".format(trafo_v_peak_out))

max_supply_voltage =(max_supply_voltage_pp/2) * safety_margin

print("Max allowed supply voltage:\t{0:.2f}V".format(max_supply_voltage))
if(max_supply_voltage < trafo_v_peak_out):
    print("Trafo output voltage is to big!")


v = (trafo_v_peak_out/(trafo_regulation * variation_in_main) - amp_voltage_drop)
print("\n",v)
actual_power = (v*v)/speakers_impedance/2

print("\nMax output power (Rout={0}ohms):\t{1:.0f}W".format(speakers_impedance, actual_power))

# Required trafo power cacilation

out_current_load_max = v_pk_output/3.14/speakers_impedance
out_current_total = passive_current + out_current_load_max

p_supply = 2*trafo_v_peak_out * out_current_total

print("Required power per channel:\t{:.2f}W".format(p_supply))
p_sup_marg = p_supply*1.5
print(" --- with margin:\t{:.2f}W".format(p_sup_marg))
va_ratings = p_sup_marg*2
print(" --- total:\t\t{:.2f}W".format(va_ratings))

print("\n### TRAFO PARMAS ###")
print("Out voltage:\t2*{0:.2f}\nVA rating:\t{1:.2f}".format(trafo_v_rms_out, va_ratings))


# In[7]:

i_vol_rms = 0.316#V
i_vol_a = 1.41 * 0.316
v_in_max = 2*i_vol_a

print(i_vol_rms,i_vol_a, i_vol_pp)

v_out_max = math.sqrt(actual_power * speakers_impedance)
print(v_out_max)

min_gain = v_out_max/v_in_max

print("Minimum gain required: {0:.2f}".format(min_gain))
