# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headers
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''a
        Emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Output data in plain-text format.
    '''
    def headings(self, headers):
        separator = '-' * (len(headers) * 10)
        print(' 	'.join(headers))
        print(separator)
        
    def row(self, rowdata):
         print('	'.join(rowdata))


class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
       print(', '.join(headers)) 
    def row(self, rowdata):
       print(', '.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for header in headers:
            print(f'<th>{header}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for data in rowdata:
            print(f'<td>{data}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(name):
    '''
    Create an appropriate formatter given an output format name
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [ str(getattr(obj, name)) for name in columns ]
        formatter.row(rowdata)