from django.core.management.base import BaseCommand
from ecw.models import Category, Product, Customer, Order, OrderItem
from faker import Faker
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        faker = Faker()

        # Create Categories
        categories = []
        for _ in range(5):
            category = Category.objects.create(
                name=faker.word().capitalize(),
                description=faker.text()
            )
            categories.append(category)

        # Create Products
        products = []
        for _ in range(20):
            product = Product.objects.create(
                title=faker.word().capitalize(),
                description=faker.text(),
                price=Decimal(random.uniform(10.00, 100.00)).quantize(Decimal('0.01')),
                ratings=random.randint(0, 5),
                image='products/default.png',  # Replace with an actual image path if needed
                is_favorite=faker.boolean(),
                add_to_cart=faker.boolean(),
                category=random.choice(categories)
            )
            products.append(product)

        # Create Customers
        customers = []
        for _ in range(10):
            customer = Customer.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                address=faker.address(),
                phone=faker.phone_number()
            )
            customers.append(customer)

        # Create Orders and OrderItems
        for _ in range(15):
            customer = random.choice(customers)
            order = Order.objects.create(
                customer=customer,
                total_amount=Decimal(0.00)
            )
            total_amount = Decimal(0.00)

            for _ in range(random.randint(1, 5)):
                product = random.choice(products)
                quantity = random.randint(1, 5)
                price = product.price
                total_price = price * quantity

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=price,
                    total_price=total_price
                )

                total_amount += total_price

            order.total_amount = total_amount
            order.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
