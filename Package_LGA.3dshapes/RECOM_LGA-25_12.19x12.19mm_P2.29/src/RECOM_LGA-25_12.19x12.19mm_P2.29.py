# This is a CadQuery script template
# Add your script code below
import cadquery as cq

pcb_x = 12.19
pcb_y = pcb_x
pcb_z = 0.8

can_x = 11.7
can_y = can_x
can_z = 3.75 - pcb_z
can_r = 0.3

pcb = cq.Workplane("XY").box(pcb_x, pcb_y, pcb_z)

s = cq.selectors.StringSyntaxSelector

can = pcb.faces(">Z")\
    .rect(can_x,can_y)\
    .extrude(can_z, combine=False)\
    .edges("|Z").fillet(can_r)\
    .faces(">Z").edges().fillet(can_r)\
    .faces(">Z").rect(can_x-3, can_y-3, forConstruction=True)\
    .vertices(s('<X')-s('<Y'))\
    .hole(1, 0.5)\


show_object(pcb, options={"rgba":(43,142,88, 0)})
show_object(can)
