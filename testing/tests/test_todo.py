# -*- coding: utf-8 -*-
from odoo.exceptions import AccessError
from odoo.tests.common import TransactionCase


class TestTodo(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super(TestTodo, self).setUp(*args, **kwargs)
        user_demo = self.env.ref('base.user_demo')
        self.env= self.env(user=user_demo)
        return result

    def test_create(self):
        "Create a simple Todo"
        Todo = self.env['reg.material']
        task = Todo.create({
            'material_code': '001',
            'material_name' : 'Jeans',
            'tipe_material_id' : '2',
            'material_buy_price':120,
            'related_supplier_id':1
            
            })
       

    def test_record_rule(self):
        "Test per user record rules"
        Todo = self.env['todo.task']
        task = Todo.sudo().create({
             'material_code': '001',
            'material_name' : 'Jeans',
            'tipe_material_id' : '2',
            'material_buy_price':120,
            'related_supplier_id':1
            })
        with self.assertRaises(AccessError):
            Todo.browse([task.id]).material_name
