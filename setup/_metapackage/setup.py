import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-server-ux",
    description="Meta package for oca-server-ux Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-date_range',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
