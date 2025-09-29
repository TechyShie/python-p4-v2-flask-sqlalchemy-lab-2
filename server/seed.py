from app import app
from models import db, Customer, Item, Review

# Wrap DB operations in the app context
with app.app_context():
    # Drop and recreate tables
    db.drop_all()
    db.create_all()

    # --- Customers ---
    c1 = Customer(name="Tal Yuri")
    c2 = Customer(name="Alice")
    c3 = Customer(name="Bob")

    db.session.add_all([c1, c2, c3])
    db.session.commit()

    # --- Items ---
    i1 = Item(name="Laptop Backpack", price=49.99)
    i2 = Item(name="Insulated Coffee Mug", price=9.99)
    i3 = Item(name="Wireless Mouse", price=25.50)

    db.session.add_all([i1, i2, i3])
    db.session.commit()

    # --- Reviews ---
    r1 = Review(comment="Love this backpack!", customer=c1, item=i1)
    r2 = Review(comment="Mug keeps coffee hot for hours.", customer=c1, item=i2)
    r3 = Review(comment="Mouse is smooth and fast.", customer=c2, item=i3)
    r4 = Review(comment="Backpack straps could be thicker.", customer=c3, item=i1)

    db.session.add_all([r1, r2, r3, r4])
    db.session.commit()

    print("Database seeded successfully!")
