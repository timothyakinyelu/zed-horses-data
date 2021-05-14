from flask.views import MethodView
from src.resolvers import DataResolver
from . import bet


class IndexView(MethodView):
    """ run graphql playground locally """
    
    def get(self):
        return DataResolver.getFromZed()


class ReadDataView(MethodView):
    """ read data from file """
    
    def get(self):
        return DataResolver.readZedDataFromFile()



# name routes
index_view = IndexView.as_view('index_view')
read_data_view = ReadDataView.as_view('read_data_view')

# url rule
bet.add_url_rule(
    '/',
    view_func=index_view
)
bet.add_url_rule(
    '/read-data',
    view_func=read_data_view
)