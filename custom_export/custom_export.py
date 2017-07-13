# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2015-Today BrowseInfo (<http://www.browseinfo.in>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################
import datetime
import functools
import itertools
import logging
import operator
import pickle
import pytz
import re
import time
from collections import defaultdict, MutableMapping
from inspect import getmembers, currentframe
from operator import itemgetter
from openerp.models import BaseModel
import babel.dates
import dateutil.relativedelta
import psycopg2
from lxml import etree
from openerp import models
import openerp
from openerp import tools, api

#class BaseModel(object):


def __export_xml_id(self):
	if not self._is_an_ordinary_table():
		raise Exception(
                "You can not export the column ID of model %s, because the "
                "table %s is not an ordinary table."
                % (self._name, self._table))
	ir_model_data = self.sudo().env['ir.model.data']
	data = ir_model_data.search([('model', '=', self._name), ('res_id', '=', self.id)])
	if data:
		if data[0].module:
			return '%s.%s' % (data[0].module, data[0].name)
		else:
			return data[0].name
	else:
		postfix = 0
		name = '%s_%s' % (self._table, self.id)
		while ir_model_data.search([('module', '=', '__export__'), ('name', '=', name)]):
			postfix += 1
			name = '%s_%s_%s' % (self._table, self.id, postfix)
		ir_model_data.create({
							'model': self._name,
                'res_id': self.id,
                'module': '__export__',
                'name': name,
            })
		return '__export__.' + name	
           
           
@api.multi
def __export_row(self,fields=None):
	""" Export fields of the records in ``self``.

	:param fields: list of lists of fields to traverse
	:return: list of lists of corresponding values
    """
	lines = []
	for record in self:
		user = self.env['res.users'].browse(record._uid)
		lang = self.env['res.lang'].search([('code','=',user.lang)])
		current = [''] * len(fields)
		lines.append(current)
		primary_done = []
		for i, path in enumerate(fields):
			if not path:
				continue
			name = path[0]
			if name in primary_done:
				continue
			if name == '.id':
				current[i] = str(record.id)
			elif name == 'id':
				current[i] = record.__export_xml_id()
			else:
				field = record._fields[name]
				if field.type == 'date':
					if record[name]:
						val = record[name]
						value = datetime.datetime.strptime(val, '%Y-%m-%d').strftime(lang.date_format)
					else:
						value = ''
				elif field.type == 'datetime':
					if record[name]:
						val = record[name]
						value = datetime.datetime.strptime(val, '%Y-%m-%d %H:%M:%S').strftime(lang.date_format +' '+ lang.time_format)
					else:
						value = ''
				elif field.type == 'boolean':
					if record[name]:
						val = record[name]
						if val == False:
							value = ''
						else:
							value = record[name]
					else:
						value = ''
				else:
					value = record[name]
				if not isinstance(value, BaseModel):
					current[i] = field.convert_to_export(value, self.env)
				else:
					primary_done.append(name)

					if field.type == 'many2many' and len(path) > 1 and path[1] == 'id':
						xml_ids = [r.__export_xml_id() for r in value]
						current[i] = ','.join(xml_ids) or False
						continue

					fields2 = [(p[1:] if p and p[0] == name else []) for p in fields]
					lines2 = value.__export_rows(fields2)
					if lines2:
						for j, val in enumerate(lines2[0]):
							if val:
								current[j] = val
						if not current[i]:
							xml_ids = [item[1] for item in value.name_get()]
							current[i] = ','.join(xml_ids)
						else:
							lines += lines2[1:]
					else:
						current[i] = False

	return lines


def fix_import_export_id_paths(fieldname):
    fixed_db_id = re.sub(r'([^/])\.id', r'\1/.id', fieldname)
    fixed_external_id = re.sub(r'([^/]):id', r'\1/id', fixed_db_id)
    return fixed_external_id.split('/')

@api.multi
def export_data(self, fields_to_export, raw_data=False):
	fields_to_export = map(fix_import_export_id_paths, fields_to_export)
	if raw_data:
		self = self.with_context(export_raw_data=True)
	return {'datas': self.__export_rows(fields_to_export)}
 
BaseModel.__export_xml_id = __export_xml_id 
BaseModel.fix_import_export_id_paths = fix_import_export_id_paths
BaseModel.export_data = export_data
BaseModel.__export_rows = __export_row

























