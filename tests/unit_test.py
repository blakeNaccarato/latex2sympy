import pytest
from sympy import Symbol
from sympy.physics.units.prefixes import PREFIXES, BIN_PREFIXES
from sympy.physics.units.definitions.unit_definitions import (
    # MKS - "meter, kilogram, second"
    meter, gram, kilogram, second, joule, newton, watt, pascal, hertz, gravitational_constant, speed_of_light,
    # MKSA - based on MKS, "meter, kilogram, second, ampere"
    ampere, volt, ohm, siemens, farad, henry, coulomb, tesla, weber,
    # SI - based on MKSA, added kelvin, candela and mole
    mol, cd, K, lux, hertz, newton, pascal, joule, watt, coulomb, volt,
    farad, ohm, siemens, weber, tesla, henry, candela, becquerel,
    gray, katal,
    # Derived
    kilometer, centimeter, millimeter, nanometer,
    milligram, microgram,
    millisecond, microsecond,
    liter, milliliter,
    # Other
    percent,
    degree,
    rad,
    minute, hour, day, year,
    foot, inch, mile, pound,
    curie, gauss,
    atomic_mass_constant,
    atmosphere,
    electronvolt,
    bar, psi, bit
)
from latex2sympy.latex2sympy import process_sympy
from latex2sympy.units.additional_units import cal, lbf, slug, degC, degF, dB
from latex2sympy.units import create_prefixed_unit, UNIT_ALIASES
from .context import _Mul, _Pow, assert_equal, is_or_contains_instance

# create local vars for known units
millivolt = UNIT_ALIASES['millivolt']
microohm = UNIT_ALIASES['microohm']

unit_examples = [
    # si units by abbrev
    ('g', gram),
    ('kg', kilogram),
    ('A', ampere),
    # si units by name
    ('grams', gram),
    ('ampere', ampere),
    # si units by latex
    ('\\Omega', ohm),
    ('\\mu g', microgram),
    # prefixed si units
    ('mV', millivolt),
    ('millivolt', millivolt),
    ('\\mu \\Omega ', microohm),
    # compound si units
    ('kg\\times \\frac{m}{s^{2}}', _Mul(kilogram, meter, _Pow(_Pow(second, 2), -1))),
    ('kg*m^{2}s^{-3}', _Mul(kilogram, _Pow(meter, 2), _Pow(second, -3))),
    # space as multiplication
    ('kg\\: m', _Mul(kilogram, meter)),
    # only allow certain constants
    ('c', speed_of_light)
]

bad_unit_examples = [
    # custom units
    'apples',
    'apples\\times grams',
    'pen\\times pineapple\\times apple\\times pen',
    'red\\: delicious',
]

