{
    "name": "Room Booking",
    "description": "Module allowing to book rooms",
    "sequence": -100,
    "category": "Managements/Booking",
    "version": "16.0.1.2",
    'author': 'ME',
    "depends": [
        'base',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/booking_view.xml',
        'views/rooms_view.xml',
        'views/menu.xml',
    ],
    'license': 'LGPL-3',
    'application': True,
    'auto_install': False,
}
