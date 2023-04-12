import os
import flow360 as fl
from flow360.examples import OM6wing

here = os.path.dirname(os.path.abspath(__file__))

OM6wing.get_files()


class datafiles:
    output = os.path.join(here, "outputs.yaml")
    geometry = os.path.join(here, "geometry.yaml")
    boundaries = os.path.join(here, "boundaries.yaml")


# submit mesh using mesh JSON from file
volume_mesh = fl.VolumeMesh.from_file(OM6wing.mesh_filename, name="OM6wing-mesh")
volume_mesh = volume_mesh.submit()
print(volume_mesh)

# read simulation params from multiple files
params = fl.Flow360Params(
    geometry=fl.Geometry(datafiles.geometry),
    boundaries=fl.Boundaries(datafiles.boundaries),
    freestream=fl.Freestream.from_speed((286, "m/s"), alpha=3.06),
)

# read params from a different file and append settings:
outputs = fl.Flow360Params(datafiles.output)
params.append(outputs)

case = fl.Case.new("om6wing-from-yaml", params, volume_mesh_id=volume_mesh.id)
case = case.submit()
print(case)