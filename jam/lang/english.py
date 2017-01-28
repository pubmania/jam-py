# -*- coding: utf-8 -*-

dictionary = \
{
    'lang':                             'en',
#interface buttons and labels
    'yes':                              'Yes',
    'no':                               'No',
    'ok':                               'OK',
    'cancel':                           'Cancel',
    'delete':                           'Delete',
    'new':                              'New',
    'edit':                             'Edit',
    'copy':                             'Copy',
    'print':                            'Print',
    'save':                             'Save',
    'open':                             'Open',
    'close':                            'Close',
    'select':                           'Select',
    'filter':                           'Filter',
    'apply':                            'Apply',
    'find':                             'Find',
    'replace':                          'Replace',
    'view':                             'View',
    'log_in':                           'Log in',
    'login':                            'Login',
    'password':                         'Password',
    'log_out':                          'Log out',
#runtime messages
    'invalid_int':                      '%s invalid value - must be an integer',
    'invalid_float':                    '%s invalid value - must be a float',
    'invalid_cur':                      '%s invalid value - must be a currency',
    'invalid_date':                     '%s invalid value - must be a date',
    'invalid_bool':                     '%s invalid value - must be a boolean',
    'invalid_value':                    '%s invalid value',
    'value_required':                   'a value is required',
    'invalid_length':                   'Text exceeds the maximum allowed length - %s',
    'save_changes':                     'Data has been modified. Do you want to save changes?',
    'delete_record':                    'Delete the record?',
    'no_record':                        'Record is not selected.',
    'server_request_error':             'Server request error',
    'cant_delete_used_record':          "Can't delete the record. It's being used.",
    'website_maintenance':              "The server is temporarily unavailable.",
    'version_changed':                  "Changed version. Press F5 to apply the changes.",
    'no_task':                          'The project is loading or the creation of the project has not been completed yet.',
    'items_selected':                   "selected: %s",
    'selected_first':                   'Selected first %s records',
    'selection_limit_exceeded':         'Selection limit %s exceeded',
    'invalid_range':                    'Invalid range',
    'range_from':                       'from',
    'range_to':                         'to',
    'not_edit_insert_state':            'Item %s is not in edit or insert state',
    'value_in_empty_dataset':           'Item %s - an attempt to get a field value in the empty dataset',
    'no_primary_field_changing':        'Item %s - changing of the primary field is forbidden',
    'no_deleted_field_changing':        'Item %s - changing of the deleted flag field is forbidden',
    'insert_not_active':                "Item %s - can't insert record: item is not active",
    'insert_not_browse':                "Item %s - can't insert record: item is not in browse state",
    'insert_master_not_changing':       "Item %s - can't insert record: master item is not in edit or insert state",
    'append_not_active':                "Item %s - can't append record: item is not active",
    'append_not_browse':                "Item %s - can't append record: item is not in browse state",
    'append_master_not_changing':       "Item %s - can't append record: master item is not in edit or insert state",
    'edit_not_active':                  "Item %s - can't edit record: item is not active",
    'edit_not_browse':                  "Item %s - can't edit record: item is not in browse state",
    'edit_master_not_changing':         "Item %s - can't edit record: master item is not in edit or insert state",
    'edit_no_records':                  "Item %s - can't edit record: dataset is empty",
    'delete_not_active':                "Item %s - can't delete record: item is not active",
    'delete_master_not_changing':       "Item %s - can't delete record: master item is not in edit or insert state",
    'delete_no_records':                "Item %s - can't delete record: dataset is empty",
    'cancel_invalid_state':             "Item %s - can't cancel: item is not in edit or insert state",
#locale
    'decimal_point':                  'Decimal point',
    'mon_decimal_point':              'Monetory decimal point',
    'mon_thousands_sep':              'Monetory thousands separator',
    'currency_symbol':                'Currency symbol',
    'frac_digits':                    'Number of fractional digits',
    'p_cs_precedes':                  'Currency symbol precedes the value (positive values)',
    'n_cs_precedes':                  'Currency symbol precedes the value (negative values)',
    'p_sep_by_space':                 'Currency symbol is separated by a space (positive values)',
    'n_sep_by_space':                 'Currency symbol is separated by a space (negative values)',
    'positive_sign':                  'Symbol for a positive monetary value',
    'negative_sign':                  'Symbol for a negative monetary value',
    'p_sign_posn':                    'The position of the sign (positive values)',
    'n_sign_posn':                    'The position of the sign (negative values)',
    'd_fmt':                          'Date format string',
    'd_t_fmt':                        'Date and time format string',
#calendar
    'months_short':                   '[Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]',
    'months':                         '[January, February, March, April, May, June, July, August, September, October, November, December]',
    'week_start':                     '0',
    'days_min':                       '[Su, Mo, Tu, We, Th, Fr, Sa, Su]',
#grid
    'page':                           'Page',
    'of':                             'of',
#history
    'created':                        'Created',
    'modified':                       'Modified',
    'deleted':                        'Deleted',
    'by_user':                        'by',
    'old_value':                      'old value',
    'new_value':                      'new value',
#rights messages
    'cant_view':                        '%s: you are not allowed to view',
    'cant_create':                      '%s: you are not allowed to create',
    'cant_edit':                        '%s: you are not allowed to edit',
    'cant_delete':                      '%s: you are not allowed to delete',
#admin fields
    'admin':                            'Administrator',
    'catalogs':                         'Catalogs',
    'journals':                         'Journals',
    'tables':                           'Tables',
    'reports':                          'Reports',
    'details':                          'Details',
    'id':                               'Record ID',
    'deleted_flag':                     'Deleted flag',
    'caption':                          'Caption',
    'name':                             'Name',
    'table_field_name':                 'Field name',
    'table_name':                       'Table name',
    'report_template':                  'Report template',
    'visible':                          'Visible',
    'project':                          'Project',
    'users':                            'Users',
    'roles':                            'Roles',
    'privileges':                       'Privileges',
    'tasks':                            'Task',
    'safe_mode':                        'Safe mode',
    'language':                         'Language',
    'author':                           'Author',
    'interface':                        'Interface',
    'db_type':                          'DB type',
    'db_name':                          'File name',
    'alias':                            'Database',
    'data_type':                        'Type',
    'filter_type':                      'Filter type',
    'size':                             'Size',
    'object':                           'Lookup item',
    'object_field':                     'Lookup field',
    'lookup_values':                    'Lookup values',
    'master_field':                     'Master field',
    'required':                         'Required',
    'calculated':                       'Calc.',
    'default':                          'Default',
    'read_only':                        'Read only',
    'alignment':                        'Alignment',
    'active':                           'Active',
    'date':                             'Date',
    'role':                             'Role',
    'info':                             'Information',
    'item':                             'Item',
    'can_view':                         'Can view',
    'can_create':                       'Can create',
    'can_edit':                         'Can edit',
    'can_delete':                       'Can delete',
    'fields':                           'Fields',
    'field':                            'Field',
    'filter':                           'Filter',
    'filters':                          'Filters',
    'index':                            'Index',
    'index_name':                       'Index name',
    'report_params':                    'Report params',
    'error':                            'Error',
    'debugging':                        'Debugging',
    'con_pool_size':                    'Connection pool size',
    'version':                          'Version',
    'mp_pool':                          'Multiprocessing connection pool',
    'persist_con':                      'Persistent connection',
    'single_file_js':                   'All JS modules in a single file',
    'dynamic_js':                       'Dynamic JS modules loading',
    'session_timeout':                  'Session timeout (seconds)',
    'compressed_js':                    'Compressed JS, CSS files',
    'soft_delete':                      'Soft delete',
    'client_module':                    'Client_module',
    'server_module':                    'Server module',
    'virtual_table':                    'Virtual table',
    'js_external':                      'External js module',
    'primary_key':                      'Primary key field',
    'deleted_flag_field':               'Deleted flag field',
    'master_id':                        'Master ID field',
    'master_rec_id':                    'Master record id field',
    'manual_update':                    'DB manual mode',
    'host':                             'Host',
    'port':                             'Port',
    'encoding':                         'Charset',
    'key':                              'Key',
    'value':                            'Value',
    'lookup_value':                     'Lookup value',
    'multi_select':                     'Multiple selection',
    'multi_select_all':                 'Select all enabled',
    'enable_typehead':                  'Typeahead',
    'default_value':                    'Default value',
    'help':                             'Help',
    'placeholder':                      'Placeholder',
    'descending':                       'Descending',
    'unique_index':                     'Unique',
    'foreign_index':                    'Foreign Index',
    'foreign_field':                    'Foreign Field',
    'find_in_task':                     'Find in task',
    'new_group_type':                   'Select new group type',
#admin interface
    'db':                               'Database',
    'export':                           'Export',
    'import':                           'Import',
    'viewing':                          'View',
    'editing':                          'Edit',
    'filters':                          'Filters',
    'order':                            'Order',
    'indices':                          'Indices',
    'foreign_keys':                     'Foreign keys',
    'select_all':                       'Select all',
    'unselect_all':                     'Unselect all',
    'show_selected':                    'Show selected',
    'show_all':                         'Show all',
    'project_params':                   'Parameters',
    'project_locale':                   'Locale',
    'reserved_word':                    'The name is a reserved word',
    'is_edited':                        '%s is already open for editing. Nevertheless open it?',
    'is_edited_by':                     '%s is already open for editing by %s. Nevertheless open it?',
#editor
    'case_sensitive':                   'Case sensitive',
    'whole_words':                      'Find whole words only',
    'in_task':                          'In task',
    'text_not_found':                   'Text was not found.\nWrap search and find again?',
    'text_changed':                     'Module has been changed.\nDo you want to save it before closing?',
    'go_to_line':                       'Go to line',
    'go_to':                            'Go to',
    'line':                             'Line',
#admin editors
    'caption_name':                     'Name',
    'caption_descening':                'Desc.',
#inport messages
    'import_sqlite_not_supported':      'Import is not supported for SQlite database.',
    'import_reading_data':              'Import: reading data',
    'import_checking_integrity':        'Import: checking data integrity',
    'import_analyzing':                 'Import: analyzing changes',
    'import_waiting_close':             'Import: waiting for connections to close',
    'import_changing_db':               'Import: applying changes to the database',
    'import_changing_admin':            'Import: applying changes to admin.sqlite',
    'import_copying':                   'Import: copying files',
    'import_deleteing_files':           'Import: deleteing tmp files',
#admin messages
    'can_not_connect':                  "Can't connect to the database. %s",
    'field_used_in_filters':            "Can't delete the field %s.\n It's used in filter definitions:\n%s",
    'field_used_in_fields':             "Can't delete the field %s.\n It's used in field definitions:\n%s",
    'field_used_in_indices':            "Can't delete the field %s.\n It's used in index definitions:\n%s",
    'field_is_system':                  "Can't delete the system field.",
    'detail_mess':                      '%s - detail %s',
    'item_used_in_items':               "Can't delete the item %s.\n It's used in item definitions:\n%s",
    'field_mess':                       '%s - field %s',
    'item_used_in_fields':              "Can't delete the item %s.\n It's used in field definitions:\n%s",
    'param_mess':                       '%s - parameter %s',
    'item_used_in_params':              "Can't delete the item %s.\n It's used in param definitions:\n%s",
    'invalid_name':                     'the Name is invalid.',
    'invalid_field_name':               'The field name is invalid.',
    'type_is_required':                 'The field type is required.',
    'size_is_required':                 'The field size is required for text fields.',
    'fields_not_defined':               'Not all field information is specified.',
    'index_name_required':              'The index name is required.',
    'index_fields_required':            'There are no index fields is required.',
    'cant_delete_group':                "Can't delete the group.",
    'object_field_required':            'A lookup field is required',
    'item_with_id_not found':           'Item with id %s not found',
    'lookup_list_is_used_in':           'Lookup list is used in <br> %s',
    'error_creating_table':             'Error while creating table: %s',
    'error_modifying_table':            'Error while modifying table: %s',
    'error_deleting_table':             'Error while deleting table %s: %s',
    'field_no_id':                      'Field %s - id value is not set',
    'error_creating_index':             'Error while creating index %s: %s',
    'error_deleting_index':             'Error while deleting index %s'
}
