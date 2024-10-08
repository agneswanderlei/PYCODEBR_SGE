from django.utils.formats import number_format
from products.models import Product
from outflows.models import Outflow
from django.db.models import Sum, F
from django.utils import timezone
from categories.models import Category
from brands.models import Brand


def get_product_metrics():
    products = Product.objects.all()
    total_cost_price = sum(
        product.cost_price * product.quantity for product in products
    )
    total_selling_price = sum(
        product.selling_prince * product.quantity for product in products
    )
    total_quantity = sum(
        product.quantity for product in products
    )
    total_profit = total_selling_price - total_cost_price

    return dict(
        total_cost_price=number_format(
            total_cost_price, decimal_pos=2, force_grouping=True
        ),
        total_selling_price=number_format(
            total_selling_price, decimal_pos=2, force_grouping=True
        ),
        total_quantity=total_quantity,
        total_profit=number_format(
            total_profit, decimal_pos=2, force_grouping=True
        ),
    )


def get_sales_metrics():
    total_sales = Outflow.objects.count()
    total_products_sold = Outflow.objects.aggregate(
        total_products_sold=Sum('quantity')
    )['total_products_sold'] or 0

    total_sale_value = sum(
        outflow.quantity * outflow.product.selling_prince
        for outflow in Outflow.objects.all()
    ) or 0

    total_sales_cost = sum(
        outflow.quantity * outflow.product.cost_price
        for outflow in Outflow.objects.all()
    ) or 0

    total_sale_profit = total_sale_value - total_sales_cost or 0
    return dict(
        total_sales=total_sales,
        total_product_sold=total_products_sold,
        total_sale_value=number_format(
            total_sale_value, decimal_pos=2, force_grouping=True
        ),
        total_sale_profit=number_format(
            total_sale_profit, decimal_pos=2, force_grouping=True
        )
    )


def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_total = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            total_sales=Sum(F('product__selling_prince') * F('quantity'))
        )['total_sales'] or 0
        values.append(float(sales_total))

    return dict(
        dates=dates,
        values=values
    )


def get_daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = list()

    for date in dates:
        sales_quantity = Outflow.objects.filter(created_at__date=date).count()
        quantities.append(sales_quantity)

    return dict(
        dates=dates,
        values=quantities
    )


def get_graphic_product_category_metric():
    categories = Category.objects.all()
    return {
        category.name: Product.objects.filter(category=category).count()
        for category in categories
    }


def get_graphic_product_brand_metric():
    brands = Brand.objects.all()
    return {
        brand.name: Product.objects.filter(brand=brand).count()
        for brand in brands
    }


def get_product_metrics_filter(self):
    products = Product.objects.all()
    brand = self.request.GET.get('brand')
    category = self.request.GET.get('category')

    if brand:
        products = products.filter(brand__id=brand)

    if category:
        products = products.filter(category__id=category)

    total_cost_price = sum(
        product.cost_price * product.quantity for product in products
    )
    total_selling_price = sum(
        product.selling_prince * product.quantity for product in products
    )
    total_quantity = sum(
        product.quantity for product in products
    )
    total_profit = total_selling_price - total_cost_price

    return dict(
        total_cost_price=number_format(
            total_cost_price, decimal_pos=2, force_grouping=True
        ),
        total_selling_price=number_format(
            total_selling_price, decimal_pos=2, force_grouping=True
        ),
        total_quantity=total_quantity,
        total_profit=number_format(
            total_profit, decimal_pos=2, force_grouping=True
        ),
    )
