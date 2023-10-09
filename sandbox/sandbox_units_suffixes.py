from latex2sympy.latex2sympy import process_sympy
from sympy import srepr, latex


suffix_examples = [
    # '-15.11',
    # ';',
    # ')',
    # '\\: ',
    '\\%',
    # '\\%\\: \\: \\: \\: \\: \\left(10\\%\\: tolerance\\right)',
    # '\\%\\: \\: \\: \\left(10\\%\\: tolerance\\right)',
    # '\\%\\: \\: \\left(10\\%\\: tolerance\\right)',
    # '\\%\\: \\left(10\\%\\: tolerance\\right)',
    '\\$',
    '\\$/unit',
    '\\$\\: per\\: unit',
    'cost\\: per\\: servable\\: pound\\: \\left(EP\\right)',  # '\\cos t\\: per\\: servable\\: pound\\: \\left(EP\\right)',
    '\\degree ',
    '\\degree \\: C',
    '\\degree C',
    '\\degree C\\: ',
    '\\degree C\\/W',
    '\\degree s',
    '\\frac{\\degree C}{W}',
    '\\frac{\\mu g}{m^{3}}',
    '\\frac{kg}{m^{3}}',  # '\\frac{\\operatorname{kg}}{m^{3}}',
    '\\frac{kg}{s}',  # '\\frac{\\operatorname{kg}}{s}',
    '\\frac{kg\\: m}{s}',  # '\\frac{\\operatorname{kg}m}{s}',
    '\\frac{km}{hr}',  # '\\frac{\\operatorname{km}}{hr}',
    '\\frac{1}{\\degree C}',
    '\\frac{1}{m}',
    '\\frac{1}{s}',
    '\\frac{A}{\\mu s}',
    '\\frac{dB}{decade}',
    '\\frac{dB}{octave}',
    '\\frac{ft}{^{\\prime }s}',
    '\\frac{ft}{s}',
    '\\frac{ft^{3}}{s}',
    '\\frac{g}{mol}',
    '\\frac{Gs}{A}',
    # '\\frac{J}{\\operatorname{kg}K}',
    '\\frac{J}{kg\\: K}',
    '\\frac{kJ}{mol}',
    '\\frac{L_{1}}{R_{total}}',
    '\\frac{L_{2}}{R_{total}}',
    '\\frac{lbf}{ft^{2}}',
    '\\frac{m}{s}',
    '\\frac{m}{s^{^{2}}}',
    '\\frac{m}{s^{2}}',
    '\\frac{m^{3}}{s}',
    '\\frac{mR}{hr}',
    '\\frac{mV}{\\mu s}',
    '\\frac{N}{m}',
    '\\frac{N}{m^{2}}',
    '\\frac{R}{hr}',
    '\\frac{Rad}{s}',
    '\\frac{rad}{sec}',
    '\\frac{T}{A}',
    '\\frac{V}{\\mu s}',
    '\\frac{V}{m}',
    '\\left(\\frac{W}{m^{2}}\\right)',
    'min',  # '\\min ',
    '\\mu A',
    '\\mu C',
    '\\mu F',
    '\\mu g',
    '\\mu H',
    '\\mu s',
    '\\mu V',
    '\\Omega ',
    # '\\Omega \\: \\left(round\\: to\\: 3\\: decimals\\right)',
    'cm',  # '\\operatorname{cm}',
    'kg',  # '\\operatorname{kg}',
    'kg\\cdot m',  # '\\operatorname{kg}\\cdot m',
    'kg\\cdot m^{2}',  # '\\operatorname{kg}\\cdot m^{2}',
    'kg\\: m^{2}',  # '\\operatorname{kg}m^{2}',
    'mm^{2}',  # '\\operatorname{mm}^{2}',
    '\\pi \\: bonds',
    '\\pm \\: s_{a}\\: \\: \\: \\frac{m}{s^{2}}',
    '\\pm s_{a}\\: \\: \\frac{m}{s^{2}}',
    '\\pm s_{x}\\: m',
    'sec',  # '\\sec ',
    # '\\text{m s}^{-1}',
    # '℃',
    # '°C\\: ',
    # '+\\: f\\mleft(x,y\\mright)\\text{ ; where f is a general function of x and y}',
    # '1',
    '1/hr',
    '10^{-6}\\: \\frac{m^{2}}{s}',
    'A',
    'A\\: peak',
    'ADC',
    'Amps',
    'amu',
    'Ap',
    'apartments',
    'atm',
    'atoms',
    'bottles',
    'boxes',
    'C',
    'cans',
    'carbon\\: atoms',
    'cases',
    'cfm',
    'cfs',
    'cm',
    'Coulumbs',
    'cubic\\: inches',
    'customers\\: will\\: order\\: asparagus',
    'customers\\: will\\: order\\: fresh\\: fruit',
    'customers\\: will\\: order\\: lemon-pepper\\: chicken',
    'days',
    'dB',
    'dBV',
    'deg',
    'deg\\: \\frac{C}{W}',
    'deg\\: C',
    'degC',
    'degC/W',
    'Degrees',
    'degrees\\: Celsius',
    'dollar',
    'dollars',
    'E-9',
    'E3',
    'electrons',
    'eV',
    'F',
    'Farads',
    'fF',
    'ft',
    'ft.lbf',
    'ft/(cfm)^{2}',
    'ft/s',
    'ft^{3}/s',
    'ft3/s',
    'g',
    'g/mol',
    'giga',
    'gpm',
    'grams',
    'Gs',
    'H',
    # 'H\\: \\: \\: \\: \\: \\left(copy\\: from\\: Activity\\: 1\\right)',
    # 'H\\: \\left(copy\\: from\\: Activity\\: 1\\right)',
    'hours',
    'Hp',
    'hr^{-1}',
    'hrs',
    'hydrogen\\: atoms',
    'Hz',
    # 'Hz\\: \\left(10\\%\\: tolerance\\: for\\: this\\: answer\\right)',
    'in',
    'in.\\: of\\: water\\: \\left(gage\\right)',
    'in^{2}',
    'in^{3}',
    'individuals',
    'J',
    'K',
    'k\\Omega ',
    # 'k\\Omega ,\\: tolerance\\: \\pm 5\\%',
    'kcal',
    'kg',
    'kg/kmole',
    'kHz',
    'kibit',
    'kJ',
    'kJ/mol',
    'kN',
    'kN.m',
    'kN/m',
    'knot',
    'kohms',
    'KPa',
    'kPa\\: \\left(abs\\right)',
    'kPa\\: \\left(gage\\right)',
    'ks',
    'kW',
    # 'kΩ',
    'L',
    'L/day',
    'L/hr',
    'lb',
    'lb/ft2',
    'lb\\: AP',
    'lbf',
    'lbf-in',
    'lbf.ft',
    'lbs',
    'lone\\: pairs',
    'm',
    'm/s',
    'm/s^{2}',
    'M\\: \\: K_{2}SO_{4}',
    'M\\: potassium\\: sulfate',
    'M\\Omega ',
    'm^{2}',
    'm^{2}/s^{2}',
    'm^{3}',
    'm^{3}/s',
    'm3/s',
    'mA',
    'mb',
    'mcg',
    'mCi',
    'Megajoules',
    'meters\\: per\\: second',
    'meters\\: per\\: second\\: squared',
    'MeV/nucleon',
    'mg',
    'mg/hr',
    'mH',
    'MHz',
    'mile\\left(s\\right)\\: per\\: hour',
    'miles\\: per\\: hour',
    'Millivolts',
    'mL',
    'mL/day',
    'mL/hr',
    'mm',
    'MN',
    'Mohms',
    'moles',
    'mph',
    'ms',
    'msec',
    'mV',
    'mV_{p}',
    'mV_{RMS}',
    'mW',
    'N',
    'N/m^{2}',
    # 'N\\: \\left(negative\\right)',
    'N\\: s\\: /\\: m^{2}',
    'N\\cdot m',
    'N\\cdot m^{2}',
    'neutrons',
    'nF',
    'nL',
    'nm',
    'nm^{-1}',
    'o',
    # 'º',
    'ohms',
    'on\\: eggplants\\: and\\: kiwis',
    'Pa',
    'pebibit',
    'per\\: 4\\: oz\\: serving',
    'per\\: fl\\: oz',
    'per\\: unit',
    'percent',
    'pF',
    'photons',
    'pico',
    'Pokeballs\\: with\\: her\\: income',
    'polar\\: molecules',
    'pounds',
    'PPS',
    'psi',
    'psia',
    'rad/s',
    'rad/sec',
    'rad\\: /\\: sec',
    'ratio',
    'represents\\: the\\: new\\: cost\\: curve',  # 'represents\\: the\\: new\\: \\cos t\\: curve',
    'represents\\: the\\: new\\: ATC\\: curve',
    'rooms',
    'rpm',
    's',
    's^{-1}',
    'sec',
    'Seconds',
    'SI\\: units',
    'slugs/ft3',
    'square\\: inches',
    'svgs',
    'T',
    'tablets',
    'uA',
    'uF',
    'ug',
    'uH',
    'units',
    'uS',
    'V',
    'V_{DC}',
    'V_{p}',
    'V_{pp}',
    'V_{RMS}',
    'V/us',
    # 'V\\: \\left(5\\%\\: tolerance\\right)',
    'V\\: to\\: 0V',
    'V\\cdot m',
    'Vmin',  # 'V\\min ',
    'valence\\: electrons',
    'Vdc',
    'Volts',
    'Vp',
    'Vpeak',
    'Vpp',
    'Vrms',
    'Vs',
    'W',
    'Watts',
    'year\\left(s\\right)\\: of\\: her\\: life\\: due\\: to\\: bickering',
    'years',
    'years\\: ',
    'yrs',
    # 'Ω',
]

for suffix in suffix_examples:
    try:
        suffix_as_unit = process_sympy(suffix, parse_as_unit=True)
        print('suffix:', suffix, ', sympy =>', suffix_as_unit)  # ', srepr =>', srepr(suffix_as_unit))
    except Exception as e:
        print('suffix:', suffix, '=>', e)
    print('------------------------------------------------------------------')