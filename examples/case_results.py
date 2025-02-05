from pylab import *

from flow360 import MyCases

my_cases = MyCases()

for case in my_cases:
    print(case)
    if case.is_finished() and case.status.value != "error":
        break
    else:
        print(f"Skipping case {case.name} because status={case.status}")

print(case)
print(case.params)

# get residuals:
residuals = case.results.residuals

# print residuals as a table:
print(residuals.raw)

# print other results as tables:
print(case.results.cfl.raw)
print(case.results.total_forces.raw)
print(case.results.linear_residuals.raw)
print(case.results.minmax_state.raw)

# download all result files of the case:
downloaded_files = case.results.download(all=True, destination=case.name)
print(downloaded_files)


# download specific result files of the case:
case.results.download(bet_forces=True, actuator_disk_output=True)

try:
    case.results.total_forces.plot()
except NotImplementedError as e:
    print(e)

# plot some results manually, code will not re-download data, it is already stored in memory
plot(case.results.total_forces.raw["pseudo_step"], case.results.total_forces.raw["CL"])
xlabel("pseudo step")
ylabel("CL")
show()

# alterantive way of plotting using pre-defined plot setup
case.results.plot.total_forces()


try:
    case.results.total_forces.to_csv()
except NotImplementedError as e:
    print(e)
