import xml.etree.ElementTree as ET
from sdfGraph import SDFgraph
from sdfGraph import SDFTop
from sdfGraph import DefVertex as DV
from sdfGraph import DefEdge as DE


class xmlTosdfG:
    def __init__(self, path):
        # 打开xml文档
        self.__tree = ET.parse(path)
        self.__root = self.__tree.getroot()  # 获得root节点

    def get_sdfG(self):
        for attributes in self.__root[0]:
            if attributes.tag == 'sdf':
                sdf = attributes
                sdf_name = sdf.attrib['name']
                sdf_type = sdf.attrib['type']
            if attributes.tag == 'sdfProperties':
                sdfProperties = attributes

        v_list = []
        v_mess = []
        port_mess = []
        channel_list = []
        for attributes in sdf:
            if attributes.tag == 'actor':
                v_mess.append(attributes.attrib)
                v = DV.Vertex(attributes.attrib['name'])
                v_list.append(v)
                mess = {'actor_name': attributes.attrib['name']}
                for aa in attributes:
                    mess = dict(mess, **{(aa.attrib['name']): aa.attrib})
                port_mess.append(mess)

            if attributes.tag == 'channel':
                if not ('initialTokens' in attributes.attrib):
                    attributes.attrib.update({'initialTokens': '0'})
                channel_list.append(attributes.attrib)

        Mess = []
        for attributes in sdfProperties:
            if attributes.tag == 'actorProperties':
                actor_mess = {'name': attributes.attrib['actor']}
                for p in attributes:
                    # print(p.attrib)
                    if not ('default' in p.attrib):
                        p.attrib.update({'default': 'false'})
                    for exe in p:
                        # print(exe.attrib)
                        if exe.tag == 'executionTime':
                            temp = dict(actor_mess, **p.attrib)
                            mess = dict(temp, **exe.attrib)
                            Mess.append(mess)

        sdfg = SDFgraph.SDFgraph(sdf.attrib['name'])

        for v in v_list:
            sdfg.addVertex(v)
        for m in Mess:
            if m['default'] == 'true':
                v = sdfg.getVertexByname(m['name'])
                v.setExeTimeOnMappedProcessor(int(m['time']))
        for c in channel_list:
            for p in port_mess:
                if p['actor_name'] == c['srcActor']:
                    produce = int(p[c['srcPort']]['rate'])
                if p['actor_name'] == c['dstActor']:
                    consume = int(p[c['dstPort']]['rate'])
            e = DE.SDFedge(c['name'], int(c['initialTokens']), produce, consume)
            sdfg.addEdge(sdfg.getVertexByname(str(c['srcActor'])), sdfg.getVertexByname(str(c['dstActor'])), e)

        return sdfg