suffix_unit_examples = [
    ('\\%', percent),
    ('dB', dB),
    ('\\degree ', degree),
    ('\\degree C', degC),
    ('\\degree C\\: ', degC),
    ('\\degree C/W', _Mul(degC, _Pow(watt, -1))),
    ('\\degree F', degF),
    ('\\frac{\\degree C}{W}', _Mul(degC, _Pow(watt, -1))),
    ('\\frac{\\mu g}{m^{3}}', _Mul(microgram, _Pow(_Pow(meter, 3), -1))),
    ('\\frac{kg}{m^{3}}', _Mul(kilogram, _Pow(_Pow(meter, 3), -1))),
    ('\\frac{kg}{s}', _Mul(kilogram, _Pow(second, -1))),
    ('\\frac{kg\\: m}{s}', _Mul(_Mul(kilogram, meter), _Pow(second, -1))),
    ('\\frac{km}{hr}', _Mul(kilometer, _Pow(hour, -1))),
    ('\\frac{1}{\\degree C}', _Mul(1, _Pow(degC, -1))),
    ('\\frac{1}{m}', _Mul(1, _Pow(meter, -1))),
    ('\\frac{1}{s}', _Mul(1, _Pow(second, -1))),
    ('\\frac{A}{\\mu s}', _Mul(ampere, _Pow(microsecond, -1))),
    ('\\frac{ft}{s}', _Mul(foot, _Pow(second, -1))),
    ('\\frac{ft^{3}}{s}', _Mul(_Pow(foot, 3), _Pow(second, -1))),
    ('\\frac{g}{mol}', _Mul(gram, _Pow(mol, -1))),
    ('\\frac{J}{kg\\: K}', _Mul(joule, _Pow(_Mul(kilogram, K), -1))),
    ('\\frac{kJ}{mol}', _Mul(create_prefixed_unit(joule, PREFIXES['k']), _Pow(mol, -1))),
    ('\\frac{lbf}{ft^{2}}', _Mul(lbf, _Pow(_Pow(foot, 2), -1))),
    ('\\frac{m}{s}', _Mul(meter, _Pow(second, -1))),
    ('\\frac{m}{s^{2}}', _Mul(meter, _Pow(_Pow(second, 2), -1))),
    ('\\frac{m^{3}}{s}', _Mul(_Pow(meter, 3), _Pow(second, -1))),
    ('\\frac{mV}{\\mu s}', _Mul(create_prefixed_unit(volt, PREFIXES['m']), _Pow(microsecond, -1))),
    ('\\frac{N}{m}', _Mul(newton, _Pow(meter, -1))),
    ('\\frac{N}{m^{2}}', _Mul(newton, _Pow(_Pow(meter, 2), -1))),
    ('\\frac{rad}{sec}', _Mul(rad, _Pow(second, -1))),
    ('\\frac{T}{A}', _Mul(tesla, _Pow(ampere, -1))),
    ('\\frac{V}{\\mu s}', _Mul(volt, _Pow(microsecond, -1))),
    ('\\frac{V}{m}', _Mul(volt, _Pow(meter, -1))),
    ('\\left(\\frac{W}{m^{2}}\\right)', _Mul(watt, _Pow(_Pow(meter, 2), -1))),
    ('min', minute),
    ('\\mu A', create_prefixed_unit(ampere, PREFIXES['mu'])),
    ('\\mu C', create_prefixed_unit(coulomb, PREFIXES['mu'])),
    ('\\mu F', create_prefixed_unit(farad, PREFIXES['mu'])),
    ('\\mu g', microgram),
    ('\\mu H', create_prefixed_unit(henry, PREFIXES['mu'])),
    ('\\mu s', microsecond),
    ('\\mu V', create_prefixed_unit(volt, PREFIXES['mu'])),
    ('\\Omega ', ohm),
    ('cm', centimeter),
    ('kg', kilogram),
    ('kg\\cdot m', _Mul(kilogram, meter)),
    ('kg\\cdot m^{2}', _Mul(kilogram, _Pow(meter, 2))),
    ('kg\\: m^{2}', _Mul(kilogram, _Pow(meter, 2))),
    ('mm^{2}', _Pow(millimeter, 2)),
    ('sec', second),
    ('1/hr', _Mul(1, _Pow(hour, -1))),
    ('A', ampere),
    ('Amps', ampere),
    ('amu', atomic_mass_constant),
    ('atm', atmosphere),
    ('C', coulomb),
    ('cm', centimeter),
    ('days', day),
    ('deg', degree),
    ('degC', degC),
    ('degC/W', _Mul(degC, _Pow(watt, -1))),
    ('Degrees', degree),
    ('eV', electronvolt),
    ('F', farad),
    ('Farads', farad),
    ('fF', create_prefixed_unit(farad, PREFIXES['f'])),
    ('ft', foot),
    ('ft/s', _Mul(foot, _Pow(second, -1))),
    ('ft^{3}/s', _Mul(_Pow(foot, 3), _Pow(second, -1))),
    ('ft3/s', _Mul(_Mul(foot, 3), _Pow(second, -1))),
    ('g', gram),
    ('g/mol', _Mul(gram, _Pow(mol, -1))),
    ('grams', gram),
    ('Gs', create_prefixed_unit(second, PREFIXES['G'])),
    ('H', henry),
    ('hours', hour),
    ('hr^{-1}', _Pow(hour, -1)),
    ('hrs', hour),
    ('Hz', hertz),
    ('in', inch),
    ('in^{2}', _Pow(inch, 2)),
    ('in^{3}', _Pow(inch, 3)),
    ('J', joule),
    ('K', K),
    ('k\\Omega ', create_prefixed_unit(ohm, PREFIXES['k'])),
    ('kcal', create_prefixed_unit(cal, PREFIXES['k'])),
    ('kg', kilogram),
    ('kHz', create_prefixed_unit(hertz, PREFIXES['k'])),
    ('kJ', create_prefixed_unit(joule, PREFIXES['k'])),
    ('kJ/mol', _Mul(create_prefixed_unit(joule, PREFIXES['k']), _Pow(mol, -1))),
    ('kN', create_prefixed_unit(newton, PREFIXES['k'])),
    ('kN/m', _Mul(create_prefixed_unit(newton, PREFIXES['k']), _Pow(meter, -1))),
    ('kPa', create_prefixed_unit(pascal, PREFIXES['k'])),
    ('ks', create_prefixed_unit(second, PREFIXES['k'])),
    ('kW', create_prefixed_unit(watt, PREFIXES['k'])),
    ('L', liter),
    ('L/day', _Mul(liter, _Pow(day, -1))),
    ('L/hr', _Mul(liter, _Pow(hour, -1))),
    ('lb', pound),
    ('lb/ft2', _Mul(pound, _Pow(_Mul(foot, 2), -1))),
    ('lbf', lbf),
    ('lbs', pound),
    ('m', meter),
    ('m/s', _Mul(meter, _Pow(second, -1))),
    ('m/s^{2}', _Mul(meter, _Pow(_Pow(second, 2), -1))),
    ('M\\Omega ', create_prefixed_unit(ohm, PREFIXES['M'])),
    ('m^{2}', _Pow(meter, 2)),
    ('m^{2}/s^{2}', _Mul(_Pow(meter, 2), _Pow(_Pow(second, 2), -1))),
    ('m^{3}', _Pow(meter, 3)),
    ('m^{3}/s', _Mul(_Pow(meter, 3), _Pow(second, -1))),
    ('m3/s', _Mul(_Mul(meter, 3), _Pow(second, -1))),
    ('mA', create_prefixed_unit(ampere, PREFIXES['m'])),
    ('mCi', create_prefixed_unit(curie, PREFIXES['m'])),
    ('Megajoules', create_prefixed_unit(joule, PREFIXES['M'])),
    ('MeV', create_prefixed_unit(electronvolt, PREFIXES['M'])),
    ('mg', milligram),
    ('mg/hr', _Mul(milligram, _Pow(hour, -1))),
    ('mH', create_prefixed_unit(henry, PREFIXES['m'])),
    ('MHz', create_prefixed_unit(hertz, PREFIXES['M'])),
    ('Millivolts', millivolt),
    ('mL', milliliter),
    ('mL/day', _Mul(milliliter, _Pow(day, -1))),
    ('mL/hr', _Mul(milliliter, _Pow(hour, -1))),
    ('mm', millimeter),
    ('MN', create_prefixed_unit(newton, PREFIXES['M'])),
    ('moles', mol),
    ('ms', millisecond),
    ('mV', create_prefixed_unit(volt, PREFIXES['m'])),
    ('mW', create_prefixed_unit(watt, PREFIXES['m'])),
    ('N', newton),
    ('N/m^{2}', _Mul(newton, _Pow(_Pow(meter, 2), -1))),
    ('N\\: s\\: /\\: m^{2}', _Mul(_Mul(newton, second), _Pow(_Pow(meter, 2), -1))),
    ('N\\cdot m', _Mul(newton, meter)),
    ('N\\cdot m^{2}', _Mul(newton, _Pow(meter, 2))),
    ('nF', create_prefixed_unit(farad, PREFIXES['n'])),
    ('nL', create_prefixed_unit(liter, PREFIXES['n'])),
    ('nm', nanometer),
    ('nm^{-1}', _Pow(nanometer, -1)),
    ('ohms', ohm),
    ('Pa', pascal),
    ('pebibit', create_prefixed_unit(bit, BIN_PREFIXES['Pi'])),
    ('percent', percent),
    ('pF', create_prefixed_unit(farad, PREFIXES['p'])),
    ('pounds', pound),
    ('psi', psi),
    ('rad/s', _Mul(rad, _Pow(second, -1))),
    ('rad/sec', _Mul(rad, _Pow(second, -1))),
    ('rad\\: /\\: sec', _Mul(rad, _Pow(second, -1))),
    ('s', second),
    ('s^{-1}', _Pow(second, -1)),
    ('sec', second),
    ('Seconds', second),
    ('slugs/ft3', _Mul(slug, _Pow(_Mul(foot, 3), -1))),
    ('T', tesla),
    ('uA', create_prefixed_unit(ampere, PREFIXES['mu'])),
    ('uF', create_prefixed_unit(farad, PREFIXES['mu'])),
    ('ug', microgram),
    ('uH', create_prefixed_unit(henry, PREFIXES['mu'])),
    ('uS', create_prefixed_unit(siemens, PREFIXES['mu'])),
    ('V', volt),
    ('V/us', _Mul(volt, _Pow(microsecond, -1))),
    ('V\\cdot m', _Mul(volt, meter)),
    ('Volts', volt),
    ('W', watt),
    ('Watts', watt),
    ('years', year),
    ('years\\: ', year),
    ('yrs', year),
]

