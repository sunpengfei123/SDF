import xml.etree.ElementTree as ET
from sdfGraph import SDFgraph
from sdfGraph import SDFTop
from sdfGraph import DefVertex as DV
from sdfGraph import DefEdge as DE

# 打开xml文档
tree = ET.parse('E:\\TestCase\\2016-TCAD\\GGH92bench\\graph\\GGH92_1.xml')
root = tree.getroot()  # 获得root节点

print(root.tag)
print(root.attrib)

child = root[0]
for childd in child:
    print(childd.tag)
    print(childd.attrib)

for actors in child[1]:
    print(actors.tag)
    print(actors.attrib)

for attributes in root[0]:
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

actorProperties = []
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

# for m in channel_list:
#     print(m['srcActor'])
#     for p in port_mess:
#         if p['actor_name'] == m['srcActor']:
#             print('produce:'+ p[m['srcPort']]['rate'])
#         if p['actor_name'] == m['dstActor']:
#             print('consume:'+ p[m['dstPort']]['rate'])

for v in v_mess:
    print(v)
for c in channel_list:
    print(c)
for p in port_mess:
    print(p)
for m in Mess:
    print(m)