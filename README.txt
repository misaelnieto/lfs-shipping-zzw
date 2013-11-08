What is it?
===========

LFS Plugin to calculate the shipping cost based on the zipcode, two or more
zones and the weight, therefore: zzw.


Basic usage
===========

Add your application to the PYTHONPATH.

Add the class ``ZZWPriceCalculator`` to the
``LFS_SHIPPING_METHOD_PRICE_CALCULATORS`` setting. Example::
    
    LFS_SHIPPING_METHOD_PRICE_CALCULATORS = [
        ["lfs.shipping.GrossShippingMethodPriceCalculator", _(u'Price includes tax')],
        ["lfs.shipping.NetShippingMethodPriceCalculator", _(u'Price excludes tax')],
        ["lfs_ZZW.ZZWPriceCalculator", _(u'ZZW')],
    ]


Add the shipping_zzw app to ``settings.INSTALLED_APPS``::


If your are using models (which is completely up to you), add the application
to settings.INSTALLED_APPS and sync your database.

Add a new shipping method and select Zipcode, Zone and Weight from the
``price_calculator`` field.

Save the shipping method.