# TODO: define additional units, if needed
unsupported_unit_examples = [
    ('\\frac{dB}{decade}', _Mul(gram, _Pow(gram, -1))),
    ('\\frac{dB}{octave}', _Mul(gram, _Pow(gram, -1))),
    ('\\frac{Gs}{A}', _Mul(gauss, _Pow(ampere, -1))),
    # R - https://en.wikipedia.org/wiki/Roentgen_(unit)
    ('\\frac{R}{hr}', _Mul(gram, _Pow(hour, -1))),
    ('\\frac{mR}{hr}', _Mul(gram, _Pow(hour, -1))),
    ('\\frac{Rad}{s}', _Mul(gram, _Pow(second, -1))),
    ('cfm', gram),
    ('ft/(cfm)^{2}', _Mul(foot, _Pow(gram, -1))),
    ('cfs', gram),
    ('dBV', gram),
    ('gpm', gram),
    ('Hp', gram),
    ('mph', _Mul(mile, _Pow(hour, -1))),
    ('knot', gram),
    ('lbf-in', gram),
    ('lbf.ft', gram),
    # M (mol/L) - conflicts with mega prefix
    ('M', gram),
    ('psia', gram),
    ('rpm', gram),
    ('mcg', microgram),
]

bad_suffix_unit_examples = [
    '1',

    # combined prefix with non-abbreviated name

    'Mohms',  # megaohms or M\Omega
    'kohms',  # killiohms or k\Omega
    'kg/kmole',  # kmol
    'mb',  # millibar or mbar

    '10^{-6}\\: \\frac{m^{2}}{s}',
    '\\$',
    '\\$/unit',
    '\\$\\: per\\: unit',
    '\\degree \\: C',
    '\\degree s',  # plural degrees
    'cost\\: per\\: servable\\: pound\\: \\left(EP\\right)',
    '\\frac{\\operatorname{kg}}{m^{3}}',
    '\\frac{\\operatorname{kg}}{s}',
    '\\frac{\\operatorname{kg}m}{s}',
    '\\frac{\\operatorname{km}}{hr}',
    '\\frac{ft}{^{\\prime }s}',
    '\\frac{J}{\\operatorname{kg}K}',
    '\\frac{L_{1}}{R_{total}}',
    '\\frac{L_{2}}{R_{total}}',
    '\\frac{m}{s^{^{2}}}',
    '\\Omega \\: \\left(round\\: to\\: 3\\: decimals\\right)',
    '\\operatorname{cm}',
    '\\operatorname{kg}',
    '\\operatorname{kg}\\cdot m',
    '\\operatorname{kg}\\cdot m^{2}',
    '\\operatorname{kg}m^{2}',
    '\\operatorname{mm}^{2}',
    '\\pi \\: bonds',
    '\\pm \\: s_{a}\\: \\: \\: \\frac{m}{s^{2}}',
    '\\pm s_{a}\\: \\: \\frac{m}{s^{2}}',
    '\\pm s_{x}\\: m',
    '\\sec ',
    '\\text{m s}^{-1}',
    '℃',
    '°C\\: ',
    '+\\: f\\mleft(x,y\\mright)\\text{ ; where f is a general function of x and y}',
    'A\\: peak',
    'ADC',
    'Ap',
    'apartments',
    'atoms',
    'bottles',
    'boxes',
    'cans',
    'carbon\\: atoms',
    'cases',
    'Coulumbs',
    'cubic\\: inches',
    'customers\\: will\\: order\\: asparagus',
    'customers\\: will\\: order\\: fresh\\: fruit',
    'customers\\: will\\: order\\: lemon-pepper\\: chicken',
    'deg\\: C',
    'degrees\\: Celsius',
    'dollar',
    'dollars',
    'E-9',
    'E3',
    'electrons'
    'ft.lbf',  # lbf⋅ft, lb-ft, "pound-foot", lb-ft or ft-lb
    'giga',
    'H\\: \\: \\: \\: \\: \\left(copy\\: from\\: Activity\\: 1\\right)',
    'H\\: \\left(copy\\: from\\: Activity\\: 1\\right)',
    'hydrogen\\: atoms',
    'Hz\\: \\left(10\\%\\: tolerance\\: for\\: this\\: answer\\right)',
    'in.\\: of\\: water\\: \\left(gage\\right)',
    'individuals',
    'k\\Omega ,\\: tolerance\\: \\pm 5\\%',
    'kibit',
    'kN.m',
    'KPa',
    'kPa\\: \\left(abs\\right)',
    'kPa\\: \\left(gage\\right)',
    'kΩ',
    'lb\\: AP',
    'lone\\: pairs',
    'M\\: \\: K_{2}SO_{4}',
    'M\\: potassium\\: sulfate',
    'msec',
    'meters\\: per\\: second',
    'meters\\: per\\: second\\: squared',
    'MeV/nucleon',
    'mile\\left(s\\right)\\: per\\: hour',
    'miles\\: per\\: hour',
    'mV_{p}',
    'mV_{RMS}',
    'N\\: \\left(negative\\right)',
    'neutrons',
    'o',  # meant to be \degree
    'º',
    'on\\: eggplants\\: and\\: kiwis',
    'per\\: 4\\: oz\\: serving',
    'per\\: fl\\: oz',
    'per\\: unit',
    'photons',
    'pico',
    'Pokeballs\\: with\\: her\\: income',
    'polar\\: molecules',
    'PPS',
    'ratio',
    'represents\\: the\\: new\\: \\cos t\\: curve',
    'represents\\: the\\: new\\: cost\\: curve',
    'represents\\: the\\: new\\: ATC\\: curve',
    'rooms',
    'SI\\: units',
    'square\\: inches',
    'svgs',
    'tablets',
    'units',
    'V_{DC}',
    'V_{p}',
    'V_{pp}',
    'V_{RMS}',
    'V\\: \\left(5\\%\\: tolerance\\right)',
    'V\\: to\\: 0V',
    'valence\\: electrons',
    'Vdc',
    'Vmin',
    'Vp',
    'Vpeak',
    'Vpp',
    'Vrms',
    'Vs',
    'year\\left(s\\right)\\: of\\: her\\: life\\: due\\: to\\: bickering',
    'V\\: \\left(5\\%\\: tolerance\\right)',
    'Ω'
]


@pytest.mark.parametrize('input, output', unit_examples)
def test_covert_unit_should_succeed(input, output):
    assert_equal(input, output, parse_letters_as_units=True)


@pytest.mark.parametrize('input', bad_unit_examples)
def test_covert_unit_should_fail(input):
    did_fail = False
    try:
        result = process_sympy(input, parse_letters_as_units=True)
        did_fail = is_or_contains_instance(result, Symbol)
    except Exception:
        did_fail = True
    assert did_fail


@pytest.mark.parametrize('input, output', suffix_unit_examples)
def test_covert_suffix_as_unit_should_succeed(input, output):
    assert_equal(input, output, parse_letters_as_units=True)


@pytest.mark.parametrize('input', bad_suffix_unit_examples)
def test_covert_suffix_as_unit_should_fail(input):
    did_fail = False
    try:
        result = process_sympy(input, parse_letters_as_units=True)
        did_fail = is_or_contains_instance(result, Symbol)
    except Exception:
        did_fail = True
    assert did_fail
