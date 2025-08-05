from faker import Faker
import random
from datetime import datetime
from decimal import Decimal

fake = Faker()

# Helper function to generate a list of fake data
def generate_fake_data(num_instances, entity_name, fields):
    data = []
    print(f"Generating {num_instances} fake {entity_name} instances...")
    for _ in range(num_instances):
        instance = {}
        for field_name, field_type in fields.items():
            if field_type == 'Long' or field_type == 'int':
                instance[field_name] = random.randint(1, 10000) # Generate random IDs
            elif field_type == 'String':
                if 'email' in field_name.lower():
                    instance[field_name] = fake.unique.email()
                elif 'phone' in field_name.lower():
                     instance[field_name] = fake.unique.phone_number()
                elif 'name' in field_name.lower():
                    instance[field_name] = fake.name() if 'artist' in entity_name.lower() or 'customer' in entity_name.lower() or 'user' in entity_name.lower() else fake.word()
                elif 'description' in field_name.lower() or 'biography' in field_name.lower():
                    instance[field_name] = fake.text()
                elif 'address' in field_name.lower():
                    instance[field_name] = fake.address()
                elif 'imageUrl' in field_name.lower():
                    instance[field_name] = fake.image_url()
                elif 'material' in field_name.lower() or 'size' in field_name.lower():
                     instance[field_name] = fake.word()
                elif 'username' in field_name.lower():
                    instance[field_name] = fake.user_name()
                elif 'password' in field_name.lower():
                    instance[field_name] = fake.password()
                elif 'fullName' in field_name.lower():
                    instance[field_name] = fake.name()
                else:
                    instance[field_name] = fake.word()
            elif field_type == 'boolean':
                instance[field_name] = fake.boolean()
            elif field_type == 'BigDecimal':
                instance[field_name] = Decimal(random.randrange(1000, 100000000))/100
            elif field_type == 'LocalDateTime':
                instance[field_name] = fake.date_time_this_year()
            elif field_type == 'OrderType':
                instance[field_name] = random.choice(['IMPORT', 'EXPORT'])
            elif field_type == 'OrderStatus':
                instance[field_name] = random.choice(['PENDING', 'PROCESSING', 'COMPLETED', 'CANCELLED'])
            elif field_type == 'Role':
                instance[field_name] = random.choice(['ADMIN', 'EMPLOYEE', 'CUSTOMER'])
            elif field_type == 'UserStatus':
                instance[field_name] = random.choice(['ACTIVE', 'INACTIVE'])


        data.append(instance)
    print(f"Finished generating fake {entity_name} instances.")
    return data

# Define fields for each entity based on your Java classes
artist_fields = {
    'id': 'Long',
    'name': 'String',
    'biography': 'String',
    'phone': 'String',
    'email': 'String',
    'address': 'String',
    'status': 'boolean'
}

category_fields = {
    'id': 'Long',
    'name': 'String',
    'description': 'String',
    'status': 'boolean'
}

customer_fields = {
    'id': 'Long',
    'name': 'String',
    'phone': 'String',
    'address': 'String',
    'email': 'String',
    'status': 'boolean'
}

order_fields = {
    'id': 'Long',
    'type': 'OrderType',
    'status': 'OrderStatus',
    'orderDate': 'LocalDateTime',
    'totalAmount': 'BigDecimal'
}

painting_fields = {
    'id': 'Long',
    'name': 'String',
    'description': 'String',
    'price': 'BigDecimal',
    'imageUrl': 'String',
    'quantity': 'int',
    'material': 'String',
    'size': 'String',
    'status': 'boolean'
}

user_fields = {
    'id': 'Long',
    'username': 'String',
    'password': 'String',
    'fullName': 'String',
    'email': 'String',
    'role': 'Role',
    'status': 'UserStatus'
}

# Generate fake data for each entity
num_instances = 1000

fake_artists = generate_fake_data(num_instances, 'Artist', artist_fields)
fake_categories = generate_fake_data(num_instances, 'Category', category_fields)
fake_customers = generate_fake_data(num_instances, 'Customer', customer_fields)
fake_orders = generate_fake_data(num_instances, 'Order', order_fields)
fake_paintings = generate_fake_data(num_instances, 'Painting', painting_fields)
fake_users = generate_fake_data(num_instances, 'User', user_fields)

# Now you have lists of dictionaries, each representing a fake instance
# You can use this data to populate your database or for testing purposes

# Example of how to access the generated data:
# print(fake_artists[0])
# print(fake_categories[0])
# print(fake_customers[0])
# print(fake_orders[0])
# print(fake_paintings[0])
# print(fake_users[0])
