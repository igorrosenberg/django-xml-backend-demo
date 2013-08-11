from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

def list(request):
    file_list = get_files()
    return render_to_response('xmlview/list.html', { 'file_list': file_list, })

def test(request):
    file_data = get_file_data("1.xml")
    #data = "Hello, world. "
    data = file_data.a.attrib['prop']
    return HttpResponse(data)

def edit(request, xml_id):
    try:
       file_data = get_file_data(xml_id)
       # return HttpResponse(file_data.a)
       return render_to_response(
            'xmlview/edit.html', 
            { 'file_data': file_data, 'file_name': xml_id }, 
            context_instance=RequestContext(request)
            )
    except IOError:
         # File not found
         raise Http404	


def save(request, xml_id):
    try:
       save_file(xml_id, request.POST)
       return HttpResponseRedirect(reverse('xmlview.views.list'))
    except IOError:
         # File not found
         raise Http404	

# Il faudrait externaliser cette partie, qui ressemble a une API d'acces aux donnees.
# On remarque qu'on a perdu les accesseurs habituels, genre get_object_or_404 
# et qu'on doit donc traiter les exceptions

from os import listdir
from os.path import isfile, join

# see http://lxml.de/objectify.html
from lxml import objectify
from lxml import etree

BASE_PATH = 'xmlview/data/'

# List files available
def get_files():
    path = BASE_PATH
    return [ f for f in listdir(path) if isfile(join(path,f)) ]

# Get XML data from a file as a dictionnary object (see lxml.objectify)
# throws IOError if file does not exist
# throws lxml exceptions if XML file has invalid syntax 
def get_file_data(xml_file_name):
    infile = open(BASE_PATH + xml_file_name, 'r')
    xml_data = objectify.parse(infile)
    return xml_data.getroot()
    #return xml_data
    #return etree.tostring(xml_data, pretty_print=True)

# Save data submitted by the user.
# Il manque le traitement d'erreurs (filtrage des entrees utilisateurs)  
def save_file(xml_file_name, submitted_data) :
    file_data = get_file_data(xml_file_name)
    file_data.a = submitted_data['a']
    file_data.a.a1 = submitted_data['a.a1']
    file_data.a.set("prop", submitted_data['a_prop'])
    file_data.b = submitted_data['b']
    objectify.deannotate(file_data, cleanup_namespaces=True)
    xmlString = etree.tostring(file_data, pretty_print=True)
    # file IO
    fo = open(BASE_PATH + xml_file_name, "w")
    fo.write(xmlString);
    fo.close()
    return
