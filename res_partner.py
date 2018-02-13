# -*- encoding: utf-8 -*-
#                                                                            #
#   OpenERP Module                                                           #
#   Copyright (C) 2014 Gustavo Lepri <gustavolepri@gmail.com>                #
#                                                                            #
#   This program is free software: you can redistribute it and/or modify     #
#   it under the terms of the GNU Affero General Public License as           #
#   published by the Free Software Foundation, either version 3 of the       #
#   License, or (at your option) any later version.                          #
#                                                                            #
#   This program is distributed in the hope that it will be useful,          #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#   GNU Affero General Public License for more details.                      #
#                                                                            #
#   You should have received a copy of the GNU Affero General Public License #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                            #
##############################################################################

from datetime import datetime
from openerp.osv import orm, fields


class ResPartner(orm.Model):
    _inherit = 'res.partner'

    _columns = {
        'aniversario': fields.date('Data de nascimento'),
        'nome_mae': fields.char('Nome da mãe', size=50),
        'nome_conjuge': fields.char('Nome do(a) cônjuge/companheiro(a)', size=50),
        'sexo': fields.selection([('f', 'Feminino'), ('m', 'Masculino')], 'Sexo'),
        'atividade': fields.selection(
            [
                ('assalariado', 'Assalariado'),
                ('autonomo', 'Autônomo'),
                ('aposentado', 'Aposentado'),
                ('nao_assalariado', 'Não Assalariado'),
                ('estudante', 'Estudante'),
                ('outros', 'Outros')
            ], 'Atividade'),
        'grau_instrucao': fields.selection(
            [
                ('fundamental', 'Fundamental'),
                ('medio', 'Ensino Médio'),
                ('superior', 'Superior')
            ], 'Grau de Instrução'),
        'area_atuacao': fields.selection(
            [
                ('educacao', 'Educação'),
                ('saude', 'Saúde'),
                ('beleza', 'Beleza'),
                ('industria', 'Indústria'),
                ('comercio', 'Comércio'),
                ('outros', 'Outros'),
            ], 'Área de atuação'),
        'como_conheceu': fields.selection(
            [
                ('revendedor', 'Revendedor'),
                ('tv_radio', 'TV/Radio'),
                ('revista', 'Revista'),
                ('amigos', 'Amigos'),
                ('internet', 'Internet'),
                ('outros', 'Outros'),
                ], 'Como você conheceu BeOK?'),
        'revende_outro': fields.selection(
            [
                ('natura', 'Natura'),
                ('jequiti', 'Jequiti'),
                ('hermes', 'Hermes'),
                ('avon', 'Avon'),
                ('outros', 'Outros')
            ], 'Revende outro Catálogo?'),
        'objetivo': fields.selection(
            [
                ('principal', 'Renda Principal'),
                ('proprio', 'Consumo Próprio')
            ], 'Objetivo do(a) candidato(a) a revendedor(a)'),
        'possui_cartoes': fields.selection(
            [
                ('credito', 'Crédito(Visa, Master, Amex, Dinners)'),
                ('lojas', 'Lojas, Magazines, Supermercados'),
                ('nao', 'Não')
            ], 'Possiu outros cartões?'),

    }
