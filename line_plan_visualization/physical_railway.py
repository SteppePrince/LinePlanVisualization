from typing import Iterator

class PhysicalRailWay(object):
    """
    Parameters:
        name: PhysicalRailway name
        stations: A list which stores each station name on the PhysicalRailway
    """

    __slots__ = ("__name", "__stations")

    def __init__(self, name: str, stations: dict[str, str]) -> None:
        self.__name: str = self.__check_name(name)
        self.__stations: dict[str, str] = self.__check_stations(stations)

    def __repr__(self) -> str:
        return super().__repr__() + "  " + f"name: {self.__name}; stations: {self.__stations}"

    def __len__(self) -> int:
        """
        Return:
        The stations num in physical railway.
        """
        return len(self.__stations)

    def __iter__(self) -> Iterator:
        iter_pr: Iterator = iter([(station, level) for station, level in self.__stations.items()])
        return iter_pr

    @property
    def name(self) -> str:
        return self.__name

    @property
    def stations(self) -> dict[str, str]:
        return self.__stations

    @staticmethod
    def __check_name(name: str) -> str:
        if not isinstance(name, str):
            raise Exception(f"unexpected {type(name)} type of {name}, only 'str' type")
        
        return name

    @staticmethod
    def __check_stations(stations: dict[str, str]) -> dict[str, str]:
        if not isinstance(stations, dict):
            raise Exception(f"unexpected {type(stations)} type of {stations}, only 'dict' type")

        for station, level in stations.items():
            if not isinstance(station, str):
                raise Exception(f"unexpected {type(station)} type of {station}, only 'str' type")
            if level not in ("high", "medium", "low"):
                raise Exception(f"unexpected {level}, only \"high\", \"medium\" or \"low\")")

        if len(stations) < 2:
            raise Exception(f"unexpected length of {stations} that is less than 2")
        
        return stations

