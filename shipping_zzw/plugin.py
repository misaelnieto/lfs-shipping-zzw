from django.contrib.sites.models import get_current_site

from lfs.cart.utils import get_cart
from lfs.customer.utils import get_customer
from lfs.plugins import ShippingMethodPriceCalculator


weight_vs_zone = {
    0.50: ['13.82',  '15.48',  '16.23',  '18.24',  '19.67',  '19.86',  '20.89',  '21.49',],
    1.00: ['14.06',  '15.73',  '16.48',  '18.50',  '19.99',  '20.18',  '21.26',  '21.87',],
    2.50: ['14.43',  '16.14',  '16.99',  '19.23',  '21.06',  '21.22',  '22.34',  '22.98',],
    5.00: ['17.01',  '18.96',  '20.51',  '24.83',  '28.79',  '29.07',  '30.62',  '31.49',],
    7.50: ['21.46',  '23.99',  '26.88',  '30.94',  '37.61',  '37.97',  '39.98',  '41.11',],
    10.00: ['25.68',  '28.85',  '33.41',  '38.99',  '48.35',  '48.83',  '51.41',  '52.86',],
    12.50: ['30.16',  '33.72',  '39.60',  '47.69',  '59.10',  '60.18',  '62.83',  '64.61',],
    15.00: ['35.13',  '38.53',  '46.20',  '57.52',  '69.87',  '72.88',  '74.27',  '76.38',],
    17.50: ['39.69',  '43.44',  '52.24',  '66.06',  '80.61',  '85.49',  '85.69',  '88.12',],
    20.00: ['44.34',  '48.27',  '57.98',  '74.85',  '91.40',  '97.25',  '97.27',  '100.35',],
    22.50: ['48.42',  '53.07',  '63.68',  '83.28',  '100.34', '109.71', '109.72', '113.37',],
    25.00: ['52.82',  '58.04',  '69.43',  '92.15',  '106.61', '122.29', '122.30', '126.42',],
    27.50: ['57.24',  '63.00',  '75.89',  '101.13', '116.20', '134.83', '134.89', '139.46',],
    30.00: ['61.70',  '67.97',  '82.55',  '110.11', '126.30', '146.75', '147.47', '152.50',],
    32.50: ['66.08',  '72.94',  '89.36',  '119.09', '136.42', '158.50', '160.05', '165.54',],
    35.00: ['70.05',  '77.41',  '95.41',  '127.17', '145.51', '169.06', '171.38', '177.27',],
    37.50: ['74.89',  '82.87',  '102.86', '137.05', '156.94', '181.98', '185.22', '191.61',],
    40.00: ['79.31',  '87.84',  '109.62', '146.03', '167.40', '193.72', '197.81', '204.66',],
    42.50: ['83.77',  '92.80',  '116.36', '155.01', '177.86', '205.63', '210.40', '217.70',],
    45.00: ['88.15',  '97.77',  '123.01', '163.99', '188.31', '217.37', '222.98', '230.74',],
}


def get_price(zone, weight):
    for wi in sorted(weight_vs_zone.keys()):
        if not weight > wi:
            _wi = wi
            break
    return weight_vs_zone[wi][zone-1]

def get_zone(zip_code):
    """
    Hardcoded ...bum
    """
        #MXL = zona D
    if zip_code >= 0 and zip_code < 17000:
        #D->A = 5
        return 5
    elif zip_code >= 20000 and zip_code < 21000:
        #D->J = 4
        return 4
    elif zip_code >= 21000 and zip_code < 24000:
        #D->D = 1
        return 1
    elif zip_code >= 24000 and zip_code < 25000:
        #D->O = 7
        return 7
    elif zip_code >= 25000 and zip_code < 28000:
        #D->B = 5
        return 5
    elif zip_code >= 28000 and zip_code < 29000:
        #D->I = 7
        return 7
    elif zip_code >= 29000 and zip_code < 31000:
        #D->M =6
        return 6
    elif zip_code >= 31000 and zip_code < 36000:
        #D->G =7
        return 7
    elif zip_code >= 36000 and zip_code < 39000:
        #D->J =4
        return 4
    elif zip_code >= 39000 and zip_code < 42000:
        #D->N =6
        return 6
    elif zip_code >= 42000 and zip_code < 44000:
        #D->A =5
        return 5
    elif zip_code >= 44000 and zip_code < 50000:
        #D->C =4
        return 4
    elif zip_code >= 50000 and zip_code < 58000:
        #D->A =5
        return 5
    elif zip_code >= 58000 and zip_code < 62000:
        #D->K =7
        return 7
    elif zip_code >= 62000 and zip_code < 63000:
        #D->A =5
        return 5
    elif zip_code >= 63000 and zip_code < 64000:
        #D->I =7
        return 7
    elif zip_code >= 64000 and zip_code < 68000:
        #D->B =5
        return 5
    elif zip_code >= 68000 and zip_code < 72000:
        #D->M =6
        return 6
    elif zip_code >= 72000 and zip_code < 76000:
        #D->A =5
        return 5
    elif zip_code >= 76000 and zip_code < 77000:
        #D->J =4
        return 4
    elif zip_code >= 77000 and zip_code < 78000:
        #D->O =7
        return 7
    elif zip_code >= 78000 and zip_code < 80000:
        #D->J =4
        return 4
    elif zip_code >= 80000 and zip_code < 83000:
        #D->E =5
        return 5
    elif zip_code >= 83000 and zip_code < 86000:
        #D->F =6
        return 6
    elif zip_code >= 86000 and zip_code < 87000:
        #D->M =6
        return 6
    elif zip_code >= 87000 and zip_code < 88000:
        #D->L =8
        return 8
    elif zip_code >= 88000 and zip_code < 89000:
        #D->H =7
        return 7
    elif zip_code >= 89000 and zip_code < 90000:
        #D->L =8
        return 9
    elif zip_code >= 90000 and zip_code < 91000:
        #D->A =5
        return 5
    elif zip_code >= 91000 and zip_code < 97000:
        #D->M =6
        return 6
    elif zip_code >= 97000 and zip_code < 98000:
        #D->O =7
        return 7
    elif zip_code >= 98000 and zip_code < 100000:
        #D->J =4
        return 4
    else:
        return 8


class ZZRPriceCalculator(ShippingMethodPriceCalculator):
    #Cache price
    _price = None

    def _compute_price(self):
        #Get the zip_code
        customer = get_customer(self.request)
        ship_address = customer.get_selected_shipping_address()
        zip_code = ship_address.zip_code

        #Lookup the zone based on the ZIP Code and weight
        if zip_code:
            zone = get_zone(int(zip_code))
        else:
            zone = 8
        cart = get_cart(self.request)
        weight = reduce(lambda x, y: x + y.product.weight * y.product.amount, cart.get_items())
        return get_price(zone, weight)

    def get_price_net(self):
        """
        Returns the net price of the shipping method.
        """
        return self.get_price_gross()

    def get_price_gross(self):
        """
        Returns the gross price of the shipping method.
        """
        if self._price is None:
            self._compute_price()
        return self._price
