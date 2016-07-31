import ipywidgets as widgets
import json
from traitlets import Unicode
from clustergrammer import Network

@widgets.register('hello.Hello')
class HelloWorld(widgets.DOMWidget):
    """"""
    _view_name = Unicode('hello_view').tag(sync=True)
    _model_name = Unicode('hello_model').tag(sync=True)
    _view_module = Unicode('clustergrammer_widget').tag(sync=True)
    _model_module = Unicode('clustergrammer_widget').tag(sync=True)
    value = Unicode('updating python by restarting kernel').tag(sync=True)

    print('\n\ninitializing net\n-----------------\n\n')
    net = Network()
    print('loaded file')

    net.load_file('rc_two_cats.txt')

    net.make_clust()

    print(net.viz.keys())

    network = net.viz

    network_string = json.dumps(network)
    network = Unicode(network_string).tag(sync=True)


