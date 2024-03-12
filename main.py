
# imports
import pybamm


def main() -> None:
    """

    :rtype: None
    """
    model = pybamm.lithium_ion.SPM()

    # setup simulation
    sim = pybamm.Simulation(model)

    # solve simulation over 3600 seconds
    sim.solve([0, 3600])

    # plot simulation result
    sim.plot()


if __name__ == '__main__':
    main()
