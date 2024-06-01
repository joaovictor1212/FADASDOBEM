{
    'name': 'Fadas do Bem RocketChat', 
    'summary': 'Modulo para integração com o RocketChat',
    'description': '''
        Módulo de integração com o RocketChat
    ''',
    'version': '1.0.0', 
    'category': 'Tools/UI',
    'license': 'LGPL-3', 
    'author': 'João Victor',
    'website':'https://fadasdobem.com.br',
    'depends': [
        'website'
    ],
    'data': [
        'views/website_templates.xml',
        
    ],
    # 'qweb': [
    #     'static/src/xml/radio_button_widget.xml',
    # ],
    'installable': True,
    'application': True,
    'auto_install':False,
    # 'assets': {
    #     'web.assets_backend': [
    #         'comissoes_lugo_tech/static/src/js/assets.xml',
    #     ],
    # },
}