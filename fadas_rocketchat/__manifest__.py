{
    'name': 'Fadas do Bem RocketChat', 
    'summary': 'Modulo para integração com o RocketChat',
    'description': """
       ** <p>Módulo de integração com o RocketChat.</p>
        <p>Este módulo permite a integração direta com o RocketChat, permitindo que você adicione um widget de chat ao seu website Odoo.</p>
        <ul>
            <li>Facilita a comunicação com os visitantes do site</li>
            <li>Integração simples e rápida</li>
            <li>Totalmente customizável</li>
        </ul>
    """,
    'version': '1.0.0', 
    'category': 'Tools/UI',
    'license': 'LGPL-3', 
    'author': 'João Victor',
    'website':'https://fadasdobem.com.br',
    'depends': [
        'website',
    ],
    'data': [
        'views/website_templates.xml',
        
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install':False,
    # 'assets': {
    #     'web.assets_backend': [
    #         'comissoes_lugo_tech/static/src/js/assets.xml',
    #     ],
    # },
}