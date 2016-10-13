# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from psycopg2 import IntegrityError
from odoo.exceptions import UserError

class test_home_page(TransactionCase):
    """
    test_home_page: 因为 改变依赖关系，home_page 不能取到
    """
    def test_home_page(self):
        """测试首页的显示情况"""
        partner_action = self.env.ref('base.action_res_users')
        self.env['home.page'].create({'sequence': 10, 'action': partner_action.id, 'menu_type': 'all_business',
                                      'domain': '[]', 'context': '{}'})
        self.env['home.page'].create({'sequence': 10, 'action': partner_action.id, 'menu_type': 'amount_summary',
                                      'domain': [], 'context': {},'note_one':'partner','compute_field_one':'companies_count'})
        self.env['home.page'].create({'sequence': 10, 'action': partner_action.id, 'menu_type': 'report',
                                      'domain': [], 'context': {}})
        self.env['home.page'].get_action_url()

    def test_onchange_action(self):
        '''测试 onchange_action
        '''
        partner_action = self.env.ref('base.action_res_users')
        partner_action = self.env['home.page'].create({'sequence': 10, 'action': partner_action.id, 'menu_type': 'all_business',
                                      'domain': '[]', 'context': '{}'})
        result = partner_action.onchange_action()
        real_result = {'domain': {'view_id': [('model', '=', u'res.partner'), ('type', '=', 'tree')]}}
        self.assertTrue(result == real_result)
