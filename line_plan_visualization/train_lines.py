from typing import Iterator

class Lines(object):
    """
    Parameters:
        lines: A dict with Key: ID of a line and Value: a list with only 0 for no stop and 1 for stop at the station corresponding to the PhysicalRailway
    """

    __slots__ = ("__lines", "__linesnum")

    def __init__(self, lines: dict[int, list[int]]) -> None:
        self.__lines: dict[int, list[int]]  = self.__check_lines(lines)
        self.__linesnum: int = len(self.__lines)

    def __repr__(self) -> str:
        return super().__repr__() + "  " + f"lines: {self.__lines}"
    
    def __len__(self) -> int:
        """
        Return:
        The stations num in line.
        """
        return len(list(self.__lines.values())[0])

    def __iter__(self) -> Iterator:
        iter_lines: Iterator = iter([(ID, line) for ID, line in self.__lines.items()])
        return iter_lines


    @property
    def lines(self) -> dict[int, list[int]]:
        return self.__lines
    
    @property
    def linesnum(self) -> int:
        return self.__linesnum

    @staticmethod
    def __check_lines(lines) -> dict[int, list[int]]:
        
        line_lengths: list[int] = []

        if not isinstance(lines, dict):
            raise Exception(f"unexpected {type(lines)} type of {lines}, only 'dict' type")
        
        for ID, line in lines.items():
            if not isinstance(ID, int):
                raise Exception(f"unexpected {type(ID)} type of {ID}, only 'int' type")
            if not isinstance(line, list):
                raise Exception(f"unexpected {type(line)} type of {line}, only 'list' type")
            for is_stop in line:
                if is_stop not in (0, 1):
                    raise Exception(f"unexpected {is_stop}, only 0 or 1")
            line_lengths.append(len(line))
            
        if len(set(line_lengths)) != 1:
            raise Exception(f"different length of lines")
        
        return lines
