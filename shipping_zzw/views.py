from django_datatables_view.base_datatable_view import BaseDatatableView

class ShippingPriceView(BaseDatatableView):
    # The model we're going to show
    model = MyModel

    # define the columns that will be returned
    columns = ['number', 'user', 'state', 'created', 'modified']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['number', 'user', 'state']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'user':
            return '%s %s' % (row.customer_firstname, row.customer_lastname)
        else:
            return super(OrderListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use request parameters to filter queryset

        # simple example:
        sSearch = self.request.POST.get('sSearch', None)
        if sSearch:
            qs = qs.filter(name__istartswith=sSearch)

        # more advanced example
        filter_customer = self.request.POST.get('customer', None)

        if filter_customer:
            customer_parts = filter_customer.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs