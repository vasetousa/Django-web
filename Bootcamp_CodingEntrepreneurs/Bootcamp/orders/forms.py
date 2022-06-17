from django import forms

from Bootcamp.orders.models import Order


class OrderForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        product = kwargs.pop('product') or None
        super().__init__(*args, **kwargs)
        self.product = product

    class Meta:
        model = Order
        fields = [
            'shipping_address',
            'billing_address',
        ]

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        # check product inventory
        if self.product is not None:
            if not self.product.has_inventory():
                raise forms.ValidationError('This product is out of inventory.')

        return cleaned_data
