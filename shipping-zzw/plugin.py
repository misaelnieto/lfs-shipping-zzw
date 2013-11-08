from django.contrib.sites.models import get_current_site

from lfs.cart.utils import get_cart
from lfs.customer.utils import get_customer
from lfs.plugins import ShippingMethodPriceCalculator


class ZZRPriceCalculator(ShippingMethodPriceCalculator):
    #Cache price
    _price = None

    def _compute_price(self):
        #Get the zip_code
        customer = get_customer(self.request)
        ship_address = customer.get_selected_shipping_address()
        zip_code = ship_address.zip_code

        #Lookup the zone based on the ZIP Code
        zone = 1 #XXX

        #Lookup price

        return price

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
